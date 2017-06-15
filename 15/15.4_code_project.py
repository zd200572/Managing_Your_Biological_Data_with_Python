#15.3_primary_frame_of_project
sequence = ''

def read_seq(filename):
	seq_name = ''
	
	'''read sequences from file'''
	inf = open(filename, 'r')
	for line in inf:
		if line[0] == '>':
			seq_name = line[1:].strip()
			sequence = ''
			print(seq_name)
		else:
			sequence += line.upper().strip()
			#print(sequence)
	print(sequence)
	return sequence
	

def sum_of_N_seq(sequence):
	'''sum for each frequency of N-seq
	N = 20 is decided when searching by baidu '''
	i = 0
	while i + 20 < len(sequence):
		list = []
		seq = sequence[i:i+20]
		i += 1
		print(seq)
		frequency = {}
		for amino_acid in seq:
			number = seq.count(amino_acid)
			frequency[amino_acid] = number
		list.append(frequency)
		for a in list:
			print(a)
	return list


def print_predicted_helix():
	'''print the seq and position of predicted helix'''
	pass



seq1 = read_seq('lysozyme .fasta')
sum_of_N_seq(seq1)
seq2 = read_seq('bacterirhodopsin.fasta')
sum_of_N_seq(seq2)