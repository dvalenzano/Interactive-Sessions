g = open('/Users/DValenzano/Dropbox/tmp/NfGn_reduced_ped.csv', 'rU').read()
gs = g.split('fam')
keys = gs[0].split(',')[9:]

keys= keys[:-1]+[keys[-1][:-1]] #the last element had a \n attached to it!!

values = []
for i in range(9, len(gs[0].split(','))):
               values.append(gs[1].split('\n')[0].split(',')[i]+gs[1].split('\n')[1].split(',')[i])

d = dict(zip(keys, values)) # A dictionary that goes like this: { '8563': 'aabb', '63406': 'aabb', ...}

# Alternatively, I will make another dictionary for the F1s as well:
valuesf1f = []
valuesf1m = []

for i in range(9, len(gs[0].split(','))):
    valuesf1f.append(gs[1].split('\n')[2].split(',')[i])

for i in range(9, len(gs[0].split(','))):
    valuesf1m.append(gs[1].split('\n')[3].split(',')[i])       

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
for i in range(len(gs[1].split('\n'))):
    if i in [0,1]+range(4, len(gs[1].split('\n'))):
        ls.append(gs[1].split('\n')[i]+'\n')
    elif i == 2:
        ls.append(','.join(gs[1].split('\n')[i].split(',')[:9]+f1f)+'\n')
    elif i == 3:
        ls.append(','.join(gs[1].split('\n')[i].split(',')[:9]+f1m)+'\n')
        
lsj = ','.join(ls).replace('\n,','\n')

z = open('/Users/DValenzano/Dropbox/tmp/prova.csv', 'w')
z.write(lsj)
z.close()
