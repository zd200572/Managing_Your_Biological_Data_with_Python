'''
=============================
fasta protein to genbank file
=============================
'''
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import Seq

protein = open('protein.fasta').read().strip()
protein = Seq.Seq(protein, IUPAC.unambiguous_dna)
protein_record = SeqRecord(protein, id = 'test', description = 'test')
outf = open('pro_fasta_to_gb.gb', 'w')
SeqIO.write(protein_record, outf, 'genbank')
outf.close()