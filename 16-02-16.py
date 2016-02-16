
# coding: utf-8

# In[2]:

import numpy as np
import matplotlib.pyplot as plt

# Following instructions from: http://nxn.se/post/46440196846/making-nicer-looking-pie-charts-with-matplotlib

pc_all = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Feb2016/uBiome_paper/Figure1/piecharts.csv', 'rU').read()

pc_all_l = pc_all.split('\n')

pc = [i.split(',') for i in pc_all_l ][:-1]
pct = zip(*pc) #transpose the pc array
pct = [list(i) for i in pct ]

fig = plt.figure(figsize=[10,10])
ax = fig.add_subplot(111)
cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., (len(pct[0])-1)))

labels = pct[0][1:] 
slices = [i[1:] for i in pct[1:] ]
ax.pie(slices[0], colors=colors, labels=labels, labeldistance=1.05)
ax.set_title("Figure 1");

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)


# The dark edges look bad, so I will remove them

# In[27]:

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

pie_wedge_collection = ax.pie(slices[1], colors=colors, labels=labels, labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 2");


# In[34]:

# Follows a plot where I sort the Phyla by abundance


# In[28]:

sort_pc = sorted(pc[1:], key= lambda x: (x[1]))
spct = [ list(i) for i in zip(*sort_pc)]
labels2 = spct[0]


# In[32]:

# plt.show()
sort_slices = sorted(slices, key= lambda x: (x[0]))

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111) #this adds polar projections

pie_wedge_collection = ax.pie(spct[1], colors=colors, labels=spct[0], labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 3");


# In[ ]:

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

pie_wedge_collection = ax.pie(slices[1], colors=colors, labels=labels, labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title(pc[0][2]);
plt.show()

slices
# In[ ]:



