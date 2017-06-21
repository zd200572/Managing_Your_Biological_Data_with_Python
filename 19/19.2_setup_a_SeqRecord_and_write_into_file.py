'''
=======================================
setup a SeqRecord and write into a file
=======================================
'''
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import Seq
fasta_file = SeqIO.parse('1.fasta', 'fasta')
records = list(fasta_file)
#print(records[0].id)
#print(records[0].seq)
dna = Seq.Seq(str(records[0].seq), IUPAC.unambiguous_dna)
#print(records[0])

#dna = Seq.Seq(records[0].seq, IUPAC.unambiguous_dna)
dna_seq = SeqRecord(dna, id = '%s' % records[0].id, description = \
	'KC470283.1 Human papillomavirus type 68 isolate Qv33999, complete genome')
outf1 = open('HPV51.fasta', 'w')
outf2 = open('HPV51.gbk', 'w')
SeqIO.write(dna_seq, outf1, 'fasta')
SeqIO.write(dna_seq, outf2, 'genbank')
outf1.close()
outf2.close()