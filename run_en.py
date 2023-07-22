import EXOSIMS,EXOSIMS.MissionSim,os.path
import numpy as np
scriptfile = os.path.join(EXOSIMS.__path__[0],'Scripts','TwoStarshadeThreeYears.json')
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)
data = sim.run_ensemble(300)

# code to calculate distibution of planet detection and so on..
det = []
dets = np.zeros((0,len(data)))
for i in range(0,len(data)):
    for j in range(0,len(data[i])):
        q = np.count_nonzero(data[i][j]['det_status']==1)
        det = np.append(det,q)
    s = np.sum(det)
    dets = np.append(dets,s)
    s = 0
    det = []    