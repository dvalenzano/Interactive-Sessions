

assoc = open('/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_7/inf-fam_7.assoc.linear', 'rU').read()


import re


assocs = ','.join([ ','.join(i.split())+'\n' for i in assoc.split('\n')]).replace('\n,','\n')


z = open('/Volumes/group_dv/personal/DValenzano/Feb2014/plink/fam_7/inf-fam_7.assoc.linear.csv', 'w')
z.write(assocs)
z.close()



