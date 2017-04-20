import re
inf = open('Moby_Dick.txt', 'r')
dicts = {}
max = 0
words = set()
article = []
i = 0
for line in inf:
	regexp = re.compile('[a-zA-Z]+')
	match = regexp.findall(line)
	if match:
		for word in match:
			words.add(word)
			article.append(word)

#print(words)
#print(article)
for a in article:
	#regex = re.compile('[Ww][Hh][Aa][Ll][Ee]')
	regex = re.compile('[Cc][Aa][Pp][Tt][Aa][Ii][Nn]')
	matchs = regex.match(a)
	if matchs:
		#print(matchs)
		#print(matchs.group())
		i +=1
print(i)
	
for word in words:
	dicts[word] = 0
	for x in article:
		regexp = re.compile('[a-zA-Z]+')
		match = regexp.findall(x)
		if match == word:
			dicts[word] += 1

print(dicts)