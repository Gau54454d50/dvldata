import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

class Time :
    def __init__(self,seconds,minutes,hours) :
        self.seconds = float(seconds)
        self.minutes = int(minutes)
        self.hours = int(hours)
    def findtime(self):
        return float(self.hours*60*60+self.minutes*60)+self.seconds
northing = 496061.20
easting = 2458748.38
df = pd.read_csv('2023-01-16 12-18-52 vehicle1.csv')
df1 = pd.read_csv('Dwarka.csv')
nan = []
print("TOF = ",type(df1["ts"][len(df1["ts"])-2]),type(pd.np.nan))
for r in range(0,len(df1["ts"])-1,14):
    print(np.isnan(df1["ts"][r]))
    if isnan(df1["ts"][r]):
        nan.append(r)
print(len(nan))
x=[]
y=[]
i=0
diff=[]
t=[]

for time in df["Timestamp"]:
    time = time.split(" ")
    time = time[1].split(":")
    t.append(Time(time[2],time[1],time[0]))
    #print(time[2],"type of =",type(time))
t.index(t[0])
for time in t:
    if t.index(time) == 0:
        print("starting ...")
    elif t.index(time) == len(t)-1:
        print("stopping ...")
    else :
        diff.append(time.findtime()-t[t.index(time)-1].findtime())

print(len(diff))
'''
for (vx,vy,dt) in (df["vx"],df["vy"],df["time"]) :
    X = vx * dt + x[i]
    x.append(X)
    Y = vy * dt + y[i]
    y.append(Y)
    x.index(X)
    s = 0
#df.plot(figsize=(15, 10))
#plt.show()
'''