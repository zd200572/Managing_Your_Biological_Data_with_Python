'''
===================================
download nucleotide sequence
===================================
'''
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'zhaojiadong@sygene.cn'
handle = Entrez.efetch(db = 'nucleotide', id = 433282994, \
		rettype = 'gb', retmode = 'text')
record = SeqIO.read(handle, 'genbank')
outf = open('genbank.fasta', 'w')
SeqIO.write(record, outf, 'fasta')