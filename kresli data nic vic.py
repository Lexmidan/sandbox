import matplotlib.pyplot as plt

import pandas as pd
from matplotlib.ticker import AutoMinorLocator


dataset=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/co.txt",
                    sep=':', decimal=',', header=None)
       
    
    
    
def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('$\omega$ [rad/s]', fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlabel('$t$ [s]',  fontname = FONT, fontweight = 'bold', fontsize = 18)
    # plt.xlim(0,0.6)
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

fig, ax=plt.subplots()


dataline=ax.plot(dataset[0], dataset[1][:],   color='black')

plot_param()
plt.tight_layout()