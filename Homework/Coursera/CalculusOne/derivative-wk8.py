
# coding: utf-8

# In[2]:

import math
import numpy
import scipy


# In[37]:

def num(t):
    return 2.0*(16.0*t*math.sin(math.pi/3.0)*16.0*math.sin(math.pi/3.0))+2.0*(16.0*t*math.cos(math.pi/3.0)-10.0*t)*(16.0*math.cos(math.pi/3.0)-10.0)


# In[38]:

def den(t):
    return 2.0*(((16.0*t*math.sin(math.pi/3.0))**2 + (16.0*t*math.cos(math.pi/3.0)-10.0*t)**2)**0.5)


# In[39]:

n= den(10.0)
n


# In[46]:

def rat(t, va, vb):
    num = float(2.0*(vb*t*math.sin(math.pi/3.0)*vb*math.sin(math.pi/3.0))+2.0*(vb*t*math.cos(math.pi/3.0)-va*t)*(vb*math.cos(math.pi/3.0)-va))
    den = float(2.0*(((vb*t*math.sin(math.pi/3.0))**2 + (vb*t*math.cos(math.pi/3.0)-va*t)**2)**0.5))
    return num/den


# In[50]:

c = rat(4, 9, 9)
c


# In[ ]:



