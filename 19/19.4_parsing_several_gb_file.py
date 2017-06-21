'''
============================
parsing several genbank file
============================
'''
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
gb_file = SeqIO.parse('hpv.gb', 'genbank')
records = list(gb_file)
#print(records[0].id)
#print(records[0].seq)


for record in records:
	outf = open('%s.fasta' % record.id, 'w')
	SeqIO.write(record, outf, 'fasta')
	outf.close()