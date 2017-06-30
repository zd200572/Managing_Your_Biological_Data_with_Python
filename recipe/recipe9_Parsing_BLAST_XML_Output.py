#Parsing_BLAST_XML_Output
from Bio.Blast import NCBIXML
xml_file = open("P05480_blastp.out")
blast_out = NCBIXML.parse(xml_file)
for record in blast_out:
   for alignment in record.alignments:
     print(alignment.title)
     for hsp in alignment.hsps:
       # filter by e-value
       if hsp.expect < 0.0001:
         print("score:", hsp.score)
         print("query:", hsp.query)