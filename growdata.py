import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.ticker as tck
from matplotlib.ticker import AutoMinorLocator

data = pd.read_json("C:/Users/aleks/1a/FUNGUJETO_O/example data/result1.json")
#data.to_csv ("C:/Users/aleks/1a/FUNGUJETO_O/example data/result.csv", index = None)


date = data['date']
dtype= data['type']

x=np.linspace(0,23, 24)*np.pi/12
mon=[]
tue=[]
wed=[]
thu=[]
fri=[]
sat=[]
sun=[]

monhour=[]
tuehour=[]
wedhour=[]
thuhour=[]
frihour=[]
sathour=[]
sunhour=[]


for i in range(len(data)-1):
    if dtype[i]=='message': 
        if date[i].weekday()==0:
            mon.append(date[i])
        if date[i].weekday()==1:
            tue.append(date[i])
        if date[i].weekday()==2:
            wed.append(date[i])
        if date[i].weekday()==3:
            thu.append(date[i])
        if date[i].weekday()==4:
            fri.append(date[i])
        if date[i].weekday()==5:
            sat.append(date[i])
        if date[i].weekday()==6:
            sun.append(date[i])

k=0
for i in [mon,tue, wed,thu, fri,sat,sun]:
    for k in range(len(i)):
        i[k]=i[k].hour


# for s in [mon,tue, wed,thu, fri,sat,sun]:
#     for i in [monhour,tuehour,wedhour,thuhour,frihour,sunhour]:
#         for k in range(24):
#             i.append(s.count(k))
            
for k in range(24):
    monhour.append(mon.count(k))
for k in range(24):
    wedhour.append(wed.count(k))
for k in range(24):
    tuehour.append(tue.count(k))
for k in range(24):
    thuhour.append(thu.count(k))
for k in range(24):
    frihour.append(fri.count(k))
for k in range(24):
    sathour.append(sat.count(k))
for k in range(24):
    sunhour.append(sun.count(k))







FONT = 'Times New Roman' 
fig=plt.figure()
ax=plt.subplot(projection='polar')
plt.xticks(fontname=FONT, fontweight = 'bold', fontsize = 12)
plt.yticks(fontname=FONT, fontweight = 'bold', fontsize = 10)
ax.set_xticklabels(['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00',])
ax.set_yticklabels([50])
ax.set_theta_zero_location("S")

ax.plot(x, monhour,   color='black', label='monday')
ax.plot([0,23*np.pi/12], [monhour[0],monhour[23]],   color='black')

ax.plot(x, tuehour,   color='blue', label='tuesday')
ax.plot([0,23*np.pi/12], [tuehour[0],tuehour[23]],   color='blue')

ax.plot(x, thuhour,   color='red', label='thursday')
ax.plot([0,23*np.pi/12], [thuhour[0],thuhour[23]],   color='red')

ax.plot(x, frihour,   color='green', label='friday')
ax.plot([0,23*np.pi/12], [frihour[0],frihour[23]],   color='green')

ax.plot(x, wedhour,   color='brown', label='wednesday')
ax.plot([0,23*np.pi/12], [wedhour[0],wedhour[23]],   color='brown')

ax.plot(x, sathour,   color='yellow', label='saturday')
ax.plot([0,23*np.pi/12], [sathour[0],sathour[23]],  color='yellow')

ax.plot(x, sunhour,   color='pink', label='sunday')
ax.plot([0,23*np.pi/12], [sunhour[0],sunhour[23]],  color='pink')

ax.legend(loc = 'best', shadow = True)
#plot_param()
plt.tight_layout()