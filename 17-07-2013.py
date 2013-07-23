# Goal: Generating a new ped file with reduced number of markers, excluding markers that miss P0 genotypes



gfam = open('NfGn_allpg_ped3_allpfam.csv', 'rU').read()
gfams = gfam.split('fam')
len(gfams)



# First thing I remove the markers where there is a missing genotype in
# either grand-parent:



gs = gfam.split('\n')
gss = []
for i in gs:
  gss.append(i.split(','))
 
gsst = zip(*gss) # In this way I have a list of lists



ls = []
for i in gsst:
    ls.append(list(i)) #this step is necessary to get an array as "gsst" is a list of tuples
len(ls)



ls2 = []
for i in ls[9:]:
  if i[1] == '0':
    pass
  elif i[2] == '0':
    pass
  else:
    ls2.append(i)



len(ls2)



# Now, this is what I wanted: I have a reduced matrix with markers with a genotype for both P0 subjects 
# 
# Then we have a total of **13396** usable markers genome-wide
# 
# Now I need to retranspose the matrix and save it



lss2 = ls[:9]+ls2
ls3 = zip(*lss2)
ls4 = []
for i in ls3:
  ls4.append(','.join(i)+'\n')
ls5 = ','.join(ls4).replace('\n,', '\n')
ls5 = ls5.replace('family', '')


z = open('/Users/DValenzano/Dropbox/tmp/NfGn_reducednew_ped.csv','w')
z.write(ls5)
z.close()



# This produced a revised, more correct version of NfGn_reduced_ped.csv, now called **NfGn_reducednew_ped.csv**

