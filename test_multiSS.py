import EXOSIMS,EXOSIMS.MissionSim,os.path
import pickle
scriptfile = os.path.join(EXOSIMS.__path__[0],'Scripts','multiOcculterScript_test.json')
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)
sim.run_sim()
DRM = sim.SurveySimulation.DRM

