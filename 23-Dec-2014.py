
# Goal: to generate an input file to map a contour map with R for precipitations/temperature in Zimbabwe-Mozambique

data = open('/Volumes/group_dv/personal/DValenzano/Dec2014/meteo_data.txt', 'rU').read()


# In[59]:

data2 = data.replace('\n\n', '\n')


# In[96]:

station = [i[1:-1] for i in data2.split() if i[0]=='*']


# In[61]:

lat = [ i.split()[2] for i in data2.split('\n')[:-1] if i[0] == 'L']
lon = [ i.split()[6] for i in data2.split('\n')[:-1] if i[0] == 'L']


# In[62]:

import math
import numpy as np


# In[75]:

Tmed = map(str, [np.median(map(float, i.split()[1:])) for i in data2.split('\n') if i[:2] == 'T '])
Tavg = map(str, [np.mean(map(float, i.split()[1:])) for i in data2.split('\n') if i[:2] == 'T '])
Tmax = map(str, [np.mean(map(float, i.split()[1:])) for i in data2.split('\n') if i[:3] == 'Tma'])
Tmin = map(str, [np.mean(map(float, i.split()[1:])) for i in data2.split('\n') if i[:3] == 'Tmi'])
mm = map(str, [np.mean(map(float, i.split()[1:])) for i in data2.split('\n') if i[:2] == 'mm'])


# In[92]:

head = 'station,lat,lon,mm,tmed,tavg,tmax,tmin\n'


# In[93]:

mfin = ','.join(lat)+'\n'+','.join(lon)+'\n'+','.join(mm)+'\n'+','.join(Tmed)+'\n'+','.join(Tavg)+'\n'+','.join(Tmax)+'\n'+','.join(Tmin)


# In[97]:

l = [station] +[lat] + [lon]+[mm]+[Tmed]+[Tavg]+[Tmax]+[Tmin]
lt = head+','.join([','.join(list(i))+'\n' for i in zip(*l)]).replace('\n,','\n')


# In[98]:

z = open('/Volumes/group_dv/personal/DValenzano/Dec2014/Rinput_gis.csv', 'w')
z.write(lt)
z.close()


# In[ ]:



