import csv
import re
field = ['time','vx','vy','vz']
string = []
time = []
vx = []
vy = []
vz = []
with open("Dwarka_16_DVL .json","r") as fp:
  string.append(fp.read())
string = string[0]
print(string[1123])
r=string.split(",")
for reg in r:
  if '{"time":' in reg :
    time.append(reg.split('{"time":')[1])
  if '"vx":' in reg :
    vx.append(reg.split('"vx":')[1])
  if '"vy"' in reg :
    vy.append(reg.split('"vy":')[1])
  if '"vz"' in reg :
    vz.append(reg.split('"vz":')[1])
time = [float(t) for t in time]
vx = [float(t) for t in vx]
vy = [float(t) for t in vy]
vz = [float(t) for t in vz]
print(len(time),len(vx),len(vy),len(vz))
data = zip(time,vx,vy,vz)
data=list(data)
print(data[0])
with open("Dwarka_16_DVL.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(field)
    writer.writerows(data)
