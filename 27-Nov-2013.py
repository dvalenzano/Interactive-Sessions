# Goal: to split ped files in family-matrices and infer F1 genotypes (for cross AAo), wherevere missing - adapted from 23-Jul-2013

# <codecell>

aao = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped6.csv', 'rU').read()
aao = aao.replace('A', 'a').replace('B', 'b')


aaos1t = zip(*[ i.split(',')   for i in aao.split('\n')])

# Here I am trying to remove the markers where either of the grandparents have a missing genotype
aaos2t = []
for i in aaos1t[10:]:
    if '0' not in i[1] + i[2]:
        aaos2t.append(list(i))

aaos2t = aaos1t[:10]+aaos2t
aaos2tt = zip(*aaos2t)

aaon = []
aaonn=[]

for i in aaos2tt:
   aaon.append(','.join(list(i))+'\n') 

aaonj = ','.join(aaon).replace('\n,','\n')
aaonj[-100:]
z = open('/Volumes/group_dv/personal/DValenzano/Nov2013/aaoped7.csv', 'w')
z.write(aaonj)
z.close()

# <codecell>

aaonj = aaonj.replace('Ffam', 'F_f').replace('Mfam', 'M_f') #I needed to add this line because splitting by "fam" was not giving the expected result - check out the F1 Catalog-IDs for this matrix and you'll understand the problem
aaos = aaonj.split('fam')
keys = aaos[0].split(',')[10:]
keys= keys[:-1]+[keys[-1][:-1]] #the last element had a \n attached to it!!

values = []

for i in range(10, len(aaos[0].split(','))):
               values.append(aaos[1].split('\n')[0].split(',')[i]+aaos[1].split('\n')[1].split(',')[i])
d = dict(zip(keys, values)) # A dictionary that goes like this: { '8563': 'aabb', '63406': 'aabb', ...}

# <codecell>

# Now starts the family specific loop:
for f in range(1, len(aaos)):
  valuesf1f = []
  valuesf1m = []

  for i in range(10, len(aaos[0].split(','))):
    valuesf1f.append(aaos[f].split('\n')[2].split(',')[i])

  for i in range(10, len(aaos[0].split(','))):
    valuesf1m.append(aaos[f].split('\n')[3].split(',')[i])       

  df1f = dict(zip(keys, valuesf1f)) #dictionaries are not sorted, so can't be sliced 
  df1m = dict(zip(keys, valuesf1m))

  f1f = [] #this returns the F1 female values
  for i in keys:
    if df1f[i] == '0':
      if d[i] == 'aabb': 
        f1f.append('ab')
      else:
        f1f.append(df1f[i])
    else:
      f1f.append(df1f[i])
        
  f1m = [] #this returns the F1 male values
  for i in keys:
    if df1m[i] == '0':
      if d[i] == 'aabb': 
        f1m.append('ab')
      else:
        f1m.append(df1m[i])
    else:
      f1m.append(df1m[i])
        
  ls = []
  for i in range(len(aaos[f].split('\n'))):
    if i in [0,1]+range(4, len(aaos[f].split('\n'))):
      ls.append(aaos[f].split('\n')[i]+'\n')
    elif i == 2:
      ls.append(','.join(aaos[f].split('\n')[i].split(',')[:10]+f1f)+'\n')
    elif i == 3:
      ls.append(','.join(aaos[f].split('\n')[i].split(',')[:10]+f1m)+'\n')

# <codecell>

#  lsj = ','.join(ls).replace('\n,','\n')
  lsj = aaos[0]+','.join(ls).replace('\n,','\n')

  currentfamily = '/Volumes/group_dv/personal/DValenzano/Nov2013/aao_families/inferrednew_fam_%s.csv' % aaos[f].split('\n')[0].split(',')[0]
  z = open(currentfamily, 'w') 
  z.write(lsj)
  z.close()

# <codecell>


