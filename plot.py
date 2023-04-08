import EXOSIMS,EXOSIMS.MissionSim,os.path
import pandas as pd 
import astropy.units as u
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import numpy as np
scriptfile = os.path.join(EXOSIMS.__path__[0],'Scripts','multiOcculterScript_test.json')
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)

#read pickle file
DRM = pd.read_pickle(r'DRM.pkl')

sim.SurveySimulation.DRM = DRM
#create an empty array
b = np.zeros((len(DRM),2))


for i in range(0,len(DRM)):
    b[i,0] = sim.TargetList.coords[sim.SurveySimulation.DRM[i]['star_ind']].ra.wrap_at(180 * u.deg).radian
    b[i,1] = sim.TargetList.coords[sim.SurveySimulation.DRM[i]['star_ind']].dec.radian

r = b[:,0]
d = b[:,1]
#plot the schedule
plt.figure()
plt.subplot(111, projection="aitoff")
plt.grid(True)
plt.title("Aitoff projection of our greedy schedule")
plt.scatter(r,d)
plt.plot(r,d)
plt.show()



