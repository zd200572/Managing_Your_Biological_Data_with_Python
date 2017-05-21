#9.1_motif
import re
motif = re.compile('C.{1,4}C.')
seq= {}
inf = open('SwissProt.fasta', 'r')
seqs = {}
seq_name = ''
for line in inf:
	if line.startswith('>'):
		seq_name = line.strip()
		seqs[seq_name] = ''
	else:
		seqs[seq_name] += line.strip().upper()
#print(seqs)
for seq_name in seqs.keys():
	search = motif.search(seqs[seq_name])
	if search:
		seq[seq_name] = seqs[seq_name]
	else:
		continue

i = 0
for s in seq.keys():
	i += 1
print(i)