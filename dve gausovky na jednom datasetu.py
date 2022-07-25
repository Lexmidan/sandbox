#zpracovani ulohy z praktik. Mam spektrum zareni Ba-133, hledam fotopiky a fituju gausem



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.ticker import AutoMinorLocator


dataset=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/co.txt",
                    sep=':', decimal=',', header=None)


pozadi=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/pozadi.txt",
                    sep=':', decimal=',', header=None)

#leva a prava pata fotopiku
startofpik=319
endofpik=363


startofpik2=363
endofpik2=400

#odecitam pozadi

dataset[1][:]-=pozadi[1][:]

#kopiruji aby mi zustal cely graf a dal protoze dal pracuji jenom s jeho castkou
datafordraw=pd.DataFrame.copy(dataset)
    
#nechavam pouze fotopiky

dataset1=pd.DataFrame.copy(dataset)[startofpik:endofpik]

dataset2=pd.DataFrame.copy(dataset)[startofpik2:endofpik2]


dataset1[0]-=startofpik
dataset2[0]-=startofpik2

def fce(x,a,sigma,x0,d):
    y = a*np.exp(-(x-x0)**2/(2*sigma**2))+d

    return y

yaxes=dataset1[1][:];xaxes=dataset1[0][:]
yaxes2=dataset2[1][:];xaxes2=dataset2[0][:]


par, cov = curve_fit(fce, xaxes, yaxes, maxfev = 1000) #!!!
par2, cov2 = curve_fit(fce, xaxes2, yaxes2, maxfev = 1000) #!!!





standev=np.sqrt(np.diag(cov))
standev2=np.sqrt(np.diag(cov2))

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


label='$'+str(round(par[0],2))+ 'e^{'+str(round(par[1],2))+'s(x'+str(round(par[2],2))+')^2}'+str(round(par[3],2))+'$'
label2='$'+str(round(par2[0],2))+ 'e^{'+str(round(par2[1],2))+'s(x'+str(round(par2[2],2))+')^2}'+str(round(par2[3],2))+'$'


fig, ax=plt.subplots()

fit=ax.plot(xaxes+startofpik,fce(xaxes,*par),color='red', linewidth=2, label=label)
fit2=ax.plot(xaxes2+startofpik2,fce(xaxes2,*par2),color='blue', linewidth=2, label=label2)



ax.legend()
plot_param()      #Danielin zlepšující skript
plt.tight_layout()


dataline=ax.plot(datafordraw[0], datafordraw[1][:],   color='black', alpha=0.6)

print("Pro první pik")
for i in range(len(par)):
    print(i+1,'. Parameter =', round(par[i], 4), '\t with err ', round(standev[i], 4))

print('Pro druhý pik')
for i in range(len(par2)):
    print(i+1,'. Parameter =', round(par2[i], 4), '\t with err ', round(standev2[i], 4))
   
