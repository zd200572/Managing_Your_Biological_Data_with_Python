inf1 = open('file1.txt', 'r')
inf2 = open('file2.txt', 'r')
list1 = []
list2 = []
i = 0
j = 0
k = 0
l = 0
list1 = inf1.readlines()
print(list1)
print('\n')
list2 = inf2.readlines()
print(list2)
print('\n')
for a in list1:
	l += 1
	print(l)
	if a in list2:
		i += 1
		print('line in both:', a)
	elif a not in list2:
		j += 1
		print('line only in file1: ', a)
for b in list2:
	if b not in list1:
		k += 1
		print('line only in file2: ', b)

print('lines in both: ', i)
print('lines only in file1: ', j)
print('lines only in file2: ', k)