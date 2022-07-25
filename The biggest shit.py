import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # for reading csv files
from scipy import integrate, constants as ct
from scipy.signal import lfilter
from matplotlib.ticker import AutoMinorLocator
FONT = 'Times New Roman'


r = 13 # the larger n is, the smoother curve will be
b = [1.0 / r] * r
a = 1
def load_rigol(name, shot, group='c'):
    rigol_name='RigolMSO5204-d'
    url = f'http://golem.fjfi.cvut.cz/shotdir/{shot}/Devices/Oscilloscopes/{rigol_name}/{name}.csv' 
    print(url)
    df = pd.read_csv(url, names=['time', name], index_col='time')
    t = np.array(df.index)
    data = np.transpose(np.array(df))[0]
    data=np.delete(data,-1)
    t=np.delete(t,-1)
    # return t, data 
    return df.iloc[:-1]

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

fig, [ax1, ax2, ax3, ax4] = plt.subplots(4, 1, sharex=True) #!!!!!
fig2, ax=plt.subplots()
#765-769 Ucd=400 Ubt 800-1200, 771-777 Ucd=500 Ubt =800-1200
shots=[38765]#,38766,38767,38768,38769,38771,38772,38773,38775,38777]

taudev=pd.DataFrame({'tau':[],'tau_std':[]})
Btdev=pd.DataFrame({'Bt':[],'Bt_std':[]})

for SHOT in shots:
#creating data
    names=['U_Loop', 'U_RogCoil', 'U_photod', 'U_BtCoil']
    data = pd.concat([load_rigol(name,  SHOT) for name in names], axis = 1 )    
    for n in names: #clearing offset
        data[n]-=data[n].loc[:1.62e-3].values.mean()
        data[n]
        data[n] = lfilter(b,a,data[n].values)
    

        
    #Constants
    Rch=0.0097 #ohm
    Vch=150/1000 #m
    Vp=57/1000 #m
    T0=300 #kelvin
    kB=1.38*10**(-23)#Boltzman
    p0=float(pd.read_csv(f'https://golem.fjfi.cvut.cz/shots/{SHOT}/Diagnostics/BasicDiagnostics/Parameters/pressure'\
                   , names=['pres'])['pres'])/1000 #Pa
    ne=2*p0*Vch/(kB*T0*Vp)
    KBt_golem=70.42
    
    Ich_golem=pd.read_csv(f'https://golem.fjfi.cvut.cz/shots/{SHOT}/Diagnostics/BasicDiagnostics/Results/Ich.csv',
                    names=['time', 'I_golem'], index_col='time') #Chamber current
    Ip_golem=pd.read_csv(f'https://golem.fjfi.cvut.cz/shots/{SHOT}/Diagnostics/BasicDiagnostics/Results/Ip.csv'\
                    , names=['time', 'I_golem'], index_col='time') #Plasma current
    Ipch_golem=(Ip_golem+Ich_golem)*1000     #Ipch ^ (kA->A)
    Bt_golem=pd.read_csv(f'https://golem.fjfi.cvut.cz/shots/{SHOT}/Diagnostics/BasicDiagnostics/Results/Bt.csv'\
                    , names=['time', 'Bt'], index_col='time') #Bt
    U_Loop_golem=pd.read_csv(f'https://golem.fjfi.cvut.cz/shots/{SHOT}/Diagnostics/BasicDiagnostics/Results/U_loop.csv'\
                    , names=['time', 'U_Loop'], index_col='time')
    U_photod_golem=pd.read_csv(f'https://golem.fjfi.cvut.cz/shots/{SHOT}/Diagnostics/BasicDiagnostics/U_LeybPhot.csv'\
                    , names=['time', 'U_photod'], index_col='time')



    
    data.index-=data.index[data['U_Loop']==data['U_Loop'].max()]-U_Loop_golem.idxmax().values/1000
    
    data['Ich']=data['U_Loop']/Rch
    data['Ipch'] = integrate.cumtrapz(data['U_RogCoil'], data.index, initial=0)
    data['Ipch']*=-1
    data['Bt'] = integrate.cumtrapz(data['U_BtCoil'], data.index, initial=0)
    
    
    Bt_gol_middle= float(Bt_golem.iloc[int(len(Bt_golem.values) / 2)].values)
    Bt_middle=data.iloc[int(len(data['Ich'])/2)]['Bt']
    KBt=float(Bt_golem.loc[10.0142358]/data.loc[0.0100142358]['Bt']) #jen pro 1. shot

   # KBt=float(Bt_gol_middle/Bt_middle) univerzalně ale nefunguje dobře
    
    data['Bt']*=KBt
    Crc=(Ipch_golem.max())/data['Ipch'].max() ##!!!!!!
    data['Ipch']=(data['Ipch']*int(Crc))
    data['Ip']=data['Ipch']-data['Ich']
    data['Te']=(0.9*(data['Ip'].values/data['U_Loop'].values)**(2))**(1/3)
    data['Wp']=1/3*ct.e*ne*data['Te'].values*Vp
    data['tau']=ct.e*ne*data['Te'].values*Vp/(3*data['U_Loop'].values*data['Ip'].values)
    
    Ip_golem.index/=1000
    Ip_golem*=1000
    U_Loop_golem.index/=1000
    Ich_golem.index/=1000
    Ipch_golem.index/=1000
    Bt_golem.index/=1000
    
    ax1.plot(Ip_golem,  lw=2, label='GOLEM standart diagnostic')
    ax1.set_ylabel('$I_p$ [A]',  fontname = FONT, fontweight = 'bold', fontsize = 16)
    ax2.plot(Bt_golem,  lw=2)
    ax2.set_ylabel('$B_t$ [T]',  fontname = FONT, fontweight = 'bold', fontsize = 16)
    ax3.plot(U_Loop_golem,  lw=2)
    ax3.set_ylabel('$U_{loop}$ [V]',  fontname = FONT, fontweight = 'bold', fontsize = 16)
    ax4.plot(U_photod_golem, lw=2)
    ax4.set_xlabel('$t$ [s]',  fontname = FONT, fontweight = 'bold', fontsize = 18)
    ax4.set_ylabel('$U_{ph}$ [V]',  fontname = FONT, fontweight = 'bold', fontsize = 16)
    

    
    

    ax1.plot(data['Ip'],  lw=2, label='Processed oscilloscope data')
    ax1.grid(True)
    ax2.plot(data['Bt'],  lw=2)
    ax2.grid(True)
    ax3.plot(data['U_Loop'],  lw=2)
    ax3.grid(True)
    ax4.plot(data['U_photod'],  lw=2)
    ax4.grid(True)
    plt.xlabel('$time$ [$\mu s$]',  fontname = FONT, fontweight = 'bold', fontsize = 18)
    
    ax1.legend(prop={'size': 10},bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=3)
    
    
    
    
    
    Ipmaxindex=data.index.get_loc(float(data.index[data['Ip']==data['Ip'].max()].values))-100
    qst=range(Ipmaxindex-5, Ipmaxindex+5)
    data_st=data.iloc[qst] #during quazistationary phase
    
    
    Bt=data_st['Bt'].mean()
    Bt_std=np.std(data_st['Bt'])
    Ul=data_st['U_Loop'].mean()
    Ul_std=np.std(data_st['U_Loop'])
    Ip=data_st['Ip'].mean()
    Ip_std=np.std(data_st['Ip'])
    Te=0.9*(Ip/Ul)**(2/3)
    Te_std=9/10*np.sqrt((1/Ul)**2*Ip_std**2+(Ip/Ul**2)*Ul_std**2)
    ne=2*p0*Vch/(kB*Te*Vp)
    ne_std=2*p0*Vch*5e-3/(kB*T0*Vp**2)
    tau=ct.e*ne*Te*Vp/(Ul*Ip*3)
    tau_std=1/3*ct.e*np.sqrt((Te*Vp/(Ul*Ip))**2*ne_std**2+(ne*Vp/(Ul*Ip))**2*Te_std**2\
                             +(ne*Vp/(Ul**2*Ip))**2*Ul_std**2+(ne*Vp/(Ul*Ip**2))**2*Ip_std**2)
    #hy=hy.append(pd.DataFrame({'Te':[Te],'chyba Te':[Te_std],'Ul':[Ul],'chyba Ul':[Ul_std], 'Ip':[Ip],'chyba Ip':[Ip_std],'ne':[ne],'chyba ne':[ne_std]}, index=None))
    taudev=taudev.append(pd.DataFrame({'tau':[tau],'tau_std':[tau_std]}))
    Btdev=Btdev.append(pd.DataFrame({'Bt':[Bt],'Bt_std':[Bt_std]}))
    print('tau = ', tau)


Bttau=pd.concat([Btdev, taudev], axis=1)
Bttau.set_index(pd.Series(shots))
Bttau=Bttau.sort_values('Bt')
ax.errorbar(x=Bttau['Bt'], y=Bttau['tau']*1000000, xerr=Bttau['Bt_std'], yerr=Bttau['tau_std']*1000000,  fmt='.k', color='blue',
              ecolor='cornflowerblue', linewidth=1.5, capsize=3, capthick=1.5 )
FONT = 'Times New Roman'

plt.ylabel('$t$ $[\mu s]$', fontsize = 18)
plt.xlabel('$Bt$ [T]', fontsize = 18)


# plt.plot(discharge['Bt'], discharge['tau']*1000000, marker='o')
# 

# 

for i, txt in enumerate([f'{str(i)}.' for i in shots]):
    ax.annotate(txt, (Bttau['Bt'].iloc[i]+0.005, Bttau['tau'].iloc[i]*1000000))
plt.show()
