import urllib.request
import re
url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=18235848'
handler = urllib.request.urlopen(url)
html = str(handler.read())
#print(html)
author_regexp = re.compile('<div class="auths">.*?</div>')
author = author_regexp.findall(html)
list = []
if author:
	#print(author)
	au = re.compile(">.*</a>")
	author = str(author)
	match = au.finditer(author)

	if match:
		for i in match:
			#print(i.group().split(','))
			list.append(i.group().split(','))
		#print(list)
for j in list:
	print(j.split('>')[1].split('</a')[0])
'''for i in match:
			if '</a>' in match:
				print(i.split('>')[1].split('</a>') + '\n')'''