import re
inf = open('Moby_Dick.txt', 'r')
dicts = {}
max = 0
words = set()
article = open('article.txt', 'w')
article1 = open('article.txt', 'r')
i = 0
ab = []
for line in inf:
	regexp = re.compile('[a-zA-Z]+')
	match = regexp.findall(line)
	if match:
		for word in match:
			words.add(word)
			ab.append(word)
			article.write(' '.join(word))
		article.write('\n')

#print(words)
#print(article)
for a in ab:
	regex = re.compile('[Ww][Hh][Aa][Ll][Ee]')
	#regex = re.compile('[Cc][Aa][Pp][Tt][Aa][Ii][Nn]')
	#regex = re.compile('[i][s]')
	matchs = regex.match(a)
	if matchs:
		#print(matchs)
		#print(matchs.group())
		i +=1
print(i)

'''for word in words:
	dicts[word] = 0
	for line in article1:
		for x in line:
			if x == word:
				dicts[word] += 1

print(dicts)'''