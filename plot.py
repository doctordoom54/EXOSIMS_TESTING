import EXOSIMS,EXOSIMS.MissionSim,os.path
import pandas as pd 
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

scriptfile = os.path.join(EXOSIMS.__path__[0],'Scripts','multiOcculterScript_test.json')
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)

#read pickle file
DRM = pd.read_pickle(r'DRM_newsim2.pkl')

sim.SurveySimulation.DRM = DRM
#create an empty array
b = np.zeros((len(DRM),2))

ind = np.zeros(len(DRM))
comp = np.zeros(len(ind))

#extracting index
for i in range(0,len(DRM)):
    ind[i] = sim.SurveySimulation.DRM[i]['star_ind']

#extracting completeness 
for i in range(0,len(DRM)):
    comp[i] = sim.TargetList.int_comp[int(ind[i])]

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

#checking if scheduler selects observable targets

koMap = sim.SurveySimulation.koMaps['occulter_1'].astype(int)
q = 0
for j in range(0,len(DRM)):
    #start time of observation (normalized)
    st = np.int64(DRM[j]['arrival_time'].value)
    #end time of observation (normalized)
    et =st + np.int64(DRM[j]['det_time'].value)
    #ind
    ind = DRM[j]['star_ind']
    if q==0:
        slew = int(DRM[j]['slew_time_1'].value)
        q = 1
    else:
        slew = int(DRM[j]['slew_time_2'].value)
        q = 0
    count  = np.all(koMap[ind,st:et])
    if count == 0:
        print("star with ind" ,j ,"is not observable but observed??")



#plot the schedule
plt.figure()
plt.subplot(111, projection="aitoff")
plt.grid(True)
plt.scatter(r_1,d_1,c = comp[0::2])
plt.plot(r_1,d_1)
plt.scatter(r_2,d_2, c = comp[1::2])
plt.plot(r_2,d_2)
plt.colorbar(label='Completeness')
plt.show()
