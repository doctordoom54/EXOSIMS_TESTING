import numpy as np

A = np.arange(100)
sInd = None
old_sInd = None
i = 0
last2Targets = [None, None]
starVisits = np.zeros(len(A))

while i < len(A):
    last2Targets = [old_sInd, sInd]
    old_sInd = sInd
    sInd = np.random.choice(A)
    print("current choice is", sInd)
    print("current choice is", old_sInd)
    starVisits[sInd] += 1
    print(last2Targets)
    i = i + 1


def test(old_sInd, sInd):
    p = np.arccos(np.clip(np.dot(old_sInd, sInd), -1, 1))
    return p


t = test(last2Targets[1], 0)
print(t)
