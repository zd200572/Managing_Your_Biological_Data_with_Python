#10.2_save_fastas.py
inf = open('SwissProt.fasta', 'r')
flag = 0
seq = ''

def save_fastas(ac):
	outf = open(ac[0] + '.fasta', 'w')
	i = 0
	while(i < len(sequence)):
		outf.write(str(sequence[i:i + 60]) + '\n')
		i += 60
	outf.close()

for line in inf:
	if line[0] == '>' and flag == 1:
		AC = line.strip().split('|')[1]
		sequence = seq
		seq = ''
		ac = [AC, sequence]
		save_fastas(ac)
	else:
		seq += line.strip()
		flag = 1
#print(AC)

