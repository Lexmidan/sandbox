import matplotlib.pyplot as plt
import scipy.integrate
import pandas as pd
from matplotlib.ticker import AutoMinorLocator

for s in range(10):
    path=f'C:/Users/aleks/OneDrive/Plocha/Skripta/GNU/uloha 1/V3/V3_{s+1}.txt'
    dataset=pd.read_csv(path, sep="	", header=None, decimal=',')
    
    #vynolování
    for i in range(len(dataset[0])):
        if dataset[1][i]<0:
            dataset[1][i]=0
    
    def interact_t(data):
        for j in range(len(data[0])):
            if data[1][j]>0:
                br=j
                break
        for s in range(len(data[0])):
            if data[1][br+s]>=data[1][br+s+1]:
                stred=br+s
                break
        for k in range(len(data[0])):
            if data[1][br+k]==0:
                br2=br+k
                break
        pred=scipy.integrate.simps(dataset[1][br:stred], dataset[0][br:stred], even='avg')
        po=scipy.integrate.simps(dataset[1][stred:br2], dataset[0][stred:br2], even='avg')
        print('I1=', pred, '\n I2=', po, '\n R=', pred/po)
        return(br2-br)
    
    suma=scipy.integrate.simps(dataset[1], dataset[0], even='avg')
    
    print(f'\n{s+1} integral =',suma, '[kgm/s]')
    #print('Interaction time = ',interact_t(dataset)*(dataset[0][1]-dataset[0][0]),' [s]')
    print(f'\n{s+1}<I>=', suma/((dataset[0][1]-dataset[0][0])*interact_t(dataset)))


def plot_param():       #чудо чудное
    FONT = 'Times New Roman'   
    plt.ylabel('Amplituda [-]', fontname = FONT, fontweight = 'bold', fontsize = 18)
    plt.xlabel('Natětí [V]',  fontname = FONT, fontweight = 'bold', fontsize = 18)
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
    
    ax.grid(which = 'major', c = 'gray', linewidth = 0.5, linestyle = 'solid') 
    ax.grid(which = 'minor', c = 'gray', linewidth = 0.3, linestyle = 'dashed')             
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    leg = plt.legend(  loc = 'best', shadow = True, fancybox=False)
    
    leg.get_frame().set_linewidth(1)
    leg.get_frame().set_edgecolor('k')
    
    for text in leg.get_texts():
          plt.setp(text, fontname=FONT, fontsize = 14)


# # def integral(data):
# #     step=data[0][1]-data[0][0]
# #     s=0
# #     for i in range(len(data[0])):
# #        s+=data[1][i]
# #     return(s*step)



fig, ax=plt.subplots()


dataline=ax.plot(dataset[0], dataset[1][:],   color='black')
plot_param()
plt.tight_layout()


