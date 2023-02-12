import EXOSIMS,EXOSIMS.MissionSim,os.path
scriptfile = os.path.join(EXOSIMS.__path__[0],'Scripts','multiOcculterScript_test.json')
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)
"""sim.run_sim()"""
