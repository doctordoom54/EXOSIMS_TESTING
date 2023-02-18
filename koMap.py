import numpy as np
from add import TMT

i = 0
a = np.random.randint(10, size=(5, 5))
A = 1
counter = 0
while A == 1:
    h = np.unravel_index(a.argmin(), a.shape)
    t = np.random.choice([1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1])
    y = np.random.choice([1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1])
    counter = counter + 1
    print(t)
    print(y)
    A = t + y
    if A == 0:
        pass
    else:
        print(counter)
        print("test t,y")
        A = 1

r = TMT(4,3,5)
p = TMT(5,4,7)

""" showing shubham how it works"""