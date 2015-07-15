# Goal: To generate Figure 3A for the simulation arXiv preprint
# coding: utf-8

# In[1]:

class het(object):
    
    """ This class allows to averaging 10 consecutive intervals to plot the genome evolution scatterplot """
    
    def __init__(self, inp):
        self.inp = inp
        self.rng = range(len(self.inp[0]))[::10]

    def loop1(self, ind):
        self.ind = int(ind)
        return [np.average(self.inp[self.ind][i:i+10]) for i in self.rng]
    
    def loop2(self):
        return [self.loop1(i) for i in range(len(self.inp))]
    


# In[2]:

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import cPickle
from time import sleep


# In[15]:

s = '/Volumes/group_dv/personal/DValenzano/month-by-month/Jun2015/simul/sex/17-Jun-2015/plot_values_run1.txt'
s0 = '/Volumes/group_dv/personal/DValenzano/papers/simulation_arXiv/Figure3/first-run/plot_values_run1.txt'


# In[4]:

class cp(object):
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
    def compute_actual_surv_rate(self, p):
        #self.p = p
        """                                                                                                                                                                                                                  
        Takes age distribution of two consecutive stages and computes the                                                                                                                                                    
        fractions of those survived from age x to age x+1. The cumulative product                                                                                                                                            
        of those values builds the final result.                                                                                                                                                                             
        Returns a numpy array.                                                                                                                                                                                               
        """
        div = self.age_distr_in[p]*self.pop_in[p]
        div[div == 0] = 1
        stage2 = np.array(list((self.age_distr_in[p+1]*self.pop_in[p+1]))[1:]+[0])

        res = stage2 / div
        for i in range(1,len(res)):
            res[i] = res[i-1] * res[i]
        return res        

    def avr_actual_surv_rate(self, m):
        """Averages actual survival rate over 100 stages."""
        if m <= 50:
            res2 = self.compute_actual_surv_rate(m+100)
            for i in range(m,m+100):
                res2 += self.compute_actual_surv_rate(i)
            return res2/100
        if m >= self.n_stage-50:
            res2 = self.compute_actual_surv_rate(self.n_stage-101)
            for i in range(self.n_stage-100,self.n_stage-1):
                res2 += self.compute_actual_surv_rate(i)
            return res2/100
        else:
            res2 = self.compute_actual_surv_rate(m+50)
            for i in range(m-50,m+50):
                res2 += self.compute_actual_surv_rate(i)
            return res2/100


# In[7]:

cs = cp(s) #this opens the last file, relative to the last 15k stages of the simulation for the const res-sex run


# In[8]:

hcs = het(cs.hetrz_mea)


# In[11]:

red = hcs.loop2() #this generates a reduced version of the initial file.


# In[14]:

sc_het_60k = red[-1] # is the snapshot of the 60k_th stage of the sexually reproducing population.


# In[16]:

cs0 = cp(s0)


# In[18]:

#hcs0 = het(cs0.hetrz_mea)
#red0 = hcs0.loop2()
#sc0_het_25k = red0[:2] #are the first 2 snapshots


# In[32]:

#a = ','.join([str(i) for i in sc0_het_25k[0]]).replace(',',',0\n')+',0\n'
#b = ','.join([str(i) for i in sc0_het_25k[1]]).replace(',',',1\n')+',1\n'
#ab = 'het,group\n'+a+b


# In[34]:

#z = open('/Volumes/group_dv/personal/DValenzano/papers/simulation_arXiv/Figure3/first-run/first2runs.csv', 'w')
#z.write(ab)
#z.close()

# ADDED ON 06-JUL-2015
hcs0 = het(cs0.hetrz_mea)
red0 = hcs0.loop2()
sc0_het_25k = red0[:10] #are the first 2 snapshots

a = ','.join([str(i) for i in sc0_het_25k[0]]).replace(',',',0\n')+',0\n'
b = ','.join([str(i) for i in sc0_het_25k[1]]).replace(',',',1\n')+',1\n'
c = ','.join([str(i) for i in sc0_het_25k[3]]).replace(',',',3\n')+',3\n'
d = ','.join([str(i) for i in sc0_het_25k[6]]).replace(',',',6\n')+',6\n'
z = ','.join([str(i) for i in sc_het_60k]).replace(',',',z\n')+',z\n'
abcdz = 'het,group\n'+a+b+c+d+z

z = open('/Volumes/group_dv/personal/DValenzano/papers/simulation_arXiv/Figure3/first-run/first2runs.csv', 'w')
z.write(abcdz)
z.close()

### BELOW, ADDED ON 10-Jul-2015

sdcs = het(cs.hetrz_mea_sd)
sd_red = sdcs.loop2()
sc_sd_60k = sd_red[-1]

sd_cs0 = het(cs0.hetrz_mea_sd)
sd_red0 = sd_cs0.loop2()
sd_sc0_het_25k = sd_red0[:10] #are the first 2 snapshots

sd_a = ','.join([str(i) for i in sd_sc0_het_25k[0]]).replace(',',',0\n')+',0\n'
sd_b = ','.join([str(i) for i in sd_sc0_het_25k[1]]).replace(',',',1\n')+',1\n'
sd_c = ','.join([str(i) for i in sd_sc0_het_25k[3]]).replace(',',',3\n')+',3\n'
sd_d = ','.join([str(i) for i in sd_sc0_het_25k[6]]).replace(',',',6\n')+',6\n'
sd_z = ','.join([str(i) for i in sc_sd_60k]).replace(',',',z\n')+',z\n'
sd_abcdz = 'het,group\n'+sd_a+sd_b+sd_c+sd_d+sd_z

z = open('/Volumes/group_dv/personal/DValenzano/papers/simulation_arXiv/Figure3/het-sd.csv', 'w')
z.write(sd_abcdz)
z.close()


# In[ ]:

## THIS PART ADDED ON JULY 15, 2015
#Below, I am generating the data for a figure on "Survival rate" and "Reproduction rate". 
surv60k = cs.surv_rate_in[-1] #survival rate in the last stage
surv60k_ctrl = cs.surv_rate_junk_in[-1] #control values for survival in the last stage
repr60k = cs.repr_rate_in[-1] #survival rate in the last stage
repr60k_ctrl = cs.repr_rate_junk_in[-1] #control values for reproduction in the last stage

rate_s = ','.join([str(i) for i in surv60k]).replace(',',',s\n')+',s\n' #survival
rate_sc = ','.join([','.join([str(i) for i in [i]*71]) for i in surv60k_ctrl]).replace(',',',sc\n')+',sc\n' #survival ctrl value
rate_r = ','.join([str(i) for i in repr60k]).replace(',',',r\n')+',r\n' #reproduction
rate_rc = ','.join([','.join([str(i) for i in [i]*71]) for i in repr60k_ctrl]).replace(',',',rc\n')+',rc\n' #reproduction ctrl value

rate_sr = 'rate,group\n'+rate_s+rate_sc+rate_r+rate_rc

z = open('/Volumes/group_dv/personal/DValenzano/papers/simulation_arXiv/Figure5/rate_surv-repr.csv', 'w')
z.write(rate_sr)
z.close()
