#blast
#RUNNING BLAST LOCALLY FROM A PYTHON SCRIPT OR INTERACTIVE SESSION
'''
import os
cmd   = "blastp -query P05480.fasta -db nr.00 -out blast_output"
os.system(cmd)

#RUNNING BLAST LOCALLY USING BIOPYTHON
from Bio.Blast.Applications import NcbiblastpCommandline
import os
comm_line = NcbiblastpCo.mmandline(query = \
    "P05480.fasta", db = "nr.00", out = "Blast.out")
print comm_line
os.system(str(comm_line))
'''

#RUNNING BLAST THROUGH THE WEB USING BIOPYTHON
from Bio.Blast import NCBIWWW
BlastResult_handle = NCBIWWW.qblast("blastp","nr"," P05480")
BlastOut = open("P05480_blastp.out", "w")
BlastOut.write(BlastResult_handle.read())
BlastOut.close()
BlastResult_handle.close()