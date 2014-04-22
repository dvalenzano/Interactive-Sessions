# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Goal: to check where all the markers in the OneMap Linkage Map lay compared to the Rqtl map

# <codecell>

f7mlg1_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG1', 'rU').read()
f7mlg1 = ','.join([ '1,'+i+'\n'  for i in f7mlg1_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg2_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG2', 'rU').read()
f7mlg2 = ','.join([ '2,'+i+'\n'  for i in f7mlg2_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg3_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG3', 'rU').read()
f7mlg3 = ','.join([ '3,'+i+'\n'  for i in f7mlg3_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg4_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG4', 'rU').read()
f7mlg4 = ','.join([ '4,'+i+'\n'  for i in f7mlg4_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg5_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG5', 'rU').read()
f7mlg5 = ','.join([ '5,'+i+'\n'  for i in f7mlg5_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg6_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG6', 'rU').read()
f7mlg6 = ','.join([ '6,'+i+'\n'  for i in f7mlg6_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg7_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG7', 'rU').read()
f7mlg7 = ','.join([ '7,'+i+'\n'  for i in f7mlg7_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg8_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG8', 'rU').read()
f7mlg8 = ','.join([ '8,'+i+'\n'  for i in f7mlg8_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg9_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG9', 'rU').read()
f7mlg9 = ','.join([ '9,'+i+'\n'  for i in f7mlg9_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg10_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG10', 'rU').read()
f7mlg10 = ','.join([ '10,'+i+'\n'  for i in f7mlg10_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg11_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG11', 'rU').read()
f7mlg11 = ','.join([ '11,'+i+'\n'  for i in f7mlg11_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg12_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG12', 'rU').read()
f7mlg12 = ','.join([ '12,'+i+'\n'  for i in f7mlg12_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg13_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG13', 'rU').read()
f7mlg13 = ','.join([ '13,'+i+'\n'  for i in f7mlg13_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg14_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG14', 'rU').read()
f7mlg14 = ','.join([ '14,'+i+'\n'  for i in f7mlg14_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg15_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG15', 'rU').read()
f7mlg15 = ','.join([ '15,'+i+'\n'  for i in f7mlg15_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg16_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG16', 'rU').read()
f7mlg16 = ','.join([ '16,'+i+'\n'  for i in f7mlg16_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg17_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG17', 'rU').read()
f7mlg17 = ','.join([ '1,'+i+'\n'  for i in f7mlg17_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg18_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG18', 'rU').read()
f7mlg18 = ','.join([ '18,'+i+'\n'  for i in f7mlg18_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg19_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG19', 'rU').read()
f7mlg19 = ','.join([ '19,'+i+'\n'  for i in f7mlg19_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg20_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG20', 'rU').read()
f7mlg20 = ','.join([ '20,'+i+'\n'  for i in f7mlg20_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg21_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG21', 'rU').read()
f7mlg21 = ','.join([ '21,'+i+'\n'  for i in f7mlg21_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg22_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG22', 'rU').read()
f7mlg22 = ','.join([ '22,'+i+'\n'  for i in f7mlg22_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg23_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG23', 'rU').read()
f7mlg23 = ','.join([ '23,'+i+'\n'  for i in f7mlg23_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg24_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG24', 'rU').read()
f7mlg24 = ','.join([ '24,'+i+'\n'  for i in f7mlg24_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg25_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG25', 'rU').read()
f7mlg25 = ','.join([ '25,'+i+'\n'  for i in f7mlg25_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg26_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG26', 'rU').read()
f7mlg26 = ','.join([ '26,'+i+'\n'  for i in f7mlg26_0.split('\n')  ]).replace('\n,','\n')[:-1]
f7mlg27_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/LG27', 'rU').read()
f7mlg27 = ','.join([ '27,'+i+'\n'  for i in f7mlg27_0.split('\n')  ]).replace('\n,','\n')[:-1]

# <codecell>

f14mlg1_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG1', 'rU').read()
f14mlg1 = ','.join([ '1,'+i+'\n'  for i in f14mlg1_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg2_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG2', 'rU').read()
f14mlg2 = ','.join([ '2,'+i+'\n'  for i in f14mlg2_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg3_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG3', 'rU').read()
f14mlg3 = ','.join([ '3,'+i+'\n'  for i in f14mlg3_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg4_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG4', 'rU').read()
f14mlg4 = ','.join([ '4,'+i+'\n'  for i in f14mlg4_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg5_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG5', 'rU').read()
f14mlg5 = ','.join([ '5,'+i+'\n'  for i in f14mlg5_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg6_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG6', 'rU').read()
f14mlg6 = ','.join([ '6,'+i+'\n'  for i in f14mlg6_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg7_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG7', 'rU').read()
f14mlg7 = ','.join([ '7,'+i+'\n'  for i in f14mlg7_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg8_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG8', 'rU').read()
f14mlg8 = ','.join([ '8,'+i+'\n'  for i in f14mlg8_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg9_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG9', 'rU').read()
f14mlg9 = ','.join([ '9,'+i+'\n'  for i in f14mlg9_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg10_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG10', 'rU').read()
f14mlg10 = ','.join([ '10,'+i+'\n'  for i in f14mlg10_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg11_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG11', 'rU').read()
f14mlg11 = ','.join([ '11,'+i+'\n'  for i in f14mlg11_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg12_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG12', 'rU').read()
f14mlg12 = ','.join([ '12,'+i+'\n'  for i in f14mlg12_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg13_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG13', 'rU').read()
f14mlg13 = ','.join([ '13,'+i+'\n'  for i in f14mlg13_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg14_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG14', 'rU').read()
f14mlg14 = ','.join([ '14,'+i+'\n'  for i in f14mlg14_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg15_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG15', 'rU').read()
f14mlg15 = ','.join([ '15,'+i+'\n'  for i in f14mlg15_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg16_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG16', 'rU').read()
f14mlg16 = ','.join([ '16,'+i+'\n'  for i in f14mlg16_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg17_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG17', 'rU').read()
f14mlg17 = ','.join([ '1,'+i+'\n'  for i in f14mlg17_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg18_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG18', 'rU').read()
f14mlg18 = ','.join([ '18,'+i+'\n'  for i in f14mlg18_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg19_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG19', 'rU').read()
f14mlg19 = ','.join([ '19,'+i+'\n'  for i in f14mlg19_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg20_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG20', 'rU').read()
f14mlg20 = ','.join([ '20,'+i+'\n'  for i in f14mlg20_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg21_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG21', 'rU').read()
f14mlg21 = ','.join([ '21,'+i+'\n'  for i in f14mlg21_0.split('\n')  ]).replace('\n,','\n')[:-1]
f14mlg22_0 = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/LG22', 'rU').read()

# <codecell>

f14m = f14mlg1+'\n\n'+f14mlg2+'\n\n'+f14mlg3+'\n\n'+f14mlg4+'\n\n'+f14mlg5+'\n\n'+f14mlg6+'\n\n'+f14mlg7+'\n\n'+f14mlg8+'\n\n'+f14mlg9+'\n\n'+f14mlg10+'\n\n'+f14mlg11+'\n\n'+f14mlg12+'\n\n'+f14mlg13+'\n\n'+f14mlg14+'\n\n'+f14mlg15+'\n\n'+f14mlg16+'\n\n'+f14mlg17+'\n\n'+f14mlg18+'\n\n'+f14mlg19+'\n\n'+f14mlg20+'\n\n'+f14mlg21+'\n\n'+f14mlg22
f7m = f7mlg1+'\n\n'+f7mlg2+'\n\n'+f7mlg3+'\n\n'+f7mlg4+'\n\n'+f7mlg5+'\n\n'+f7mlg6+'\n\n'+f7mlg7+'\n\n'+f7mlg8+'\n\n'+f7mlg9+'\n\n'+f7mlg10+'\n\n'+f7mlg11+'\n\n'+f7mlg12+'\n\n'+f7mlg13+'\n\n'+f7mlg14+'\n\n'+f7mlg15+'\n\n'+f7mlg16+'\n\n'+f7mlg17+'\n\n'+f7mlg18+'\n\n'+f7mlg19+'\n\n'+f7mlg20+'\n\n'+f7mlg21+'\n\n'+f7mlg22+'\n\n'+f7mlg23+'\n\n'+f7mlg24+'\n\n'+f7mlg25+'\n\n'+f7mlg26+'\n\n'+f7mlg27

# <codecell>

Golg = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/go32014_all_pos.csv', 'rU').read()

# <codecell>

golgs = Golg.split('\n')[:-1]
ks = [i.split(',')[0].replace('"','') for i in golgs]
vls = [i.replace('"','') for i in golgs]
d = dict(zip(ks, vls))

# <codecell>

ls7 = []
for i in f7m.split('\n\n'):
    for j in i.split('\n'):
        if j.split(',')[1] in ks:
            ls7.append(j+','+d[j.split(',')[1]]+'\n')
        else:
            ls7.append(j+',,,\n')
            
ls14 = []
for i in f14m.split('\n\n'):
    for j in i.split('\n'):
        if j.split(',')[1] in ks:
            ls14.append(j+','+d[j.split(',')[1]]+'\n')
        else:
            ls14.append(j+',,,\n')

# <codecell>

ls7j = 'LGom,marker,poson,p-val,mar,LGrqtl,posrqtl\n'+','.join(ls).replace('\n,','\n')
ls14j = 'LGom,marker,poson,p-val,mar,LGrqtl,posrqtl\n'+','.join(ls).replace('\n,','\n')

# <codecell>

z = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f7m/om-rqtl.csv', 'w')
x = open('/Volumes/group_dv/personal/DValenzano/Apr2014/R/f14m/om-rqtl.csv', 'w')
z.write(ls7j)
x.write(ls14j)
z.close()
x.close()

# <codecell>


