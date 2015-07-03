# This class is linked to what done on 01-Jul-2015.py

class het(object):
    
    """ This class allows to averaging 10 consecutive intervals to plot the genome evolution scatterplot """
    
    def __init__(self, inp):
        self.inp = inp
        self.rng = range(len(self.inp[0]))[::10]

    def loop1(self, ind):
        self.ind = int(ind)
        return [np.average(self.inp[self.ind][i:i+10]) for i in self.rng]
    
    def loop2(self):
        return [self.loop1(i) for i in range(len(self.inp))]
    
# Usage: 
# hs = het(cs.hetrz_mea)
# prova = [hs.loop1(i) for i in range(len(hs.inp))]
# prova is an array that lists 16 lists, each containing the average value for each genomic position
    
