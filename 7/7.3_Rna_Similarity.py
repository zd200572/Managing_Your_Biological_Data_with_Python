table = []
for line in open('RNA_similarity.txt'):
	table.append(line.strip().split('\t'))
for row in table:
	print(row, '\n')
seq1 = 'AGCAUCUA'
seq2 = 'ACCGUUCU'
RNA_similarity = 0.0
b1 = 0
b2 = 0
for base1, base2 in zip(seq1, seq2):
	if base1 == 'A':
		b1 = 1
	elif base1 == 'G':
		b1 = 2
	elif base1 == 'C':
		b1 = 3
	elif base1 == 'U':
		b1 = 4
	if base2 == 'A':
		b2 = 1
	elif base2 == 'G':
		b2 = 2
	elif base2 == 'C':
		b2 = 3
	elif base2 == 'U':
		b2 = 4
	RNA_similarity += float(table[b1][b2])
	print(RNA_similarity)
print(RNA_similarity)