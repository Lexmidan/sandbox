import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.ticker import AutoMinorLocator



dataset=pd.read_csv("C:/Users/aleks/1a/Prak/11/11.txt",
                    sep='	', decimal='.', header=None)
dataset2=pd.read_csv("C:/Users/aleks/1a/Prak/11/111.txt",
                    sep='	', decimal=',', header=None)

dataset[1]*=1000
def fce(x,a,b):
    y=a*x+b

    return y

yaxes=dataset[1][:];xaxes=dataset[0][:] #-dataset[1][:].iloc[-1] protože sinusovka mi nekmítá kolem 0
y2axes=dataset2[1][:];x2axes=dataset2[0][:]

par, cov = curve_fit(fce, xaxes, yaxes, maxfev = 1000,)
par2, cov2 = curve_fit(fce, x2axes, y2axes, maxfev = 1000)



xaxes=np.linspace(dataset.iloc[0][0],dataset.iloc[-1][0],1000)

x2axes=np.linspace(dataset.iloc[0][0],dataset.iloc[-1][0],1000)

standev=np.sqrt(np.diag(cov))
standev2=np.sqrt(np.diag(cov2))


def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('Energie [eV]', fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlabel('Frekvence záření $10^{14}$[Hz]',  fontname = FONT, fontweight = 'bold', fontsize = 18)   #!!!!!
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


fit=ax.plot(xaxes,fce(xaxes,*par),'r-', linewidth=1)
fit2=ax.plot(x2axes,fce(x2axes,*par2),'g-', linewidth=1)


dataline=ax.scatter(dataset[0], dataset[1][:], label='Větší otvor', s=7, color='black') 
dataline2=ax.scatter(dataset2[0], dataset2[1][:], label='Menší otvor', s=7, color='blue') 

ax.hlines(0, 0,10000, color='black')

ax.legend()
plot_param()      #Danielin zlepšující skript
plt.tight_layout()
    #chyba




for i in range(len(par)):
    print(i+1,'. Parameter =', par[i], '\t with err ', standev[i])
    
    
for i in range(len(par2)):
    print(i+1,'. 2Parameter =', par2[i], '\t with err ', standev2[i])
#paramsprint=('par1={},\npar2={},\npar3={},\npar4={} ').format(round(par[0],2), round(par[1],2), round(par[2],2),round(par[3],2) )

#print ('chyba par1:', standev[0],'\nchyba par2:',standev[1],'\nchyba par2:',standev[2], '\nchyba par2:',standev[3])

