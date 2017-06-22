'''
====================================
a program do something like Endnote
====================================
'''
from Bio import Entrez
from Bio import Medline
import re

#get pubmed ids
inf = open('endnote.txt', 'r')
#print(inf.read())
#pattern = re.compile('\[(.*?)\]')
#pubmed_ids = pattern.findall(inf.read())
#print(pubmed_ids)
#inf.close()


pubmed_ids = []
for line in inf:
	pubmed_ids.append(line.strip().split('[')[1].split(']')[0])
#print(pubmed_ids)
inf.close()


#search pubmed id in Pubmed
Entrez.email = 'zd200572@yahoo.com'
handle = Entrez.efetch(db = 'pubmed', id = pubmed_ids, \
		rettype = 'medline', retmode = 'text')
medline_records = Medline.parse(handle)
records = list(medline_records)
authors = []
titles = []
for record in records:
	separator = re.compile('\'')
	author = separator.sub('', str(record['AU']).split('[')[1].split(']')[0])
	authors.append(author)
	titles.append(record['TI'])

#sub pubmedids with number, and author, title on the bottom
outf = open('endnote1.txt', 'w')
i = 0
list = []
for i in range(len(pubmed_ids)):
	list.append(i + 1)
j = 1
for j in range(len(pubmed_ids)):
	#print(line)
	line = '[%s] %s. %s' % (list[j], authors[j], titles[j]) + '\n'
	j += 1
	#print(line)
	outf.write(line)

