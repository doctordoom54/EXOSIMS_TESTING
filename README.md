# EXOSIMS_TESTING
Testing scheduling algorithm before implementing in the workflow 
All the required function are updated in helpfun file. 
Use the multiSS.py file to run the sim, the size of target is determined by EXOCAT1 catalog size #2051. 
This file is dependent on latest EXOSIMS version and related dependencies. 
Might take a while to run for the first time. This repo also contains the DRM pickle files which stores simulation data for various algorithm I've been testing, the observation schedule can be visualized by using the `plot.py` file in the same repo. The user needs to install latest version of EXOSIMS to do so. For generating the final results use the pkl files of wTf_nRuns.pkl type. Using `testCompare.py` file extract number of total detections. Use `Histogram.m` files for plotting the distribution of different runs.  
