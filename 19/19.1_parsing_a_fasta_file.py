'''
============================
parsing several genbank file
============================
'''
from Bio import SeqIO
gb_file = SeqIO.parse('hpv.gb', 'genbank')
records = list(gb_file)
print(records[0].id)
print(records[0].seq)