tk_ids = open('/Volumes/group_dv/personal/DValenzano/month-by-month/Jul2015/tk_orthologs.txt', 'rU').read()
tk_idsL = ['>' + i+'\n' for i in tk_ids.split(',')]
tk_fa = open('/Users/DValenzano/Dropbox/Fish_paper/Code/Param/Annotation/1_sequence_collection/0_Nfurzeri_sequences/nfurzeri_transcripts_all_id.fasta', 'rU')
prova = open('/Users/DValenzano/Dropbox/Fish_paper/Code/Param/Annotation/1_sequence_collection/0_Nfurzeri_sequences/prova.fa', 'rU')
prova2 = open('/Users/DValenzano/Dropbox/Fish_paper/Code/Param/Annotation/1_sequence_collection/0_Nfurzeri_sequences/prova2.fa', 'rU')
tk_idsL2 = ['>maker-GapFilledScaffold_17761-snap-gene-0.1-mRNA-1_CDS\n', '>maker-GapFilledScaffold_11884-exonerate_est2genome-gene-0.0-mRNA-1_CDS\n']+tk_idsL
#prova2.readline() == tk_idsL2[0]

#L = []
#while True:
#    line = prova2.readline()
#    if not line : break
#    else:
#        if line in tk_idsL2:
#            L.append(line + prova2.readline())
#        else:
#            pass
#prova2.close()

L = []
while True:
    line = tk_fa.readline()
    if not line : break
    else:
        if line in tk_idsL2:
            L.append(line + tk_fa.readline())
        else:
            pass
tk_fa.close()

#p2 = prova2.read()
#p2_1 = p2.split('\n')[::2]
#from sets import Set
#p2s = Set([i + '\n' for i in p2_1])
#tk2s = Set(tk_idsL2)
#p2s & tk2s
