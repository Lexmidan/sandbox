#zpracovani ulohy z praktik. Mam spektrum zareni cesia-137, hledam fotopik a fituju gausem


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.ticker import AutoMinorLocator


dataset=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/cs.txt",
                    sep=':', decimal=',', header=None)


pozadi=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/pozadi.txt",
                    sep=':', decimal=',', header=None)

#leva a prava pata fotopiku
startofpik=170
endofpik=230


dataset[1][:]-=pozadi[1][:] #odecitam pozadi
datafordraw=pd.DataFrame.copy(dataset) #kopiruji aby mi zustal cely graf a dal protoze dal pracuji jenom s jeho castkou
dataset1=pd.DataFrame.copy(dataset)[startofpik:endofpik]    #nechavam pouze fotopiky
dataset1[0]-=startofpik     #chci aby i ten usek zacinal od nuly


def fce(x,a,sigma,x0,d):
    y = a*np.exp(-(x-x0)**2/(2*sigma**2))+d
    return y

yaxes=dataset1[1][:];xaxes=dataset1[0][:]
par, cov = curve_fit(fce, xaxes, yaxes, maxfev = 1000) #!!!
xaxes=np.linspace(dataset1.iloc[0][0],dataset1.iloc[-1][0],1000) #aby fitovaci krivka vypadala lip


standev=np.sqrt(np.diag(cov))

def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('Counts', fontname = FONT, fontweight = 'bold', fontsize = 18)
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
label='$'+str(round(par[0],2))+ 'e^{'+str(round(par[1],2))+'s(x'+str(round(par[2],2))+')^2}'+str(round(par[3],2))+'$'

fig, ax=plt.subplots()

fit=ax.plot(xaxes+startofpik,fce(xaxes,*par),color='red', linewidth=2, label=label)



ax.legend()
plot_param()      #Danielin zlepšující skript
plt.tight_layout()


dataline=ax.plot(datafordraw[0], datafordraw[1][:],   color='black', alpha=0.6)

print("Pro první pik")
for i in range(len(par)):
    print(i+1,'. Parameter =', round(par[i], 4), '\t with err ', round(standev[i], 4))

