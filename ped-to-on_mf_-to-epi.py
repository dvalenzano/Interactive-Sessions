import sys
from sets import Set

inp = raw_input('What family would you like to analyze?\n')

famfile = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_%s.csv' % inp

# f1_1 = open(famfile, 'rU').read()
fo = open(famfile, 'rU').read()

# <codecell>

fof = ','.join([i+'\n' for i in fo.split('\n')[0:5]]).replace('\n,','\n')+','.join([i+'\n' for i in fo.split('\n')[5:-1] if i.split(',')[4] == '2']).replace('\n,','\n')
fom = ','.join([i+'\n' for i in fo.split('\n')[0:5]]).replace('\n,','\n')+','.join([i+'\n' for i in fo.split('\n')[5:-1] if i.split(',')[4] == '1']).replace('\n,','\n')

fofs = zip(*[ i.split(',') for i in fof.split('\n')[:-1]])
foms = zip(*[ i.split(',') for i in fom.split('\n')[:-1]])

# <codecell>

lsf = []
for i in fofs[10:]:
    lsf.append([i[0]]+[i[3]+'-'+i[4]]+list(i[5:]))
lzf = []

for i in lsf:
    lzf.append(','.join(i)+'\n')
    
lzf2 = ','.join(lzf).replace('\n,','\n')

lwf = [i.split(',')[1] for i in lzf2.split('\n')[:-1]]

# <codecell>

df = {}
df['ab-ab'] = 'B3.7'
df['aa-ab'] = 'D2.15'
df['ab-aa'] = 'D1.10'

# <codecell>

lzf3 = []
for i in lzf2.split('\n')[:-1]:
    lzf3.append(i.split(','))

# <codecell>

lzf4 = []
for i in lzf3:
    lzf4.append('*'+i[0]+'\t'+df[i[1]]+'\t'+','.join(i[2:]).replace('0','-')+'\n')   

# <codecell>

lzf5 = ','.join(lzf4).replace('\n,','\n').replace('aa','a').replace('bb','b')

finf = str(len(lzf5.split('\n')[0].split(',')))+' '+str(len(lzf5.split('\n')[:-1]))+'\n'+lzf5

outf = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fem/fam_%sf_OneMap.txt' % (inp, inp)

z = open(outf, 'w')
z.write(finf)
z.close()

# <codecell>

lsm = []
for i in foms[10:]:
    lsm.append([i[0]]+[i[3]+'-'+i[4]]+list(i[5:]))
lzm = []

for i in lsm:
    lzm.append(','.join(i)+'\n')
    
lzm2 = ','.join(lzm).replace('\n,','\n')

lwm = [i.split(',')[1] for i in lzm2.split('\n')[:-1]]

dm = {}
dm['ab-ab'] = 'B3.7'
dm['aa-ab'] = 'D2.15'
dm['ab-aa'] = 'D1.10'

lzm3 = []
for i in lzm2.split('\n')[:-1]:
    lzm3.append(i.split(','))
    
lzm4 = []
for i in lzm3:
    lzm4.append('*'+i[0]+'\t'+dm[i[1]]+'\t'+','.join(i[2:]).replace('0','-')+'\n')   
    
lzm5 = ','.join(lzm4).replace('\n,','\n').replace('aa','a').replace('bb','b')

finm = str(len(lzm5.split('\n')[0].split(',')))+' '+str(len(lzm5.split('\n')[:-1]))+'\n'+lzm5

outm = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/mal/fam_%sm_OneMap.txt' % (inp, inp)

z = open(outm, 'w')
z.write(finm)
z.close()


#import sys
#from sets import Set

#inp = raw_input('What family would you like to analyze?\n')

omfamf = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fem/fam_%sf_OneMap.txt' % (inp, inp)
omfamm = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/mal/fam_%sm_OneMap.txt' % (inp, inp)
ominp = open(omfamf, 'rU').read()
mar = float(ominp.split('\n')[0].split()[1])

qtlepif = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fem/fam_%sf.epi.qt' % (inp, inp)                                                                                
qtlepim = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/mal/fam_%sm.epi.qt' % (inp, inp)                                                           

qtlepiinpf = open(qtlepif, 'rU').read()                                                                                                                                                  
qtlepiinpm = open(qtlepim, 'rU').read()                                                                                                                                                  

qtlepiinp2f = qtlepiinpf.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepiinpf.split('\n')[1:-1] if float(i.split()[6]) < 0.05/mar ]).replace('\n,','\n')                            
qtlepiinp2m = qtlepiinpm.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepiinpm.split('\n')[1:-1] if float(i.split()[6]) < 0.05/mar ]).replace('\n,','\n')

inplf = ','.join([ i.split()[1] +'\n'+i.split()[3]+'\n' for i in qtlepiinp2f.split('\n')[1:-1]]).replace('\n,','\n')
inplm = ','.join([ i.split()[1] +'\n'+i.split()[3]+'\n' for i in qtlepiinp2m.split('\n')[1:-1]]).replace('\n,','\n')

new_ominpef = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(inplf.split('\n')[:-1])))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in Set(inplf.split('\n')[:-1])]).replace('\n,','\n')
new_ominpem = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(inplm.split('\n')[:-1])))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in Set(inplm.split('\n')[:-1])]).replace('\n,','\n')

outf = '/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/f%s_omf_epi.txt' % inp
outm = '/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/f%s_omm_epi.txt' % inp

z = open(outf, 'w')                                                                                                                                                                                      
z.write(new_ominpef)                                                                                                                                                                                     
z.close()    

z = open(outm, 'w')                                                                                                                                                                                      
z.write(new_ominpem)                                                                                                                                                                                     
z.close()

