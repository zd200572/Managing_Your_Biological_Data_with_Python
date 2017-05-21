prospensities = {
	'A':[1.45, 0.97], 'C':[0.77, 1.30], 'D':[0.98, 0.80], 'E':[1.53, 0.26], 
	'F':[1.12, 1.28], 'G':[0.53, 0.81], 'H':[1.24, 0.71], 'I':[1.00, 1.60], 
	'K':[1.07, 0.74], 'L':[1.34, 1.22], 'M':[1.20, 1.67], 'P':[0.59, 0.62],
	'Q':[1.17, 1.23], 'R':[0.79, 0.90], 'S':[0.79, 0.72], 'T':[0.82, 1.20],
	'V':[1.14, 1.65], 'W':[1.14, 1.19], 'Y':[0.61,1.29], 'N':[0, 0]
	}
seq = ''
seq_transformed = ''
for line in open('5.4_Secondary_structure.fasta'):
	if line[0] != '>':
		seq +=line.strip().upper()
print(seq + '\n')
for amino_acid in seq:
	pref_H = prospensities[amino_acid][0]
	pref_E = prospensities[amino_acid][1]
	if pref_H >=1 and pref_E < pref_H:
		seq_transformed += 'H'
	elif pref_E >=1 and pref_H < pref_E:
		seq_transformed += 'E'
	else:
		seq_transformed += 'L'
print(seq_transformed)