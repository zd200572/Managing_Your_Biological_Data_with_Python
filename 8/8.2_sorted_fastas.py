from operator import itemgetter
table = []
key = ['name', 'seq', 'length']
seq = ''
length = 0
i = 0
flag = 0
inf = open('Homo.fasta', 'r')
for line in inf:
	#print(i)
	if line.startswith('>') and flag == 1:
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
		flag = 1
for row in table:
	print(row[2], '\n')
table_sorted = sorted(table, key = itemgetter(2))
out_put = open('out_put.txt', 'w')
for row in table:
	i +=1
	if i <= 3:
		row = [str(x) for x in row]
		out_put.write('\t'.join(row) + '\n')
out_put.close()