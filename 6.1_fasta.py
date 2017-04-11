inf = open('Homo.fasta', 'r')
outf = open('fasta_out_M.txt', 'w')
seq_name = ''
i = 0
for index, line in enumerate(inf):
	if line.startswith('>') and seq_name == '':
		seq_name = line.strip()
		i = index
	elif line[0] == 'M' and i == index - 1:
		outf.write(seq_name + '\n')
		seq_name = ''
inf.close()
outf.close()