input_file = open('C:\\Users\\shenyou\\Desktop\\bioinfo\\krother-python-for-biologists-e47cf55735c7\\sequence.gb')
output_file = open('C:\\Users\\shenyou\\Desktop\\bioinfo\\krother-python-for-biologists-e47cf55735c7\\gbout.fasta', 'w')
flag = 0
for line in input_file:
	if line[:9] == 'ACCESSION':
		AC = line.split()[1].strip()
		print(AC)
	if line[:6] == 'SOURCE':
		sp1 = line.split()[1].strip()
		sp2 = line.split()[2].strip()
		output_file.write('>' + sp1 + ' ' + sp2 + '|' + AC + '\n')
	elif line[:6] == 'ORIGIN':
		flag = 1
	elif flag == 1:
		fields = line.split()
		if fields !=[]:
			seq = ''.join(fields[1:])
			output_file.write(seq.upper() + '\n')
input_file.close()
output_file.close()