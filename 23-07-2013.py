# This is an update of the 19-07-2013 session, which uses a new input file, and saves a different output file name
g = open('/Users/DValenzano/Dropbox/tmp/NfGn_reducednew_ped.csv', 'rU').read()
gs = g.split('fam')

keys = gs[0].split(',')[9:]
keys= keys[:-1]+[keys[-1][:-1]] #the last element had a \n attached to it!!

values = []

for i in range(9, len(gs[0].split(','))):
               values.append(gs[1].split('\n')[0].split(',')[i]+gs[1].split('\n')[1].split(',')[i])
d = dict(zip(keys, values)) # A dictionary that goes like this: { '8563': 'aabb', '63406': 'aabb', ...}

# Now starts the family specific loop:
for f in range(1, len(gs)):
  valuesf1f = []
  valuesf1m = []

  for i in range(9, len(gs[0].split(','))):
    valuesf1f.append(gs[f].split('\n')[2].split(',')[i])

  for i in range(9, len(gs[0].split(','))):
    valuesf1m.append(gs[f].split('\n')[3].split(',')[i])       

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
  for i in range(len(gs[f].split('\n'))):
    if i in [0,1]+range(4, len(gs[f].split('\n'))):
      ls.append(gs[f].split('\n')[i]+'\n')
    elif i == 2:
      ls.append(','.join(gs[f].split('\n')[i].split(',')[:9]+f1f)+'\n')
    elif i == 3:
      ls.append(','.join(gs[f].split('\n')[i].split(',')[:9]+f1m)+'\n')
        
#  lsj = ','.join(ls).replace('\n,','\n')
  lsj = gs[0]+','.join(ls).replace('\n,','\n')

  currentfamily = '/Users/DValenzano/Dropbox/tmp/inferrednew_fam_%s.csv' % gs[f].split('\n')[0].split(',')[0]
  z = open(currentfamily, 'w') 
  z.write(lsj)
  z.close()
