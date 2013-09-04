# Check if the newly sequenced G-cross samples contain any individual that was previously sequenced

list0 = open('/Volumes/group_dv/personal/DValenzano/stacks/samples/G/list.txt', 'rU').read()
list1 = open('/Volumes/group_dv/personal/DValenzano/stacks/samples/G/list1.txt', 'rU').read()

from sets import Set

S0 = Set(list0.split(' '))
S1 = Set(list1.split(' '))

S1 & S0

# The answer is no
# Now let's do the same for the AA cross:

list0 = open('/Volumes/group_dv/personal/DValenzano/stacks/samples/AA/list.txt', 'rU').read()
list1 = open('/Volumes/group_dv/personal/DValenzano/stacks/samples/AA/list1.txt', 'rU').read()
S0 = Set(list0.split(' '))
S1 = Set(list1.split(' '))
S1 & S0

# Also for AA cross there is no overlap -  I can now run stacks on these all samples

