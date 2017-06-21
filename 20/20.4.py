'''
===================================
searching protein by keywords
===================================
'''
from Bio import Entrez
from Bio import SeqIO
import time
keyword = 'bacteriorhodopsin'
#search proteins in Entrez
Entrez.email = 'zhaojiadong@sygene.cn'
handle = Entrez.esearch(db = 'protein', term = keyword)
 
 
record = Entrez.read(handle)
#protein_ids = record['IdList']
id_list = record['IdList'][:20]
id_list = ','.join(id_list)
#print(id_list)
#retrive sequence from Entrez
outf = open('protein_searching.gb', 'w')
handle = Entrez.efetch(db = 'protein', id = id_list, \
         rettype = 'gb', retmode = 'xml')
records = Entrez.parse(handle)
 
 
#for record in records:
#        SeqIO.write(record, outf, 'genbank')###这样报错
i = 0
for record in records:
        i += 1
        outf.write('%s\n' % i)
        #print(record)
        for a in record.keys():
                outf.write('%s:%s' % (a, record[a]) + '\n')
outf.close()