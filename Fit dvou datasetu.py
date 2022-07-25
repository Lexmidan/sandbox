import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.ticker import AutoMinorLocator


dataset=pd.read_csv('C:/Users/aleks/1a/JUPITER/PRAKTIKUM ZPRACOVANI DAT/Uloha11/bezjadra.txt',
                    sep="	", decimal=',', header=None)
dataset2=pd.read_csv('C:/Users/aleks/1a/JUPITER/PRAKTIKUM ZPRACOVANI DAT/Uloha11/sjadrem.txt',
                    sep="	", decimal=',', header=None)
dataset[1]/=5
dataset2[1]/=5



def fce(x,I,Q, f0):
    y=I/(np.sqrt(1+Q*(x/f0-f0/x)**2))

    return y

yaxes=dataset[1][:];xaxes=dataset[0][:] #-dataset[1][:].iloc[-1] protože sinusovka mi nekmítá kolem 0
y2axes=dataset2[1][:];x2axes=dataset2[0][:]

par, cov = curve_fit(fce, xaxes, yaxes, maxfev = 10000, bounds=([-np.inf, -np.inf, 200],
                                                                [np.inf,np.inf,230]))
par2, cov2 = curve_fit(fce, x2axes, y2axes, maxfev = 10000, bounds=([-np.inf, -np.inf, 200],
                                                                    [np.inf,np.inf,350]))


xaxes=np.linspace(0,1000,1000)
x2axes=np.linspace(0,1000, 1000) 

standev=np.sqrt(np.diag(cov))
standev2=np.sqrt(np.diag(cov2))


def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('Proud I $[mA]$', fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlabel('Frekvence $\omega \;[rad/s]$',  fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlim(100,400)   #!!!!!
    #graphic parameters
    plt.xticks(fontname=FONT, fontweight = 'bold', fontsize = 15)
    plt.yticks(fontname=FONT, fontweight = 'bold', fontsize = 15)
    
    ax.tick_params(which = 'major', direction='out', length=6, width=1.5)
    ax.tick_params(which = 'minor', direction='out', length=3, width=1)
    
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(1.5)
        
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    
    ax.grid(which = 'major', c = 'gray', linewidth = 0.5, linestyle = 'solid') 
    ax.grid(which = 'minor', c = 'gray', linewidth = 0.3, linestyle = 'dashed')             
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    leg = plt.legend(  loc = 'best', shadow = True, fancybox=False)
    
    leg.get_frame().set_linewidth(1)
    leg.get_frame().set_edgecolor('k')
    
    for text in leg.get_texts():
          plt.setp(text, fontname=FONT, fontsize = 14)






fig, ax=plt.subplots()

legend='$y_1$='
legend2='$y_2=\frac{I}{\sqrt{1+Q^2(\frac{f_0}{f}-\frac{f}{f_0})^2}}$'

ax.plot(xaxes[1],fce(xaxes[1],*par),'r-',linewidth=1)
ax.plot(x2axes[1],fce(x2axes[1],*par2),'g-'
        ,linewidth=1) #Kresli jen jeden bod. Potřeben jenom ke kreslení legendy

fit=ax.plot(xaxes,fce(xaxes,*par),'r-', linewidth=1)
fit2=ax.plot(x2axes,fce(x2axes,*par2),'g-', linewidth=1)


dataline=ax.scatter(dataset[0], dataset[1][:], label='Cívka bez jádra', s=7, color='black') 
dataline2=ax.scatter(dataset2[0], dataset2[1][:], label='Cívka s jádrem', s=7, color='blue') 


ax.legend()
plot_param()      #Danielin zlepšující skript
plt.tight_layout()
    #chyba




for i in range(len(par)):
    print(i+1,'. Parameter =', round(par[i], 2), '\t with err ', round(standev[i], 2))
    
    
for i in range(len(par2)):
    print(i+1,'. 2Parameter =', round(par2[i], 2), '\t with err ', round(standev2[i], 2))
#paramsprint=('par1={},\npar2={},\npar3={},\npar4={} ').format(round(par[0],2), round(par[1],2), round(par[2],2),round(par[3],2) )

#print ('chyba par1:', standev[0],'\nchyba par2:',standev[1],'\nchyba par2:',standev[2], '\nchyba par2:',standev[3])

