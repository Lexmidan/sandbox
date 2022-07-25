import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.ticker import AutoMinorLocator



dataset=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/malus.csv",
                    sep=';', decimal=',', header=None)
    



def fce(x,a,b,d):
    y=a*np.cos(d*x)**2+b
    return y


yaxes=dataset[2][:];xaxes=dataset[0][:]



par, cov = curve_fit(fce, xaxes, yaxes, maxfev = 1000, bounds=([-np.inf, -np.inf,0.007],
                                                                [np.inf,   np.inf,0.009])) #!!!


xaxes=np.linspace(dataset.iloc[0][0],dataset.iloc[-1][0],1000)



standev=np.sqrt(np.diag(cov))


def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('Intenzita', fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlabel('Úhel otočení analyzátoru',  fontname = FONT, fontweight = 'bold', fontsize = 18)
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



fit=ax.plot(xaxes,fce(xaxes,*par),color='royalblue', linewidth=2, label='$y=293,8\cos^2(0,007x)-188,9$')


plt.errorbar(dataset[0][:],yaxes, xerr=dataset[1][:], yerr=dataset[3][:],  fmt='.k', color='blue',
              ecolor='cornflowerblue', linewidth=1.5, capsize=3, capthick=1.5)


ax.legend()
plot_param()      #Danielin zlepšující skript
plt.tight_layout()
    #chyba




for i in range(len(par)):
    print(i+1,'. Parameter =', round(par[i], 4), '\t with err ', round(standev[i], 4))
    