'''
===================================
searching for articles in pubmed
===================================
'''
from Bio import Entrez
from Bio import Medline
from Bio import SeqIO
keyword = 'trna AND aminoacylation AND 2008[Publication Date]'
Entrez.email = 'zhaojiadong@sygene.cn'
handle = Entrez.esearch(db = 'pubmed', term = keyword)
record = Entrez.read(handle)
pmids = record['IdList']
print(record['Count'])
handle = Entrez.efetch(db = 'pubmed', id = pmids, \
		rettype = 'medline', retmode = 'text')
medline_records = Medline.parse(handle)
#records = list(medline_records)
outf = open('pubmed_out.txt', 'w')
#SeqIO.write(medline_records, outf, 'genbank')# cannot handle this
i = 0
for record in records:
	i += 1
	outf.write('%s\n' % i)
	#print(record)
	for a in record.keys():
		outf.write('%s:%s' % (a, record[a]) + '\n')
outf.close()
