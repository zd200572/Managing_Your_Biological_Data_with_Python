from operator import itemgetter
inf = open('200762216530736.csv', 'r')
table = []
header = inf.readline()
for line in inf:
    col = line.strip().split(',')
    table.append(col)
    #print(col)

table_sorted = sorted(table, key = itemgetter(7, 6, 5, 4, 3, 2, 1, 0))
out = open('excel_out.txt', 'w')
header = [str(x) for x in header.strip().split(',')]
out.write('\t'.join(header) + '\n')
for row in table_sorted:
    #print(row, '\n')
    row = [str(x) for x in row]
    out.write('\t'.join(row) + '\n')

out.close()