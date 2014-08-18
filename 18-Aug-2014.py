

a = open('/Volumes/group_dv/personal/DValenzano/Aug2014/surv_list', 'rU').read()


# In[34]:

l_fig = ','.join(['species,name,age (years)\n']+[i.split('</td><td >')[2].split('<')[1].replace('em>','') +','+','.join(i.split('</td><td >')[3:5])+'\n' for i in a.split('\n')[:-1] ]).replace('\n,','\n')


# In[36]:

z = open('/Volumes/group_dv/personal/DValenzano/Aug2014/surv_list.csv', 'w')
z.write(l_fig)
z.close()


# In[ ]:



