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
print(record['IdList'])
print(record['Count'])
outf = open('pubmed_out.txt', 'w')
for pmid in pmids:
	handle = Entrez.efetch(db = 'pubmed', id = pmid, \
		rettype = 'medline', retmode = 'text').read()
	outf.write(handle)
#medline_records = Medline.parse(handle)
#records = list(medline_records)

'''
#SeqIO.write(medline_records, outf, 'genbank')# cannot handle this
i = 0
for record in records:
	i += 1
	outf.write('%s\n' % i)
	#print(record)
	for a in record.keys():
		outf.write('%s:%s' % (a, record[a]) + '\n')'''
outf.close()
