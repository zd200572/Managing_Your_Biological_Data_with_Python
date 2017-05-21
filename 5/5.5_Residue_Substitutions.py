prospensities = {
	'A':[0.48, 0.35, 0.17], 'C':[0.32, 0.54, 0.14], 'D':[0.81, 0.09, 0.10], 
	'E':[0.93, 0.04, 0.03], 'F':[0.42, 0.42, 0.16], 'G':[0.51, 0.36, 0.13], 
	'H':[0.66, 0.19, 0.15], 'I':[0.39, 0.47, 0.14], 'K':[0.93, 0.02, 0.05], 
	'L':[0.41, 0.49, 0.10], 'M':[0.44, 0.20, 0.36], 'P':[0.78, 0.13, 0.09],
	'Q':[0.81, 0.10, 0.09], 'R':[0.84, 0.05, 0.11], 'S':[0.70, 0.20, 0.10], 
	'T':[0.71, 0.16, 0.13], 'V':[0.40, 0.50, 0.10], 'W':[0.49, 0.44, 0.07], 
	'Y':[0.67, 0.20, 0.13], 'N':[0.82, 0, 0.08]
	}
seq_in = open('5.4_Secondary_structure.fasta')
seq = ''
for line in seq_in:
	if line[0] != '>':
		seq += line.strip()
seq_out = ''
for amino_acid in seq:
	A30 = prospensities[amino_acid][0]
	if A30 > 0.60:
		seq_out += amino_acid.upper()
	else:
		seq_out += amino_acid.lower()
print(seq + '\n')
print(seq_out)