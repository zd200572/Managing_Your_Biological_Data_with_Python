'''
from urllib import urlopen
url = urlopen('http://www.uniprot.org/uniprot/P01308.fasta')
doc = url.read()
print(doc)
'''

#urllib2
import requests
url = requests('http://www.uniprot.org/ \
uniprot/P01308.fasta')
doc = url.read()
print(doc)