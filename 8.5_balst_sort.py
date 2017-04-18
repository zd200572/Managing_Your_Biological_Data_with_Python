from operator import itemgetter
inf = open('BlastOut.csv', 'r')
outf = open('BlastOutSorted.csv', 'w')
table = []
for line in inf:
	col = line.split(',')
	col[8] = float(col[8])
	table.append(col)

table_sorted = sorted(table, key = itemgetter(8))

for row in table_sorted:
	row = [str(x) for x in row]
	outf.write('\t'.join(row))
outf.close()