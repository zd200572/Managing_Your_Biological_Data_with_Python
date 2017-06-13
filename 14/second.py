#second.py
inf = open('first.py', 'r')
s = 0.0
for line in inf:
	s = line.strip()
print(s)
print(int(s)**2)