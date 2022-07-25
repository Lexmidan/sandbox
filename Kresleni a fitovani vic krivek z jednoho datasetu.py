#zpracovani ulohy z praktik. Mam krivku, potrebuju ji fitovat nekolika krivkami v zavislosti na oblasti jiz fituju


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from matplotlib.ticker import AutoMinorLocator
from random import randint
from inspect import signature


dataset=pd.read_csv("C:/Users/aleks/1a/FUNGUJETO_O/example data/FH.txt",
                    sep='	', decimal=',', header=None)

dataset[0]/=100 #tak cislo bodu odpovida napeti 
#!!!!! #vzdycky zadej start a end
startends=np.array([[6,17],[16,25],[24,35],[33,43],[50,60],[65,76],[81,90],[42,51],[59,66],[75,82],[89,98],[97,105]]) #zadej indexy piku ve tvare [pocatek,konec],[pocatek,konec]

def fce(x,a,b,c):
    y = a*x**2+b*x+c
    return y

def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('$U_\mathrm{A}\;\; [\mathrm{V}]$', fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlabel('$U_2\;\; [\mathrm{V}]$',  fontname = FONT, fontweight = 'bold', fontsize = 18)
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

def plus(num): #da znamenko plus pred kladnou a minus pred zapornou. je potreba jen na legendu
    if num>=0:
        s='$+$'+str(num)
        return(s)
    else:
        return('$-$'+str(abs(num)))

xerr=[]
for i in range(len(dataset[0][:])):
    if dataset.iloc[i][0]<=2:
        xerr.append(0.001)
    else:
        xerr.append(0.01)

parames=np.zeros((len(startends)+1,(len(signature(fce).parameters)-1)*2,)) #tabulka kam zapisu vsechny parametry a chyby
i=0
while i < len(parames[0]):
    parames[0][i]=i/2
    parames[0][i+1]=i/2
    i+=2 

def jojojo(dataset,startends):

    itera=len(startends)
    colors = []  #vytvarim array barev jež budou mít budoucí fit křivky
    for s in range(itera):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    r=0 #je potřeba jenom pro vybírání barvy ve fit=ax.plot a vytvoreni tabulky parames
    plt.errorbar(dataset[0][:],dataset[1][:], xerr=xerr, yerr=0.001,  fmt='+', color='black',
              ecolor='cornflowerblue', linewidth=1.5, capsize=3, capthick=1.5, )
    for i in startends:
        dataset1=pd.DataFrame.copy(dataset)[i[0]:i[1]]    #nechavam pouze fotopiky   
        yaxes=dataset1[1][:];xaxes=dataset1[0][:]
        par, cov = curve_fit(fce, xaxes, yaxes, maxfev = 1000) #!!!
        xaxes=np.linspace(dataset1.iloc[0][0],dataset1.iloc[-1][0],1000) #aby fitovaci krivka vypadala lip
        standev=np.sqrt(np.diag(cov))
        
        #vytvarim automaticke popisky
        
        label=str(round(par[0],  -int(np.log10(standev[0]))+1))+'$x^2$'+plus(round(par[1],  -int(np.log10(standev[1]))+1))+'$x$'+plus(round(par[2],  -int(np.log10(standev[2]))+1))
        ax.plot(xaxes,fce(xaxes,*par),color=colors[r], linewidth=2, label=label)
        
        for k in range((len(signature(fce).parameters)-1)): #tabulka kam zapisu vsechny parametry a chyby
            parames[r+1][2*k:2*k+2]=[par[k],standev[k]]    
        print("Pro ", r+1, ". pik")
        for k in range(len(par)):
            print(k+1,'. Parameter =', round(par[k], -int(np.log10(standev[k]))), '\t with err ', '{:g}'.format(float('{:.1g}'.format(standev[k]))))
        r+=1
fig, ax=plt.subplots()
jojojo(dataset,startends)
ax.legend()
plot_param()      #Danielin zlepšující skript
plt.tight_layout()
print('all parameters and covariances are in parames in format- par1 cov1 par2 cov2....\n')

