from operator import itemgetter
table = []
inf = open('Lowry.txt', 'r')
for line in inf:
	table.append(line.strip().split('\t'))
table1 = table[1:]
table_sorted = sorted(table1, key = itemgetter(1))
key = table[0]
out1 = ''
line = [str(x) for x in key]
out1 += '\t'.join(line) + '\n'
outf = open('sorted_Lowry.txt', 'w')
outf.write(out1)
print(out1)
i = 0
out2 = ''
for row in table_sorted:
    i += 1
    if i <3:
        line1 = [str(x) for x in row]
        out2 +='\t'.join(line1) + '\n'
        outf.write(out2)
        