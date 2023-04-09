import EXOSIMS,EXOSIMS.MissionSim,os.path
import pandas as pd 
import astropy.units as u
import matplotlib.pyplot as plt
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


#extracting coordinates of all targets

a = np.zeros((len(sim.TargetList.coords),2))

for p in range(0,len(sim.TargetList.coords)):
    a[p,0] = sim.TargetList.coords[p].ra.wrap_at(180 * u.deg).radian
    a[p,1] = sim.TargetList.coords[p].dec.radian

R = a[:,0]
D = a[:,1]

#targets from 1st Starshade
r_1 = b[0::2,0]
d_1 = b[0::2,1]

#targets from 2nd Starshade
r_2 = b[1::2,0]
d_2 = b[1::2,1]


#plot the schedule
plt.figure()
plt.subplot(111, projection="aitoff")
plt.grid(True)
plt.scatter(r_1,d_1)
plt.plot(r_1,d_1)
plt.scatter(r_2,d_2)
plt.plot(r_2,d_2)
plt.show()



