# Covid-19 SIR Simulation
# Date: 31.03.2020
# Version 1.1

import math
from matplotlib import pyplot as plt
import numpy as np

S = np.empty(1000)
I = np.empty(1000)
R = np.empty(1000)

t=1
S[0] = 1000
I[0] = 10
R[0] = 0

time_array = [i for i in range(1000)]

# run simulation
while t < 1000:
    s = -0.0005*S[t-1]*I[t-1]
    i = 0.0005 * S[t-1] * I[t-1] - 1/14*I[t-1]
    r = 1/14*I[t-1]

    S[t] = S[t-1] + math.floor(s)
    I[t] = I[t-1] + math.floor(i)
    R[t] = R[t-1] + math.floor(r)    
    t+=1

plt.plot(time_array, I)
plt.plot(time_array, S)
plt.plot(time_array, R)

plt.show()