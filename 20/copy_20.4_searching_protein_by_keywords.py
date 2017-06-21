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
#out_handle = open('handle.txt', "w")
#out_handle.write(handle.read())
#out_handle.close()
#record = SeqIO.read('handle.txt', "genbank")

record = Entrez.read(handle)
#protein_ids = record['IdList']
id_list = record['IdList'][:20]


id_list = ','.join(id_list)
#print(id_list)
#retrive sequence from Entrez
outf = open('protein_searching.gb', 'w')
#time.sleep(5)
handle = Entrez.efetch(db = 'protein', id = id_list,\
	rettype = 'gb', retmode = 'xml')
record = Entrez.parse(handle)
print(handle)
time.sleep(10)
#rec = list(records)
SeqIO.write(record, outf, 'genbank')

outf.close()

