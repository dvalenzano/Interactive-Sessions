a = open('/Volumes/group_dv/personal/DValenzano/stacks/samples/plate5/replaced.sh', 'rU').read()
asp = a.split('\n')
a2 = []
for i in asp[1:]:
   a2.append(i.split(' ')[0]+' '+i.split(' ')[2]+' '+ i.split(' ')[1])
a3 = []
for i in a2:
    a3.append(i+'\n')
az = asp[0]+'\n'+','.join(a3).replace('\n,','\n')[:-1]
z = open('/Volumes/group_dv/personal/DValenzano/stacks/samples/plate5/replaced2.sh', 'w')
z.write(az)
z.close()


