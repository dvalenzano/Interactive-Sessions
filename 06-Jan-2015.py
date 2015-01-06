
# exome_indelsvcf.py

# Goal: to generate an indel table for a PCA analysis [YUMI]

Br_iy_242 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/242_Brain_individual_all_indel.vcf', 'rU').read()
Br_iy_259 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/259_Brain_individual_all_indel.vcf', 'rU').read()
Br_iy_272 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/272_Brain_individual_all_indel.vcf', 'rU').read()
Br_iy_296 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/296_Brain_individual_all_indel.vcf', 'rU').read()
Br_io_50 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/50_Brain_individual_all_indel.vcf', 'rU').read()
Br_io_55 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/55_Brain_individual_all_indel.vcf', 'rU').read()
Br_io_56 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/56_Brain_individual_all_indel.vcf', 'rU').read()
Br_io_77 = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/77_Brain_individual_all_indel.vcf', 'rU').read()
Bl_po = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Old_blood_all_indel.vcf', 'rU').read()
Br_po = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Old_brain_all_indel.vcf', 'rU').read()
H_po = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Old_heart_pooled_all_indel.vcf', 'rU').read()
L_po = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Old_liver_all_indel.vcf', 'rU').read()
Bl_py = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Younb_blood_all_indel.vcf', 'rU').read()
Br_py = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Young_brain_all_indel.vcf', 'rU').read()
H_py = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Young_heart_all_indel.vcf', 'rU').read()
L_py = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/Young_liver_all_indel.vcf', 'rU').read()


# In[12]:

Br_iy_242L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_iy_242.split('\n')[:-1]]


# In[15]:

Br_iy_242L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_iy_242.split('\n')[:-1]]
Br_iy_259L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_iy_259.split('\n')[:-1]]
Br_iy_272L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_iy_272.split('\n')[:-1]]
Br_iy_296L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_iy_296.split('\n')[:-1]]
Br_io_50L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_io_50.split('\n')[:-1]]
Br_io_55L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_io_55.split('\n')[:-1]]
Br_io_56L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_io_56.split('\n')[:-1]]
Br_io_77L = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_io_77.split('\n')[:-1]]
Bl_poL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Bl_po.split('\n')[:-1]]
Br_poL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_po.split('\n')[:-1]]
H_poL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in H_po.split('\n')[:-1]]
L_poL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in L_po.split('\n')[:-1]]
Bl_pyL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Bl_py.split('\n')[:-1]]
Br_pyL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in Br_py.split('\n')[:-1]]
H_pyL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in H_py.split('\n')[:-1]]
L_pyL = [','.join(i.split('\t')[:2]).replace(',','_').replace('GapFilledScaffold_', '') for i in L_py.split('\n')[:-1]]


# In[79]:

from sets import Set
bigset = Set(Br_iy_242L) | Set(Br_iy_259L) | Set(Br_iy_272L) | Set(Br_iy_296L) | Set(Br_io_50L) | Set(Br_io_55L) | Set(Br_io_56L) | Set(Br_io_77L) | Set(Bl_poL) | Set(Br_poL) | Set(H_poL) | Set(L_poL) | Set(Bl_pyL) | Set(Br_pyL) | Set(H_pyL) | Set(L_pyL) 


# In[23]:

# len(Set(Br_iy_242L))+len(Set(Br_iy_259L)) == len(bigset)


# In[82]:

bigsetL = list(bigset)
bigsetL2 = ['position']+bigsetL


# In[26]:

Br_iy_242m = ['1' if i in Br_iy_242L else '0'  for i in bigsetL ] #m as in match


# In[83]:

Br_iy_242m = ['Br_iy_242']+['1' if i in Br_iy_242L else '0'  for i in bigsetL ]
Br_iy_259m = ['Br_iy_259']+['1' if i in Br_iy_259L else '0'  for i in bigsetL ]
Br_iy_272m = ['Br_iy_272']+['1' if i in Br_iy_272L else '0'  for i in bigsetL ]
Br_iy_296m = ['Br_iy_296']+['1' if i in Br_iy_296L else '0'  for i in bigsetL ]
Br_io_50m = ['Br_io_50']+['1' if i in Br_io_50L else '0'  for i in bigsetL ]
Br_io_55m = ['Br_io_55']+['1' if i in Br_io_55L else '0'  for i in bigsetL ]
Br_io_56m = ['Br_io_56']+['1' if i in Br_io_56L else '0'  for i in bigsetL ]
Br_io_77m = ['Br_io_77']+['1' if i in Br_io_77L else '0'  for i in bigsetL ]
Bl_pom = ['Bl_po']+['1' if i in Bl_poL else '0'  for i in bigsetL ]
Br_pom = ['Br_po']+['1' if i in Br_poL else '0'  for i in bigsetL ]
H_pom = ['H_po']+['1' if i in H_poL else '0'  for i in bigsetL ]
L_pom = ['L_po']+['1' if i in L_poL else '0'  for i in bigsetL ]
Bl_pym = ['Bl_py']+['1' if i in Bl_pyL else '0'  for i in bigsetL ]
Br_pym = ['Br_py']+['1' if i in Br_pyL else '0'  for i in bigsetL ]
H_pym = ['H_py']+['1' if i in H_pyL else '0'  for i in bigsetL ]
L_pym = ['L_py']+['1' if i in L_pyL else '0'  for i in bigsetL ]


# In[84]:

tab0 = [bigsetL2] + [Br_iy_242m] + [Br_iy_242m] + [Br_iy_272m] + [Br_iy_296m] + [Br_io_50m] + [Br_io_55m] + [Br_io_56m] + [Br_io_77m] + [Bl_pom] + [Br_pom] + [H_pom] + [L_pom] + [Bl_pym] + [ Br_pym] + [H_pym] + [L_pym]


# In[87]:

tab1 = ','.join([','.join(i)+'\n' for i in tab0 ]).replace('\n,','\n')


# In[89]:

z = open('/Volumes/group_dv/group/data/whole_exome_sequencing_2014_yumi/indels/indels_tab.csv', 'w')
z.write(tab1)
z.close()


# In[91]:

bigsetL[:15]


# In[ ]:



