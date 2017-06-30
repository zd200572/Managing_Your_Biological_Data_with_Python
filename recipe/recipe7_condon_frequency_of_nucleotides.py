#recipe7_condon_frequency_of_nucleotides.py
# This program calculates the codon frequency in a RNA sequence 
# (it could also be an entire genome)
aa_codon = {
	'A':['GCU', 'GCC', 'GCA', 'GCG'], 'C':['UGU', 'UGC'],
	'D':['GAU', 'GAC'], 'E':['GAA', 'GAG'], 'F':['UUU', 'UUC'],
	'G':['GGU', 'GGC', 'GGA', 'GGG'], 'H':['GAU', 'CAC'],
	'k':['AAA', 'AAG'], 'I':['AUU', 'AUC', 'AUA']
	'L':['UUA','UUG','CUU','CUC','CUA','CUG'],'M':['AUG'],
	'N':['AAU','AAC'],'P':['CCU','CCC','CCA','CCG'],
	'Q':['CAA','CAG'],'R':['CGU','CGC','CGA','CGG','AGA','AGG'],
	'S':['UCU','UCC','UCA','UCG','AGU','AGC',],'Y':['UAU','UAC'],
	'T':['ACU','ACC','ACA','ACG'],
	'V':['GUU','GUC','GUA','GUG'],'W':['UGG'],
	'STOP':['UAG','UGA','UAA']
}
codon_count = {
'GCU':0,'GCC':0,'GCA':0,'GCG':0,'CGU':0,'CGC':0,   
'CGA':0,'CGG':0,'AGA':0,'AGG':0,'UCU':0,'UCC':0,
'UCA':0,'UCG':0,'AGU':0,'AGC':0,'AUU':0,'AUC':0,
'AUA':0,'AUU':0,'AUC':0,'AUA':0,'UUA':0,'UUG':0,
'CUU':0,'CUC':0,'CUA':0,'CUG':0,'GGU':0,'GGC':0,
'GGA':0,'GGG':0,'GUU':0,'GUC':0,'GUA':0,'GUG':0, 
'ACU':0,'ACC':0,'ACA':0,'ACG':0,'CCU':0,'CCC':0,
'CCA':0,'CCG':0,'AAU':0,'AAC':0,'GAU':0,'GAC':0, 
'UGU':0,'UGC':0,'CAA':0,'CAG':0,'GAA':0,'GAG':0,   
'CAU':0,'CAC':0,'AAA':0,'AAG':0,'UUU':0,'UUC':0, 
'UAU':0,'UAC':0,'AUG':0,'UGG':0,'UAG':0,
'UGA':0,'UAA':0}
# Writes the frequency of each codon to a file
def calc_freq(codon_count, out_file):
    count_tot = {}
    for aa in aa_codon.keys():
        n = 0
        for codon in aa_codon[aa]:
            n = n + codon_count[codon]
        count_tot[aa] = float(n)
    for aa in aa_codon.keys():
        for codon in aa_codon[aa]:
            if count_tot[aa] != 0.0: 
                freq =  codon_count[codon] / count_tot[aa]
            else:
                freq = 0.0
            out_file.write('%4s\t%5s\t%4d\t%9.3f\n'% \
                (aa,codon,codon_count[codon], freq))
in_file = open('A06662.1.fasta') 
out_file = open('CodonFrequency.txt', 'w')
# Reads the RNA sequence into a single string
rna = ''
for line in in_file:
    if not line[0] == '>': 
        rna = rna + line.strip()
# Scans the sequence frame by frame,
# counts the number of occurrences 
# of each codon, and stores it in codon_count dictionary.
# Then calls calc_freq() 
for j in range(3):
    out_file.write('!!Codon frequency in frame %d\n' %(j+1)) 
    out_file.write('  AA\tcodon\thits\tfrequency\n')
    prot = '' 
    for i in range(j, len(rna), 3):
        codon = rna[i:i + 3]
        if codon in codon_count:
            codon_count[codon] = codon_count[codon] + 1
    calc_freq(codon_count, out_file) 
out_file.close()