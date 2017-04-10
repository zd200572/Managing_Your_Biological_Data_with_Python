# Translating RNA into Protein
codon_table = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'', 'UAG':'',
    'UGC':'C', 'UGU':'C', 'UGA':'', 'UGG':'W',
    }
mRNA = ''
with open ("C:\\Users\\shenyou\\Desktop\\bioinfo\\workflow\\rosalind_prot.txt") as f:
		for line in f:
			mRNA += (line.rstrip()).upper()

protein = ''
i = 0
g = 0
for i in range(0, len(mRNA),3):
	if mRNA[i:i+3] in codon_table.keys():
		if mRNA[i:i+3] == 'AUG' and g != 1:
			print("tranlate starting:")
			protein += codon_table[mRNA[i:i+3]] 
			g = 1
		elif codon_table[mRNA[i:i+3]] == '':
			break
		elif g==1:
				protein += codon_table[mRNA[i:i+3]]
		elif mRNA[i:i+3] == 'STOP':
			protein += '*'
	else:
		protein += '-'

i = 0
while i < len(protein):
	print(protein[i:i + 48])
	i +=48

#print("The protein is :\n",protein)