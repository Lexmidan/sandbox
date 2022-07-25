#zpracovani ulohy z praktik. Mam spektrum zareni cesia-137, hledam fotopik a fituju gausem


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.ticker import AutoMinorLocator

#format dat: skut hodnota;namerena hodnota;chyba skut;chyba namer
dataset=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/kalibracni.csv",
                    sep=';', decimal=',', header=None)




def fce(x,a,b):
    y = a*x+b
    return y

yaxes=dataset[1][:];xaxes=dataset[0][:]
par, cov = curve_fit(fce, xaxes, yaxes, maxfev = 1000) #!!!
xaxes=np.linspace(dataset.iloc[0][0],dataset.iloc[-1][0],100) #aby fitovaci krivka vypadala lip


standev=np.sqrt(np.diag(cov))

def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('Energie [keV]', fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlabel('Kanál',  fontname = FONT, fontweight = 'bold', fontsize = 18)
    # plt.xlim(0.,0.5)   #!!!!!
    # plt.ylim(0.,0.5)
    #graphic parameters
    plt.xticks(fontname=FONT, fontweight = 'bold', fontsize = 15)
    plt.yticks(fontname=FONT, fontweight = 'bold', fontsize = 15)
    
    ax.tick_params(which = 'major', direction='out', length=6, width=1.5)
    ax.tick_params(which = 'minor', direction='out', length=3, width=1)
    
    for axis in ['bottom','left']:
        ax.spines[axis].set_linewidth(1.5)
        
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    
    #ax.grid(which = 'major', c = 'gray', linewidth = 0.5, linestyle = 'solid') 
    #ax.grid(which = 'minor', c = 'gray', linewidth = 0.3, linestyle = 'dashed')             
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    leg = plt.legend(  loc = 'best', shadow = True, fancybox=False)
    
    leg.get_frame().set_linewidth(1)
    leg.get_frame().set_edgecolor('k')
    
    for text in leg.get_texts():
          plt.setp(text, fontname=FONT, fontsize = 14)

#vytvarim automaticke popisky
label='$'+str(round(par[0],2))+'x'+ str(round(par[1],2))+'$'

fig, ax=plt.subplots()

fit=ax.plot(xaxes,fce(xaxes,*par),color='red', linewidth=2, label='$y=(0,285\pm0,003)x+7\pm2$')

plt.errorbar(dataset[0][:],dataset[1][:], xerr=dataset[3][:],yerr=dataset[2][:],  fmt='.k', color='blue',
             ecolor='cornflowerblue', linewidth=1.5, capsize=0, capthick=0)

ax.legend()
plot_param()      #Danielin zlepšující skript
plt.tight_layout()


dataline=ax.scatter(dataset[0], dataset[1][:],   color='black', alpha=0.6, s=10, )

print("Pro první pik")
for i in range(len(par)):
    print(i+1,'. Parameter =', round(par[i], 4), '\t with err ', round(standev[i], 4))

