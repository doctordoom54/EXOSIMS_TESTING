import pandas as pd
import numpy as np
data = pd.read_pickle(r"July17.pkl")
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