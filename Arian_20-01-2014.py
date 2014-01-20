# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

young = []
adult = []
old = []
resources = []

### script here ###

young.append(#output for len(young) at every time point)
aduld.append(#output for len(adult) at every time point)
old.append(#output for len(old) at every time point)
resources.append(#same thing as above)
 
# These are all lists, not strings, so they cannot be saved as a file. 

yst = ','.join(young)+'\n' #now you have a string
ast = ','.join(adult)+'\n'
ost = ','.join(old)+'\n'
res = ','.join(resources)+'\n'

tab = (yst+ast+ost+res).replace('\n,','\n')

tabt = zip(*[i.split(',') for i in tab.split('\n')]) #transpose tab so that y, a, o, r are columns, not rows - now you have an array, which is a list of lists, so we need to re-join everything in a big string

tabtj = ','.join([  ','.join(list(i))+'\n'  for i in tabt]).replace('\n,','\n')

z = open('/path-to-file-you-want-to-save', 'w')
z.write(tabtj)
z.close()

#####################################################################
############################# SESSION 2 #############################
#####################################################################

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#start_population = int(input('Starting number of individuals: '))
start_population = 100

# <codecell>

#resources = int(input("Starting resources: "))
resources = 250
# time = int(input("Time passed: "))
time = 250
##k = float(input("Resource growth factor: "))
k = 1.5
population = []
starting_age = 19
new_born_age = 0
time_passed = 0
x = 1.0
young_final = []
adult_final = []
old_final = []
resources_final = []

# <codecell>

from random import*

def chance(z):
    z = z * 1000000
    if (randint(1, 1000000) <= z):
        y = True
    else:
        y = False
    return y

for i in range(start_population):
    a = ["individual"]
    a.append(i+1)
    a[1] = str(a[1])
    a[0:2] = ["".join(a[0:2])]
    a.append(starting_age)
    population.append(a)

# <codecell>

##programm begins here
for i in range(time):

    disease = 1
    war = 1
    catastrophe = 1
    war_2 = 1
    disease_2 = 1
    good_year = 1

    if (len(population) == 0):
        print("EXTINCT")
        break
##x increases the probability of death when there is lack of resources
    if (resources == 0):
        x = x*1.5
    else:
        x = 1.0
    ##print(x)    
##drift
##    if chance(0.10):
##        disease = 1.05
##    if chance(0.10):
##        disease_2 = 1.025
##    if chance(0.10):
##        catastrophe = 0.95
##    if chance(0.10):
##        good_year = 1.05
##    if chance(0.02):
##        war = 1.4
##        war_2 = 1.2
        

    adult = []
    for i in range(len(population)):
        if (population[i][1] > 18) and (population[i][1] < 50):
            adult.append(population[i])
        
    resources_population = float(resources/len(population))
    if (resources_population == 0.0):
        resources_population = 0.0
    if (resources_population >= 1.25):
        resources_population = 1.25

    ##
    
    ##here one can adjust the reproduction factor (now between 10 and 25%)
    new_born = int(uniform(0.10, 0.25)*len(adult)*resources_population)
    for i in range(new_born):
        a = ["individual"]
        a.append(len(population)+1)
        a[1] = str(a[1])
        a[0:2] = ["".join(a[0:2])]
        a.append(new_born_age)
        population.append(a)

    young = []
    adult = []
    old = []
    for i in range(len(population)):
        if (population[i][1] <= 18):
            young.append(population[i])
        elif (population[i][1] >= 50):
            old.append(population[i])
        else:
            adult.append(population[i])

    ##resources
    resources += -len(population)
    resources = resources * k
    ##resources = int((resources +(len(adult) + len(old)/2)*2)*catastrophe*good_year)
    
    ##resources cannot be negative
    if (resources <= 0):
        resources = 0
    
    
    j = 0
    q = len(population)
    for i in range(q):
        if (population[i-j][1] in range(0,1) and chance(0.006930*x*disease)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(1,2) and chance(0.000517*x*disease)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(2,3) and chance(0.000347*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(3,4) and chance(0.000243*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(4,5) and chance(0.000202*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(6,7) and chance(0.000177*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(7,8) and chance(0.000167*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(8,9) and chance(0.000154*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(9,10) and chance(0.000137*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(10,11) and chance(0.000125*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(11,12) and chance(0.000130*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(12,13) and chance(0.000170*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(13,14) and chance(0.000253*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(14,15) and chance(0.000366*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(15,16) and chance(0.000491*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(16,17) and chance(0.000607*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(17,18) and chance(0.000706*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(18,19) and chance(0.000780*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(19,20) and chance(0.000833*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(20,21) and chance(0.000888*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(21,22) and chance(0.000945*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(22,23) and chance(0.000983*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(23,24) and chance(0.000996*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(24,25) and chance(0.000991*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(25,26) and chance(0.000981*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(26,27) and chance(0.000977*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(27,28) and chance(0.000979*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(28,29) and chance(0.000993*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(29,30) and chance(0.001019*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(30,31) and chance(0.001050*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(31,32) and chance(0.001087*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(32,33) and chance(0.001141*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(33,34) and chance(0.001215*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(34,35) and chance(0.001302*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(35,36) and chance(0.001395*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(36,37) and chance(0.001492*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(37,38) and chance(0.001602*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(38,39) and chance(0.001728*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(39,40) and chance(0.001870*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(40,41) and chance(0.002021*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(41,42) and chance(0.002181*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(42,43) and chance(0.002355*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(43,44) and chance(0.002550*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(44,45) and chance(0.002768*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(45,46) and chance(0.003014*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(46,47) and chance(0.003284*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(47,48) and chance(0.003567*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(48,49) and chance(0.003851*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(49,50) and chance(0.004138*x*disease_2*war)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(50,51) and chance(0.004443*x)*disease*(war_2)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(51,52) and chance(0.004780*x)*disease*(war_2)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(52,53) and chance(0.005152*x)*disease*(war_2)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(53,54) and chance(0.005579*x)*disease*(war_2)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(54,55) and chance(0.006075*x)*disease*(war_2)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(55,56) and chance(0.006654*x)*disease*(war_2)):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(56,57) and chance(0.007309*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(57,58) and chance(0.008023*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(58,59) and chance(0.008773*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(59,60) and chance(0.009563*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(60,61) and chance(0.010446*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(61,62) and chance(0.011448*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(62,63) and chance(0.012521*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(63,64) and chance(0.013646*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(64,65) and chance(0.014828*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(65,66) and chance(0.016058*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(66,67) and chance(0.017400*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(67,68) and chance(0.018933*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(68,69) and chance(0.020701*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(69,70) and chance(0.022663*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(70,71) and chance(0.024663*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(71,72) and chance(0.026741*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(72,73) and chance(0.029042*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(73,74) and chance(0.031663*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(74,75) and chance(0.034588*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(75,76) and chance(0.037675*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(76,77) and chance(0.040886*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(77,78) and chance(0.044437*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(78,79) and chance(0.048530*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(79,80) and chance(0.053313*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(80,81) and chance(0.058841*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(81,82) and chance(0.065093*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(82,83) and chance(0.072140*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(83,84) and chance(0.079850*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(84,85) and chance(0.088195*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(85,86) and chance(0.096751*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(86,87) and chance(0.105884*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(87,88) and chance(0.115605*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(88,89) and chance(0.125917*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(89,90) and chance(0.136824*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(90,91) and chance(0.148322*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(91,92) and chance(0.160404*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(92,93) and chance(0.173058*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(93,94) and chance(0.186266*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(94,95) and chance(0.200006*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(95,96) and chance(0.214248*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(96,97) and chance(0.228960*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(97,98) and chance(0.244099*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(98,99) and chance(0.259622*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(99,100) and chance(0.275475*x*disease*(war_2))):
            population.remove(population[i-j])
            j += 1
        elif (population[i-j][1] in range(100,101) and chance(1.000000)):
            population.remove(population[i-j])
            j += 1

    for i in range(len(population)):
        population[i][1] += 1

    time_passed += 1
    
##    print ("",sep="\n")
##    print("Young: ", len(young))
##    print("Adult: ", len(adult))
##    print("Old: ", len(old))
##    print("Resources: ", resources)
##    print("Time passed: ", time_passed)
    
####    print("Disease: ", disease)
####    print("War: ", war)
####    print("Catastrophe: ", catastrophe)
##    print ("",sep="\n")
    

### script here ###

    young_final.append(str(len(young)))
    adult_final.append(str(len(adult)))
    old_final.append(str(len(old)))
    resources_final.append(str(resources))

# <codecell>

# These are all lists, not strings, so they cannot be saved as a file. 

yst = ','.join(young_final)+'\n' #now you have a string
ast = ','.join(adult_final)+'\n'
ost = ','.join(old_final)+'\n'
res = ','.join(resources_final)+'\n'

##print(yst)

tab = (yst+ast+ost+res).replace('\n,','\n')

tabt = zip(*[i.split(',') for i in tab.split('\n')[:-1]]) #transpose tab so that y, a, o, r are columns, not rows - now you have an array, which is a list of lists, so we need to re-join everything in a big string

tabtj = 'yst, ast, ost, res\n'+','.join([  ','.join(list(i))+'\n'  for i in tabt]).replace('\n,','\n')

#print(tabtj)
z = open('/Users/DValenzano/Desktop/Arian_output.csv', 'w')
z.write(tabtj)
z.close()

# <codecell>

tabtj[:100]

# <codecell>



