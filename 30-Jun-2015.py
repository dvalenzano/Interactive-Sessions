import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import cPickle
from time import sleep

a = '/Volumes/group_dv/personal/DValenzano/month-by-month/Jun2015/simul/asex/17-Jun/plot_values_run1.txt'
a_out = '/Volumes/group_dv/personal/DValenzano/month-by-month/Jun2015/simul/asex/17-Jun/'

s = '/Volumes/group_dv/personal/DValenzano/month-by-month/Jun2015/simul/sex/17-Jun-2015/plot_values_run1.txt'
s_out = '/Volumes/group_dv/personal/DValenzano/month-by-month/Jun2015/simul/sex/17-Jun/'


class cp():
    def __init__(self, inp):
        self.inp = inp
        self.o = open(self.inp, 'rb')
        self.pop_in = cPickle.load(self.o)
        self.n_stage = len(self.pop_in)-1
        self.res_in = cPickle.load(self.o)
        self.age_distr_in = cPickle.load(self.o)
        #print np.shape(age_distr_in[0])                                                                                                                                                                                         
        self.repr_rate_in = cPickle.load(self.o)
        self.repr_rate_sd_in = cPickle.load(self.o)
        for i in range(len(self.repr_rate_sd_in)):
            self.repr_rate_sd_in[i] = np.array(self.repr_rate_sd_in[i])
            self.repr_rate_sd_in[i].shape = (71,1)
        self.repr_rate_junk_in = cPickle.load(self.o)
        self.surv_rate_in = cPickle.load(self.o)
        self.surv_rate_sd_in = cPickle.load(self.o)
        for i in range(len(self.surv_rate_sd_in)):
            self.surv_rate_sd_in[i] = np.array(self.surv_rate_sd_in[i])
            self.surv_rate_sd_in[i].shape = (71,1)
        self.surv_rate_junk_in = cPickle.load(self.o)
        self.repr_fit_in = cPickle.load(self.o)
        self.repr_fit_junk_in = cPickle.load(self.o)
        self.surv_fit_in = cPickle.load(self.o)
        self.surv_fit_junk_in = cPickle.load(self.o)
        self.fit_in = np.array(self.repr_fit_in)*np.array(self.surv_fit_in)
        self.fit_junk_in = np.array(self.repr_fit_junk_in)*np.array(self.surv_fit_junk_in)
        self.dens_surv_in = cPickle.load(self.o)
        self.dens_repr_in = cPickle.load(self.o)
        self.hetrz_mea = cPickle.load(self.o)
        self.hetrz_mea_sd = cPickle.load(self.o) # when simul version > 0.6                                                                                                                                                                
        self.males_females_ages = cPickle.load(self.o)
        self.o.close()
        
    # actual survival series                                                                                                                                                                                                 
    def compute_actual_surv_rate(self, n):
        self.n = n
        """                                                                                                                                                                                                                  
        Takes age distribution of two consecutive stages and computes the                                                                                                                                                    
        fractions of those survived from age x to age x+1. The cumulative product                                                                                                                                            
        of those values builds the final result.                                                                                                                                                                             
        Returns a numpy array.                                                                                                                                                                                               
        """
        div = self.age_distr_in[self.n]*self.pop_in[self.n]
        div[div == 0] = 1
        stage2 = np.array(list((self.age_distr_in[self.n+1]*self.pop_in[self.n+1]))[1:]+[0])

        res = stage2 / div
        for i in range(1,len(res)):
            res[i] = res[i-1] * res[i]
        return res        

    def avr_actual_surv_rate(self, m):
        """Averages actual survival rate over 100 stages."""
        self.m = m
        if self.m <= 50:
            res = compute_actual_surv_rate(self.m+100)
            for i in range(self.m,self.m+100):
                res += compute_actual_surv_rate(i)
            return res/100
        if self.m >= self.n_stage-50:
            res = compute_actual_surv_rate(self.n_stage-101)
            for i in range(self.n_stage-100,self.n_stage-1):
                res += compute_actual_surv_rate(i)
            return res/100
        else:
            res = compute_actual_surv_rate(self.m+50)
            for i in range(self.m-50,self.m+50):
                res += compute_actual_surv_rate(i)
            return res/100



ca = cp(a)
cs = cp(s)


ay = ca.avr_actual_surv_rate(15000)[:-1]
ax = np.array(range(70))

sy = cs.avr_actual_surv_rate(15000)[:-1]
sx = np.array(range(70))


az = np.polyfit(ax,ay,3)
aq = np.poly1d(az)
ax_new = np.linspace(ax[0], ax[-1], 50)
ay_new = aq(ax_new)
plt.plot(ax,ay,'o', ax_new, ay_new)
plt.plot(ax,ay)
plt.xlim([ax[0], ax[-1] + 1])
plt.ylim([0, 1])
plt.show()


sz = np.polyfit(sx,sy,3)
sq = np.poly1d(sz)
sx_new = np.linspace(sx[0], sx[-1], 50)
sy_new = sq(sx_new)
plt.plot(sx,sy,'o', sx_new, sy_new)
plt.xlim([sx[0], sx[-1] + 1])
plt.ylim([0, 1])
plt.show()


plt.plot(ax,ay,'o', sx, sy)
plt.xlim([ax[0], ax[-1] + 1])
plt.ylim([0, 1])
plt.show()
