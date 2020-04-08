# Covid-19 SIR Simulation
# Date: 31.03.2020
# Version 1.1

import datetime
import math
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame

data = pd.read_csv('covid-19.csv')
dates = np.asarray(data['Date'])
daily_cases = np.asarray(data['New Cases'])


S = np.empty(69)
I = np.empty(69)
R = np.empty(69)

t=1
S[0] = 1000
I[0] = 10
R[0] = 0

#time_array = [i for i in range(69)]

# run simulation
while t < 69:
    s = -0.0005*S[t-1]*I[t-1]
    i = 0.0005 * S[t-1] * I[t-1] - 1/14*I[t-1]
    r = 1/14*I[t-1]

    S[t] = S[t-1] + math.floor(s)
    I[t] = I[t-1] + math.floor(i)
    R[t] = R[t-1] + math.floor(r)    
    t+=1

#plt.plot(dates, I)
#plt.plot(dates, S)
#plt.plot(dates, R)
plt.plot(dates, daily_cases)
plt.show()