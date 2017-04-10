sequences = {}
ac = ''
seq = ''
for line in open('SwissProt.fasta'):
	if line.startswith('>') and seq != '':
		sequences[ac] = seq
		seq = ''
	if line.startswith('>'):
		ac = line.split('|')[1]
	else:
		seq = seq + line.strip()
sequences[ac] = seq
print(sequences.keys())
print(sequences['Q969J2'])