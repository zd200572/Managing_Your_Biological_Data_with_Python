<<<<<<< HEAD
#14.2
'''inf = open("first.py", 'r')
#print(inf)
a = inf.read()
print(float(a)**2)
'''
#14.3
def second(filename):
	inf = open(filename, 'r')
	#print(inf)
	a = inf.read()
	print(float(a)**2)
=======
#second.py
inf = open('first.py', 'r')
s = 0.0
for line in inf:
	s = line.strip()
print(s)
print(int(s)**2)
>>>>>>> 1826422aa18a04af5ee2b90666e6b78299f01da3
