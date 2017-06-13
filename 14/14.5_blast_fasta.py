import os
from Bio.Blast import NCBIXML
import sys
##blast local query 
def blast_test(filename):
	if os.path.exists(filename):
		os.system('blastn -query ' + filename + ' -db hpv53l1db' + ' -out' + ' blast_out.xml ' + '-outfmt 5')

blast_test('hpv53l.fasta')

def parse_blast_xml(xml_file):
	xml = open(xml_file)
	blast_out = NCBIXML.parse(xml)

	for record in blast_out:
		for alignment in record.alignments:
			print(alignment.title)
			for hsp in alignment.hsps:
				#filter by e-value
				if hsp.expect < 0.0001:
					print("score:", hsp.score)
					print('query:', hsp.query)
					print('match:', hsp.match)
					print('sbjct:', hsp.sbjct)
					print('#' * 70)
					print()

parse_blast_xml('blast_out.xml')