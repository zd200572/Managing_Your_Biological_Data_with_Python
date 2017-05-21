#10.2_save_fastas.py
inf = open('SwissProt.fasta', 'r')
flag = 0
seq = ''
ac = []

def save_fastas(ac):
	outf = open(10.2/(ac[0] + '.fasta'), 'w')
	outf.write(str(sequence))
	outf.close()
	i += 1

for line in inf:
	if line[0] == '>' and flag == 1:
		ac.append(line.strip().split('|')[1])
		ac.append(seq)
		seq = ''
		ac = []
		save_fastas(ac)
	else:
		seq += line.strip()
		flag = 1
#print(AC)

