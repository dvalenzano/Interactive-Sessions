import sys
sys.path.append('/Users/DValenzano/cecco/Rad-Tag/G-cross/')
import bootlrt
base = open('/Users/DValenzano/cecco/Rad-Tag/G-cross/G3_reduced.csv', 'rU').read()
ids = open('/Users/DValenzano/cecco/Rad-Tag/G-cross/boot2501M_IDs.csv', 'rU').read()
a = bootlrt.big(base, ids)
len(a.split('\r'))
#import lrt

###############################################################################
import math
def out(input):
  ls = []
  for i in input.split('\n')[2:]:
    a = i.count('A')
    b = i.count('B')
    if a and b >0:
        freq_a = float(a)/(a+b)
        freq_b = 1-freq_a
        MLE_ab = (freq_a**a)*(freq_b**b)
        MLE_05 = (.5**a)*(.5**b) 
        LRT = 2*(math.log(MLE_ab)-math.log(MLE_05))
        LOD = math.log10(MLE_ab/MLE_05)
        p_val = 1.0/(10**(LOD))
        out = i.split(',')[0]+':' + '\t'+str(LRT)+'\t'+str(LOD)+'\t'+str(p_val)+'\n'
        ls.append(out)
    else:
        pass
  return 'Marker'+'\tLRT\tLOD\tp_val\n'+','.join(ls)[:-1].replace('\n,','\n')
###############################################################################

a0lrt=out(a.split('\r')[0])
#a.split('\r')[0]

#>>> base = open('G3_reduced.csv', 'rU').read()
#>>> ids= open('boot2501M_IDs.csv', 'rU').read()
#>>> import bootlrt
#>>> a = bootlrt.big(base, ids) 
#>>> len(a.split('\r'))
#217

#>>> import lrt
#>>> a0lrt=lrt.out(a.split('\r')[0])
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "lrt.py", line 7, in out
#    freq_a = float(a)/(a+b)
#ZeroDivisionError: float division by zero
