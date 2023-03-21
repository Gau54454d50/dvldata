import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)
plt.rcParams['figure.figsize'] = (15, 5)
northing = 496061.20
easting = 2458748.38
df = pd.read_csv('Dwarka_16_DVL.csv')
x=[]
y=[]
i=0

for (vx,vy,dt) in (df["vx"],df["vy"],df["time"]) :
    X = vx * dt + x[i]
    x.append(X)
    Y = vy * dt + y[i]
    y.append(Y)
    x.index(X)
    s = 0
#df.plot(figsize=(15, 10))
#plt.show()