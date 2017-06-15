#hist plot of a fasta file contain many seqs
from pylab import figure, title, xlabel, ylabel, \
	hist, axis, grid, savefig

def read_into_dict(filename):
	'''read seq_name and seqs from a
	file, into a dict'''
	bins = 0
	inf = open(filename)
	seqs = {}
	for line in inf:
		if line.startswith('>'):
			seq_name = ''
			seq_name = line[1:].split('.')[0].strip()
			seqs[seq_name] = ''
		else:
			seqs[seq_name] += line.upper().strip()
	return seqs

def get_seq_length_and_name(seqs):
	'''get the sequence name and length,
	prepare for the figure drawing'''
	ydata = []
	for seq in seqs.keys():
		ydata.append(len(seqs[seq]))
	#print(ydata)
	return ydata

def draw_fig(ydata):
	'''draw picture using data from above'''
	
	figure()
	num, bins, patches = hist(ydata, 4, normed = 1.0, \
		histtype = 'bar', facecolor = 'red', alpha = 0.75)
	title('histgram of fasta files')
	xlabel('length')
	ylabel('frequency')
	axis()
	grid(True)
	savefig('fasta_length_histgram.png', dpi = 300)

seqs = read_into_dict('hpv68 L1.fasta')
ydata = get_seq_length_and_name(seqs)
draw_fig(ydata)