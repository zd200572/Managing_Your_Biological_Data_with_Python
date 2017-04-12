table = []
for line in open('RNA_similarity.txt'):
	table.append(line.strip().split('\t'))

#print(table)
table1 = table[1:]
print(table1)
A, U, G, C = zip(*table1)
table2 = A, U, G, C
table1.pop()

#table2 = zip(*table2)

for row in table2:
	print(row, '\n')