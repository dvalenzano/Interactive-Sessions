import sys
inp = raw_input('What family would you like to analyze?\n')
inp2 = '/Volumes/group_dv/personal/DValenzano/Jan2014/F1_inference/Go_families/inf-fam_%s.csv' % inp
fam = open(inp2, 'rU').read()
fams = fam.split('\n')[:-1]
fams2 = [','.join(i.split(',')[:5]) +','+ i.split(',')[8]+','+','.join(i.split(',')[10:]) for i in fams[1:]]
def blast(input):
    ls = []
    for i in input.split(',')[6:]:
        if len(i)== 2:
            ls.append(i[0]+','+i[1])
        else:
            ls.append(i+','+i)
    return ','.join(ls)+'\n'
pedfam = ','.join([ ','.join(i.split(',')[:6])+','+blast(i) for i in fams2 ]).replace('\n,','\n').replace(',','\t')
out0 = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/inf-fam_%s_w.ped' % (inp, inp)
z = open(out0,'w')
z.write(pedfam)
z.close()
