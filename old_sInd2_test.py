import numpy as np

A = np.arange(100)
sInd = None
old_sInd = None
i = 0
s = [None, None]

while i < 5:
    s = [old_sInd, sInd]
    old_sInd = sInd
    sInd = np.random.choice(A)
    print("current choice is", sInd)
    print("current choice is", old_sInd)
    print(s)
    i = i + 1


def test(old_sInd, sInd):
    p = np.arccos(np.clip(np.dot(old_sInd, sInd), -1, 1))
    return p


t = test(s[1], 0)
print(t)
