# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

om7f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/fem/fam_7f_OneMap.txt', 'rU').read()
sig7f = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/fem/fam_7f_sqtl_sig', 'rU').read()

# <markdowncell>

# s7 below is a list of significant markers with respective p-value

# <codecell>

s7 = ','.join([ i.split()[1]+','+i.split()[-1]+'\n'  for i in sig7f.split('\n')[:-1] ]).replace('\n,','\n')
s7m = [ i.split(',')[0] for i in s7.split('\n')[1:-1]]

# <codecell>

om7sig0 = ','.join([ i+'\n'  for i in om7f.split('\n')[:-1] if i.split('\t')[0][1:] in s7m ]).replace('\n,','\n')
om7sig1 = str(len(om7sig0.split('\n')[0].split('\t')[2].split(',')))+' '+str(len(om7sig0.split('\n')))+'\n'+om7sig0

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_7/fem/fam_7_omsig', 'w')
z.write(om7sig1)
z.close()

# <codecell>

gender = raw_input('What gender are you interested in processing [fem, mal]?\n')
gender_init = gender[0]
family = raw_input('What family are you interested in processing?\n')
omin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_OneMap.txt' %(family, gender, family, gender_init)
om = open(omin, 'rU').read()
assig = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_sqtl_sig' %(family, gender, family, gender_init)
sig = open(assig, 'rU').read()
s = ','.join([ i.split()[1]+','+i.split()[-1]+'\n'  for i in sig.split('\n')[:-1] ]).replace('\n,','\n')
sigmark = [ i.split(',')[0] for i in s.split('\n')[1:-1]]
om_sig0 = ','.join([ i+'\n'  for i in om.split('\n')[:-1] if i.split('\t')[0][1:] in sigmark ]).replace('\n,','\n')
om_sig1 = str(len(om_sig0.split('\n')[0].split('\t')[2].split(',')))+' '+str(len(om_sig0.split('\n')[:-1]))+'\n'+om_sig0
out = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_omsig' %(family, gender, family, gender_init)
z = open(out, 'w')
z.write(om_sig1)
z.close()


########################################################################################################################
########################################        Below the general version #1      ########################################      
########################################################################################################################


gender = raw_input('What gender are you interested in processing [fem, mal]?\n')
gender_init = gender[0]
family = raw_input('What family are you interested in processing?\n')
omin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_OneMap.txt' %(family, gender, family, gender_init)
om = open(omin, 'rU').read()
assig = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_sqtl_sig' %(family, gender, family, gender_init)
sig = open(assig, 'rU').read()
s = ','.join([ i.split()[1]+','+i.split()[-1]+'\n'  for i in sig.split('\n')[:-1] ]).replace('\n,','\n')
sigmark = [ i.split(',')[0] for i in s.split('\n')[1:-1]]
om_sig0 = ','.join([ i+'\n'  for i in om.split('\n')[:-1] if i.split('\t')[0][1:] in sigmark ]).replace('\n,','\n')
om_sig1 = str(len(om_sig0.split('\n')[0].split('\t')[2].split(',')))+' '+str(len(om_sig0.split('\n')[:-1]))+'\n'+om_sig0
out = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_omsig' %(family, gender, family, gender_init)
z = open(out, 'w')
z.write(om_sig1)
z.close()

########################################################################################################################
########################################        Below the general version #2      ########################################      
########################################################################################################################
# This includes 50 randomly chosen markers for cross Go

gender = raw_input('What gender are you interested in processing [fem, mal]?\n')
gender_init = gender[0]
family = raw_input('What family are you interested in processing?\n')
omin = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_OneMap.txt' %(family, gender, family, gender_init)
om = open(omin, 'rU').read()
assig = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_sqtl_sig' %(family, gender, family, gender_init)
sig = open(assig, 'rU').read()
s = ','.join([ i.split()[1]+','+i.split()[-1]+'\n'  for i in sig.split('\n')[:-1] ]).replace('\n,','\n')
sigmark = [ i.split(',')[0] for i in s.split('\n')[1:-1]]
om_sig0 = ','.join([ i+'\n'  for i in om.split('\n')[:-1] if i.split('\t')[0][1:] in sigmark ]).replace('\n,','\n')
om_sig1 = str(len(om_sig0.split('\n')[0].split('\t')[2].split(',')))+' '+str(len(om_sig0.split('\n')[:-1])+50)+'\n'+om_sig0

#here add the random choice of markers
rm = '8894,41979,36640,47896,29445,5319,2564,51049,22786,27040,52874,22797,54079,8181,12044,23179,15691,19664,24973,32502,12204,28171,24843,14880,24153,33254,40690,49836,4326,29227,45297,52775,41072,31692,47481,11202,52646,4628,49267,30859,13356,2661,32371,23360,26909,35869,3662,1201,64,50621'.split(',')
om_sig2 = ','.join([ i+'\n'  for i in om.split('\n')[:-1] if i.split('\t')[0][1:] in rm and i.split('\t')[0][1:] not in sigmark]).replace('\n,','\n')
om_sig3 = om_sig1 + om_sig2

out = '/Volumes/group_dv/personal/DValenzano/Apr2014/plink/fam_%s/%s/fam_%s%s_omsig_new' %(family, gender, family, gender_init)
z = open(out, 'w')
z.write(om_sig3)
z.close()


