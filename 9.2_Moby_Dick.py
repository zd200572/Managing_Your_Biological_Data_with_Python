import re
inf = open('Moby_Dick.txt', 'r')
dict = {}
max = 0
words = set()
for line in inf:
	regex = re.compile('[a-zA-Z]+')
	results = regex.search(line)
	words.add(results.split('\'')[1])
	print(results)