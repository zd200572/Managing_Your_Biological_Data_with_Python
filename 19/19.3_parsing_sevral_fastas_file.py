'''
============================
parsing several fasta file
============================
'''
from Bio import SeqIO
fasta_file = SeqIO.parse('1.fasta', 'fasta')
records = list(fasta_file)
#print(records[0].id)
#print(records[0].seq)

outf = open('fasta_id.txt', 'w')
for a in records:
	outf.write('%s' % a.id + '\n')

outf.close()