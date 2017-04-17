table = []
key = ['name', 'seq', 'length']
seq = ''
length = 0
i = 0
l = 0
inf = open('Homo.fasta', 'r')
for line in inf:
	#print(i)
	if line.startswith('>'):
		col = []
		col.append(line.strip())
		col.append(seq)
		col.append(str(length))
		table.append(col)
		print(col[0])
		length = 0
		seq = ''
	else:
		length += len(line.strip())
		seq += line.strip()
for row in table:
	print(row[2], '\n')