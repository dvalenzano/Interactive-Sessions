import sys
from sets import Set

inp = raw_input('What family would you like to analyze?\n')
omfam = '/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/fam_%s_OneMap.txt' % inp
ominp = open(omfam, 'rU').read()
mar = float(ominp.split('\n')[0].split()[1])
qtls = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fam_%s_survbysex.csv' % (inp, inp)
qtlsinp = open(qtls, 'rU').read()
qtls = [ list(i) for i in zip(*[ i.split(',')  for i in qtlsinp.split('\n')[:-1]])][0][1:]
new_ominps = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(qtls)))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in qtls]).replace('\n,','\n'\
)
out = '/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/f%s_om_survbysex.txt' % inp
z = open(out, 'w')
z.write(new_ominps)
z.close()

# from sets import Set                                                                                                                                                                                    
# qtlepi = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/inf-fam_%s.epi.qt' % (inp, inp)                                                                                                    
# qtlepiinp = open(qtlepi, 'rU').read()                                                                                                                                                                   

# #qtlepiinp2 = qtlepiinp.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepiinp.split('\n')[1:-1] if float(i.split(',')[6]) < 0.05/mar ]).replace('\n,','\n')                                          

# qtlepiinp2 = qtlepiinp.split('\n')[0] +'\n'+','.join([i+'\n' for i in qtlepiinp.split('\n')[1:-1] if float(i.split()[6]) < 0.05/mar ]).replace('\n,','\n')                                              

# inpl = ','.join([ i.split()[1] +'\n'+i.split()[3]+'\n' for i in qtlepiinp2.split('\n')[1:-1]]).replace('\n,','\n')                                                                                      

# new_ominpe = str(len(ominp.split('\n')[1].split('\t')[-1].split(',')))+' '+str(len(Set(inpl.split('\n')[:-1])))+'\n'+','.join([ i+'\n' for i in ominp.split('\n')[1:] if i.split('\t')[0][1:] in Set(in\
pl.split('\n')[:-1])]).replace('\n,','\n')                                                                                                                                                                
# out = '/Volumes/group_dv/personal/DValenzano/Mar2014/OneMap/f%s_om_epi.txt' % inp                                                                                                                       
# z = open(out, 'w')                                                                                                                                                                                      
# z.write(new_ominpe)                                                                                                                                                                                     
# z.close()    
