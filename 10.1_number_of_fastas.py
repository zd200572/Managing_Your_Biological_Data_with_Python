def fastas_number(filename):
	i = 0
	inf = open(filename, 'r')
	for line in inf:
		if line.startswith('>'):
			i += 1
	print(i)
	return i
	
fastas_number('SwissProt.fasta')