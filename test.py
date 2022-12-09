# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:28:38 2022

@author: sachin kelkar
"""
import EXOSIMS,EXOSIMS.MissionSim,os.path
scriptfile = os.path.join(EXOSIMS.__path__[0],'Scripts','sampleScript_occulter.json')
sim = EXOSIMS.MissionSim.MissionSim(scriptfile)

""" Creates keepout map for 1973 stars for 1827 days ~5Y missions time
"""
sim.SurveySimulation.koMaps['occulter'].astype(int) 