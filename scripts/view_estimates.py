import numpy as np
import matplotlib.pyplot as plt

fig,axs = plt.subplots(2,1,figsize=(6.5,5))

###########################################################
ax = axs[0]
dat = np.loadtxt('ml_estimates.txt',skiprows=1)
periods = dat[:,0]
idx = np.argsort(periods)
periods = periods[idx]
means = dat[idx,1]
percs = dat[idx,2:]
p10 = percs[:,2]
p25 = percs[:,5]
medians = percs[:,10]
p75 = percs[:,15]
p90 = percs[:,18]

ax.plot(periods,means,'b--',zorder=.3,label='mean')
ax.plot(periods,medians,'b-',zorder=.3,label='median')
ax.plot([periods[0],periods[-1]],[1.3,1.3],'k-',zorder=.4,label='true value')
ax.fill_between(periods,p10,p90,color=(0.8,0.8,1.0),zorder=.1,label='10$\mathregular{^{th}}$-90$\mathregular{^{th}}$ percentile')
ax.fill_between(periods,p25,p75,color=(0.6,0.6,1.0),zorder=.2,label='25$\mathregular{^{th}}$-75$\mathregular{^{th}}$ percentile')

ax.set_xlabel('time series length [years]',fontsize=10)
ax.set_ylabel('$\mathrm{\sigma_{rw}}$ [mm/yr$\mathregular{^{0.5}}$]',fontsize=10)

ax.set_xlim((periods[0],periods[-1]))
ax.set_ylim((0.0,3.5))
ax.set_title('Maximum likelihood estimation (MLE)',fontsize=10)
ax.set_xticks([0.3,0.5,1.0,1.5,2.0,2.5])
ax.set_xticklabels(['$\mathregular{f_c^{-1}}$','0.5','1.0','1.5','2.0','2.5'])
ax.grid(c='0.5',alpha=0.5)
ax.legend(ncol=2)
###########################################################

###########################################################
ax = axs[1]

dat = np.loadtxt('reml_estimates.txt',skiprows=1)
periods = dat[:,0]
idx = np.argsort(periods)
periods = periods[idx]
means = dat[idx,1]
percs = dat[idx,2:]
p10 = percs[:,2]
p25 = percs[:,5]
medians = percs[:,10]
p75 = percs[:,15]
p90 = percs[:,18]

#for i,period in enumerate(periods):
ax.plot(periods,means,'b--',zorder=.3,label='mean')
ax.plot(periods,medians,'b-',zorder=.3,label='median')
ax.plot([periods[0],periods[-1]],[1.3,1.3],'k-',zorder=.4,label='true value')
ax.fill_between(periods,p10,p90,color=(0.8,0.8,1.0),zorder=.1,label='10$\mathregular{^{th}}$-90$\mathregular{^{th}}$ percentile')
ax.fill_between(periods,p25,p75,color=(0.6,0.6,1.0),zorder=.2,label='25$\mathregular{^{th}}$-75$\mathregular{^{th}}$ percentile')

ax.set_xlabel('time series length [years]',fontsize=10)
ax.set_ylabel('$\mathrm{\sigma_{rw}}$ [mm/yr$\mathregular{^{0.5}}$]',fontsize=10)

ax.plot([periods[0],periods[-1]],[1.3,1.3],'k-',zorder=4)
ax.set_xlim((periods[0],periods[-1]))
ax.set_ylim((0.0,3.5))
ax.set_title('Restricted maximum likelihood (REML) estimation',fontsize=10)
ax.set_xticks([0.3,0.5,1.0,1.5,2.0,2.5])
ax.set_xticklabels(['$\mathregular{f_c^{-1}}$','0.5','1.0','1.5','2.0','2.5'])
ax.grid(c='0.5',alpha=0.5)
###########################################################

plt.tight_layout()
plt.show()

