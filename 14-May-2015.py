
# Goal: to format cr1_sex2-qvals.csv and cr1_surv2-qvals.csv as R input files 

# In[2]:

c1surv = open('/Volumes/group_dv/personal/DValenzano/month-by-month/May2015/cr1_surv2-qvals.csv', 'rU').read()
c1sex = open('/Volumes/group_dv/personal/DValenzano/month-by-month/May2015/cr1_sex2-qvals.csv', 'rU').read()


# In[12]:

c1surv2 = 'index,'+c1surv.replace(' ', ',').replace('cr1p.', '').replace('"','')
c1sex2 = 'index,'+c1sex.replace(' ', ',').replace('cr1p.', '').replace('"','')


# In[14]:

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/May2015/cr1_surv2.1-qvals.csv', 'w')
z.write(c1surv2)
z.close()

z = open('/Volumes/group_dv/personal/DValenzano/month-by-month/May2015/cr1_sex2.1-qvals.csv', 'w')
z.write(c1sex2)
z.close()


# In[ ]:



