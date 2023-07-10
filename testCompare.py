import EXOSIMS,EXOSIMS.MissionSim,os.path
import numpy as np
import pickle
scriptfile = os.path.join(EXOSIMS.__path__[0],'Scripts','TwoStarshadeThreeYears.json')
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)
sim.run_sim()
DRM = sim.SurveySimulation.DRM
det =[]
for j in range(0,len(DRM)):
    q = np.count_nonzero(DRM[j]['det_status']==1)
    det = np.append(det,q)
print(np.sum(det))