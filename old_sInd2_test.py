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
    print("current target is", sInd)
    print("last target was", old_sInd)
    starVisits[sInd] += 1
    print("last 2 targets were", last2Targets)
    i = i + 1


def test(old_sInd, sInd):
    p = np.arccos(np.clip(np.dot(old_sInd, sInd), -1, 1))
    return p


t = test(last2Targets[1], 0)
print(t)
