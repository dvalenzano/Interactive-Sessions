# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# the output is going to be a table with three columns: including marker, p-value, and method  
# this output can be used as an input for R

# <codecell>

class Fam(object):
    
    'Generating an R file for all the SQTL, family by family'

    version = '0.1'
    
    def __init__(self, vam):
        self.vam = str(vam)
        
    def __str__(self):
        return 'We are analyzing family %s' % str(self.vam)

    def process(self):

        # First we read all the files 
        fam = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/' % self.vam
        famas = 'inf-fam_%sas.assoc.linear' % self.vam
        famepi = 'inf-fam_%s.epi.qt' % self.vam
        ffam = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/fem/' % self.vam
        ffamas = 'fam_%sf_sqtl.assoc.linear' % self.vam
        ffamepi = 'fam_%sf.epi.qt' % self.vam
        mfam = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/fam_%s/mal/' % self.vam
        mfamas = 'fam_%sm_sqtl.assoc.linear' % self.vam
        mfamepi = 'fam_%sm.epi.qt' % self.vam
        fam_as =  open(fam+famas, 'rU').read()
        fam_e = open(fam+famepi, 'rU').read()
        fam_fas = open(ffam+ffamas, 'rU').read()
        fam_fe = open(ffam+ffamepi, 'rU').read()
        fam_mas = open(mfam+mfamas, 'rU').read()
        fam_me = open(mfam+mfamepi, 'rU').read()
        

        ## sex-association first
        as0 = []
        for i in fam_as.split('\n')[2:-1:2]:
            as0.append(i.split()[1]+','+ ','.join(i.split()[6:])+','+famas+'\n')
        as0s = ','.join(as0).replace('\n,','\n')
        
        as1 = []
        for i in fam_fas.split('\n')[2:-1:2]:
            as1.append(i.split()[1]+','+ ','.join(i.split()[6:])+','+ffamas+'\n')
        as1s = ','.join(as1).replace('\n,','\n')
        
        as2 = []
        for i in fam_mas.split('\n')[2:-1:2]:
            as2.append(i.split()[1]+','+ ','.join(i.split()[6:])+','+mfamas+'\n')
        as2s = ','.join(as2).replace('\n,','\n')

        asall = fam_as.split('\n')[0].split()[1]+','+','.join(fam_as.split('\n')[0].split()[6:])+',group\n'+as0s+as1s+as2s
        
        asout = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/sqtlas_fam%s.csv' %self.vam
        zas = open(asout, 'w')
        zas.write(asall)
        zas.close()
        
                ## sex-association first
        e0 = []
        for i in fam_e.split('\n')[1:-1]:
            e0.append(i.split()[1]+','+ ','.join(i.split()[3:])+','+famepi+'\n')
        e0s = ','.join(e0).replace('\n,','\n')
        
        e1 = []
        for i in fam_fe.split('\n')[1:-1]:
            e1.append(i.split()[1]+','+ ','.join(i.split()[3:])+','+ffamepi+'\n')
        e1s = ','.join(e1).replace('\n,','\n')
        
        e2 = []
        for i in fam_me.split('\n')[1:-1]:
            e2.append(i.split()[1]+','+ ','.join(i.split()[3:])+','+mfamepi+'\n')
        e2s = ','.join(e2).replace('\n,','\n')

        eall = fam_e.split('\n')[0].split()[1]+','+','.join(fam_e.split('\n')[0].split()[3:])+',group\n'+e0s+e1s+e2s
        
        epiout = '/Volumes/group_dv/personal/DValenzano/Mar2014/plink/sqtle_fam%s.csv' %self.vam
        ze = open(epiout, 'w')
        ze.write(eall)
        ze.close()
        

# <codecell>

f14 = Fam(14)
print(f14)
f14.process()

# <codecell>

f1_1 = Fam(1.1)
print(f1_1)
f1_1.process()

# <codecell>

f8 = Fam(8)
print(f8)
f8.process()

# <codecell>


