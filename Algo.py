# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:28:11 2022

@author: sachin kelkar
"""

import numpy as np
from helpfun import fill_diag, row_op
import EXOSIMS, EXOSIMS.MissionSim, os.path

scriptfile = os.path.join(
    EXOSIMS.__path__[0], "Scripts", "sampleScript_occulter.json"
)
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)
koMap = sim.SurveySimulation.koMaps["occulter"].astype(int)

# index of stars
sInds = np.arange(200)

# define mission time of 5 years with dt = 1 day
tf = np.linspace(1, 365 * 5 + 2, 365 * 5 + 2, dtype=int)

# define random completness values
comp = np.random.rand(len(sInds), 1)

# define a random keepout
ko = np.random.randint(0, high=2, size=(len(sInds), 1825)).astype(bool)

# define random coordinates
u = np.random.uniform(low=0.5, high=13.3, size=(len(sInds), 3))

# define random integration time
intime = np.random.randint(1, high=10, size=(len(sInds), 1))

# generate random slew times
slew = np.random.randint(5, high=25, size=(len(sInds), 1))
nstars = len(sInds)

# define an empty cost matrix
A = np.zeros((nstars, nstars))
coeff = np.array([-1, -2, -3, -np.e, -np.pi])
cn = coeff / np.linalg.norm(coeff)
tc = 0  # current time/mission start
i = 0
ko_tot = 0
while tc < len(tf):
    if i == 0:
        # select the first target with maximum completness value
        index = np.unravel_index(comp.argmax(), comp.shape)
        A_i = sInds[index[0]]

        # fill diagonal with arbitrary high values
        fill_diag(A)

        # fill the row corresponding to the selected first value with arbitrary high number
        row_op(A, A_i)

        # total completness of index (m,n)
        x, y = np.meshgrid(comp, comp)
        COMP = x + y

        # matrix updated with completness cost
        A = A + cn[1] * (comp[A_i] + COMP)

        # Calculating unit vector
        u = u.T / np.linalg.norm(u, axis=1).T
        u = u.T

        # taking the angular separation between first target and rest the available targets
        ang = np.arccos(np.clip(np.dot(u[A_i, :], u.T), -1, 1))
        # converting the angular separation between A_i and y_i into NxN
        ang = np.repeat([ang], len(sInds), axis=0)

        # updating the cost matrix with angular separation cost
        A = A + ang * cn[4]

        # getting the next two steps from lowest cost element
        steps = np.unravel_index(A.argmin(), A.shape)

        order = np.reshape(np.array([A_i, steps[0], steps[1]]), (1, 3))
        ko1 = ko[A_i, 0 : intime[A_i].item()]
        ko2 = ko[steps[0].item(), 0 : intime[steps[0]].item()]
        ko3 = ko[steps[1].item(), 0 : intime[steps[1]].item()]
        ko_tot = np.prod(ko1) * np.prod(ko2) * np.prod(ko2)
        tint = intime[sInds[steps[1]]] + intime[sInds[steps[0]]] + intime[A_i]
        tc = tc + tint  # add integration time to current time
        i = i + 1
        print(order)
        print(tc)

    else:
        tc = tc + 100  # check for loop to run
        print(tc)
