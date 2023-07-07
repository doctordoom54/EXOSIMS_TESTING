import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#import pickle data
data = pd.read_pickle(r"July7Runs.pkl")
data1 = pd.read_pickle(r"Ensemble300rand.pkl")

#extract plots for scheduler runs
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
print("done")
mu = np.mean(dets)
sigma = np.std(dets)

#extract plots for random scheduler runs

det1 = []
dets1 = np.zeros((0,len(data1)))
for i in range(0,len(data1)):
    for j in range(0,len(data1[i])):
        q = np.count_nonzero(data1[i][j]['det_status']==1)
        det1 = np.append(det1,q)
    s = np.sum(det1)
    dets1 = np.append(dets1,s)
    s = 0
    det1 = []
print("done")
mu1 = np.mean(dets1)
sigma1 = np.std(dets1)

fig, ax = plt.subplots()
#make individual plots
#scheduler runs
counts, bins = np.histogram(dets)
plt.hist(bins[:-1], bins, weights=counts)
#random runs

counts1, bins1 = np.histogram(dets1)
plt.hist(bins1[:-1], bins1, weights=counts1)




