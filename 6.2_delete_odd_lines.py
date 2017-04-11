inf = open('Homo.fasta', 'r')
outf = open('fasta_delete_odd_lines.fasta', 'w')
for index, line in enumerate(inf):
	if (index + 1)%2 == 1:
		continue
	else:
		outf.write(line)
inf.close()
outf.close()
