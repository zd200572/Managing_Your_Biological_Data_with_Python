import re
inf = open('SwissProt.fasta', 'r')
seq_s = []
seqs = {}
seq_name = ''
for line in inf:
	if line.startswith('>'):
		seq_name = line.strip()
		seqs[seq_name] = ''
	else:
		seqs[seq_name] += line.strip()

for seq_name in seqs.keys():
	if 'kinase' and 'Homo sapiens' in seq_name:
		seq_s.append(seq_name)

for seq_name in seq_s:
	reg = re.compile('R.[ST][^P]')
	all =reg.findall(seqs[seq_name])
	if all:
		print(seq_name.split('|')[1], all)