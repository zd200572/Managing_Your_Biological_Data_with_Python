#pycogent  module
from cogent.core.alignment import Alignment

fasta_file = open('Homo.fasta')
ali = Alignment(fasta_file.read())
print(ali.toFasta())

for column in ali.iterPositions():
	gap_fraction = float(column.count('-'))/len(column)
	print('%4.2f' % gap_fraction, )
print()