import re
author = '<a href="/pubmed/?term=Inglese%20J%5BAuthor%5D&amp;cauthor=true&amp;cauthor_uid=18235848">Inglese J</a>'
au = re.compile(">.*</a>")
match = au.search(author)
if match:
		print(match.group().split('>')[1].split('</a')[0])