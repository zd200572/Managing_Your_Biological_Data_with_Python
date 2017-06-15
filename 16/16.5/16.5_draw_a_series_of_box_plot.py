"""
=================================
draw a serious of pie plots 
=================================
"""
from pylab import figure, title, pie, savefig, legend

def read_into_dict(filename):
	'''read seq_name and seqs from a
	file, into a dict'''
	bins = 0
	inf = open(filename)
	seqs = {}
	for line in inf:
		if line.startswith('>'):
			seq_name = ''
			seq_name = line[1:].split('|')[1].strip()
			seqs[seq_name] = ''
		else:
			seqs[seq_name] += line.upper().strip()
	return seqs
	

def sum_of_N_seq(sequence):
	'''sum for each frequency of N-seq
	N = 20 is decided when searching by baidu '''
	i = 0
	while i + 20 < len(sequence):
		seq = sequence[i:i+20]
		i += 1
		#print(seq)
		frequency = {}
		for amino_acid in seq:
			frequency[amino_acid] = ''
			number = seq.count(amino_acid)
			frequency[amino_acid] = number
		#for a in frequency.keys():
		#	print(a, frequency[a])
	return frequency


def draw_a_pie_plot(seq, frequency):
	"""draw fig of a squence"""
	#for b in 'ARNDCQEGHILKMFPSTWYV':
	f = sorted(frequency.items(), key=lambda d:d[1], reverse = True)
	f = f[:5]
	#print([x for x in f], '\n')
	amino = []
	count = []
	i = 0
	for b in f:
		amino.append(b[0])
		count.append(frequency[b[0]])
		i  += frequency[b[0]]
	count = [int(x)/len(seqs[seq]) for x in count]
	count.append((len(seqs[seq]) - i) / len(seqs[seq]))
	amino.append('others')
	explode = [0.15, 0.25, 0.35, 0.45, 0.55, 0.0]
	figure()
	title('pie plot of five first amino acid in fasta squence %s' % seq)
	pie(count, explode = explode, labels = amino)
	legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
	savefig('%s.png' % seq)


seqs = read_into_dict('protein.fasta')
for seq in seqs.keys():
	frequency = sum_of_N_seq(seqs[seq])
	draw_a_pie_plot(seq, frequency)