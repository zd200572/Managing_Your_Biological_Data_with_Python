fasta = open('SwissProt.fasta', 'r')
fout = open('Homo.fasta', 'w')
seq = ''
for line in fasta:
	if line[0] == '>' and seq == '':
		header = line
	elif line[0] != '>':
		seq += line
	elif line[0] == '>' and seq !='':
		if "Homo sapiens" in header:
			fout.write(header + seq)
		seq = ''
		header =line.strip()
if "Homo sapiens" in header:
			fout.write(header + seq)
fout.close()