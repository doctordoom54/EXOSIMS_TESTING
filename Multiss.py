"""
Created on Mon Nov 28 01:04:35 2022

@author: sachin kelkar
"""


def multiss(Ind):

    """
    Ind: Strictly 2052 to match the keepout dimensions (int)
    """

    import numpy as np
    import EXOSIMS, EXOSIMS.MissionSim, os.path

    scriptfile = os.path.join(
        EXOSIMS.__path__[0], "Scripts", "sampleScript_occulter.json"
    )
    sim = EXOSIMS.MissionSim.MissionSim(scriptfile)
    from helpfun import (
        fill_diag,
        row_op,
        com_del,
        targets_del,
        revisit,
        revisit_fun,
        fill_d,
    )

    # index of stars
    sInds = np.arange(Ind)

    # define mission time of 5 years with dt = 1 day
    tf = np.linspace(1, 365 * 5 + 2, 365 * 5 + 2, dtype=int)

    # define random completness values
    comp = np.random.rand(len(sInds), 1)

    # define random coordinates
    u = np.random.uniform(low=0.5, high=33.3, size=(len(sInds), 3))

    # define random integration time
    intime = np.random.randint(6, high=45, size=(len(sInds), 1))

    # generate random slew times
    slew = np.random.randint(5, high=25, size=(len(sInds), 1))
    nstars = len(sInds)

    # define an empty cost matrix
    A = np.zeros((nstars, nstars))
    coeff = np.array([100, -200, -300, -np.e, -np.pi])
    cn = coeff / np.linalg.norm(coeff)

    # generate a keepout map
    koMap = sim.SurveySimulation.koMaps["occulter"].astype(int)

    tc = 0  # current time/mission start
    i = 0  # mission counter
    ##select the first target with maximum completness value and check if it's in the keepout
    k = 0  # keepout counter
    ko2 = 0
    co = np.copy(comp)
    while tc < len(tf):
        if i == 0:

            while k == 0:
                index = np.unravel_index(co.argmax(), co.shape)
                A_i = sInds[index[0]]
                k = np.prod(koMap[A_i, 0 : intime.item(A_i)])
                if k == 0:
                    co = com_del(co, A_i)
                tc = tc + intime[A_i]

            ko = 0  # keepout counter for next 2 targets
            B = np.copy(A)  # copying the cost matrix

            while ko == 0:
                # fill diagonal with arbitrary high values
                fill_diag(B)

                # fill the row corresponding to the selected first value with arbitrary high number
                row_op(B, A_i)

                # total completness of index (m,n)
                x, y = np.meshgrid(comp, comp)
                COMP = x + y

                # matrix updated with completness cost
                B = B + cn[1] * (comp[A_i] + COMP)

                # Calculating unit vector
                u = u.T / np.linalg.norm(u, axis=1).T
                u = u.T

                # taking the angular separation between first target and rest the available targets
                ang = np.arccos(np.clip(np.dot(u[A_i, :], u.T), -1, 1))

                # converting the angular separation between A_i and y_i into NxN
                ang = np.repeat([ang], len(sInds), axis=0)

                # updating the cost matrix with angular separation cost
                B = B + ang * cn[2]

                # getting the next two steps from lowest cost element
                steps = np.unravel_index(B.argmin(), B.shape)
                ko = np.prod(
                    koMap[steps[0], tc.item() : intime.item(steps[0])]
                ) * np.prod(
                    koMap[
                        steps[1],
                        tc.item()
                        + intime.item(steps[0]) : intime.item(steps[1]),
                    ]
                )

                if ko == 0:
                    B = targets_del(B, steps[0], steps[1])
                order = np.reshape(np.array([A_i, steps[0], steps[1]]), (1, 3))

            tc = (
                tc + intime[steps[0]] + intime[steps[1]]
            )  # adding integration time to current time

            # create a null matrix for keeping tab of number of observations done

            Null = np.zeros(
                (1, len(sInds))
            )  # initial matrix for keeping count of number of observations done

            revisit_0 = (
                revisit(len(sInds), Null, A_i)
                + revisit(len(sInds), Null, steps[0])
                + revisit(len(sInds), Null, steps[1])
            )
            x, y = np.meshgrid(revisit_0, revisit_0)
            revisit_tab = x * y
            i = i + 1

        else:
            C = np.copy(A)
            # fill diagonal with arbitrary high values
            T = order
            while ko2 == 0 and tc < len(tf):
                fill_diag(C)
                # fill the row corresponding to the selected first value with arbitrary high number
                row_op(C, T[-1])
                # cost for calculating angular separation
                u1 = np.arccos(np.clip(np.dot(u[T.item(-1), :], u.T), -1, 1))
                u2 = np.arccos(np.clip(np.dot(u[T.item(-2), :], u.T), -1, 1))
                u, w = np.meshgrid(u1, u2)
                # angular separation matrix between y_i-1,y_i &x_i-1,x_i
                ANG = u + w
                # total completness of index (m,n)
                x, y = np.meshgrid(comp, comp)
                COMP = x + y
                # matrix updated with completness costs
                C = (
                    C
                    + cn[2] * (1 - COMP)
                    + (revisit_tab * cn[0] * np.exp(tc / 100))
                    + ANG * cn[1] * np.pi
                )
                # getting the next two steps from lowest cost element
                step = np.unravel_index(C.argmin(), C.shape)
                step = np.asarray(step)
                ko2 = np.prod(
                    koMap[step[0], tc.item() : intime.item(step[0])]
                ) * np.prod(
                    koMap[
                        step[1],
                        tc.item()
                        + intime.item(step[0]) : intime.item(step[1]),
                    ]
                )

                if ko2 == 0:
                    C = targets_del(C, step[0], step[1])
                else:
                    # append the targets in the order
                    T = np.append(T, step)
                    # adding integration time to current time
                    tc = tc + intime[step[0]] + intime[step[1]]
                    revisit_tab = revisit_fun(
                        revisit_tab, step[0], step[1], len(sInds)
                    )
                ko2 = 0
                print(tc)

            # check for loop to run
            print(T)
    return T
