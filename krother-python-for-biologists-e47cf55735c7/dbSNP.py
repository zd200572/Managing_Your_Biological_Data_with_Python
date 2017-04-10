###dbSNP
import re,urllib.request
idlist = ['6560']

for id in idlist:
	url = 'http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?locusId=%s'%id
	f = urllib.request.urlopen(url).read()
	f = f.decode('utf-8')#python3
	res = re.findall('spacing = 0">(\d*)</a></td><td.*?currpage = 1">(\d*)\<\a><\td><td.*?(rs\d*) <\a></td><td', f,re.S)
	print('Chr.position', 'mRNA pos', 'dbSNP cluster id')
	for i in res:
		print(i)
        