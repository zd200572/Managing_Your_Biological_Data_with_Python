from Bio import AlignIO, SeqIO
#alignment = AlignIO.read('PF00042.sth', 'stockholm')
print(alignment)
handle = open('PF00042.fasta', 'w')
AlignIO.write(alignment, handle, 'fasta')
#SeqIO also can do this


#get only a seq alone
for record in alignment:
	print(record.id, record.annotations, record.seq)

#several MSA
alignments = AlignIO.parse('PF00042.sth', 'stockholm')
for alignment in alignments:
	print(alignment)
	#get one record
	for record in alignment:
		print(record.id, record.annotations, record.seq)
handle.close()
