"""
Background: Multiple StarShade occulter setup for an exoplanet imaging mission has been in the discussion for a while
this scheduler uses 2 StarShades and checks if there is a significant increase in the science yield from a given mission timeline when compared to a
blind search, random walk or a single occulter mission
"""

from EXOSIMS.Prototypes.SurveySimulation import SurveySimulation
import astropy.units as u
import numpy as np
import astropy.constants as const
import astropy.time as time

class multiSScheduler_SK(SurveySimulation):

    def _init_(self, coeff=[1,1,2,np.e,np.e], revisit_wait=1, **specs):

        SurveySimulation._init_(self, **specs)

        #verify that coefficients imputs are iterable 1xn
        if not(isinstance(coeffs,(list,tuple,np.ndarray))) or len(coeffs)!= 5:
            raise(TypeError("Coeffs are not it  iterable or of insufficient length"))

        #adding the input to outspec
        self._outspec['coeffs']=coeffs
        self._outspec['revisit_wait']=revisit_wait

        #normalizing coefficients
        coeffs=np.array(coeffs)                 # this is an array of coeffs
        cofffs=coeffs/np.linalg.norm(coeffs)    #normalizing

        self.coeffs=coeffs
        self.revisit_wait=revisit_wait*u.d
        self.no_dets= np.ones(self.TargetList.nStars, dtype=bool)

        #Taking the second step, at mission start this is the star with highest completeness
        #this variable is named old_sInd as per the inputs required by choose_next_target method
        self.old_sInd = old_sInd
        self.second_step = second_step


    def choose_next_target(self, old_sInd, sInds, slewTimes, intTimes):
        """Choose next target based on depth 2 search using cost function matrix

        Args:
            old_sInd (list(Integers)):
                Index of the previous target star
            sInds (integer array):
                Indices of available targets
            slewTimes (astropy quantity array):
                slew times to all stars (must be indexed by sInds)
            intTimes (astropy Quantity array):
                Integration times for detection in units of day

        Returns:
            sInd (integer):
                Index of next target star
            waitTime (astropy Quantity):
                the amount of time to wait (this method returns None)

        """

        Comp = self.Completeness
        TL = self.TargetList
        TK = self.TimeKeeping
        OS = self.OpticalSystem
        Obs = self.Observatory
        allModes = OS.observingModes

        #changing sInds to array:
        sInds = np.array(sInds, ndmin=1, copy=False)

        #checking if this is the first step or not
        if (old_sInd is not None) and (second_step is not None):
            sInds = np.append(sInds,second_step,old_sInd)

        # calculate dt since previous observation
        dt = TK.currentTimeNorm.copy() + slewTimes[sInds] - self.lastObsTimes[sInds]
        # get dynamic completeness values
        comps = Comp.completeness_update(TL, sInds, self.starVisits[sInds], dt)

        #length of index Star array
        nStars = len(sInds)

        #define the cost matrix
        A = np.array(nStars,nStars)

        #if this is the first step
        if (old_sInd is None) or (nStars ==1):
            sInd = np.random.choice(sInds[comps == max(comps)])
            return sInd, slewTimes[sInd]

        #populate the matrix with cost elements

        #adding factor for deltaV
        if OS.haveOcculter:
            r_ts = TL.starprop(sInds, TK.currentTimeAbs.copy())
            u_ts = (r_ts.to("AU").value.T/np.linalg.norm(r_ts.to("AU").value, axis=1)).T
            angdists = np.arccos(np.clip(np.dot(u_ts, u_ts.T), -1, 1))
            A[np.ones((nStars), dtype=bool)] = angdists
            A = self.coeff[1]*(A)/np.pi

        #adding value for completeness

        #adding factor for minimum visits

        #adding factor for integration time vs slewTimes

        #adding factor revisit Cost

        #checking for keepout boolean

        # kill diagonal ( filling arbitrary large number)
        np.fill_diagonal(A,1e9)

        #prune the row with index (secon_step,n) assigning arbitrary large number to the matrix
        if second_step is not None:
            A[second_step,:] = 1e9

        #select the minimum cost element
        B = np.unravel_index(A.argmin(),A.shape)
        self.first_step = B[0]
        self.second_step = B[1]

        #check if current time < mission times

        #return required variables





    def next_target(self, old_sInd, mode):
        return sInds, DRM, det_intTime
