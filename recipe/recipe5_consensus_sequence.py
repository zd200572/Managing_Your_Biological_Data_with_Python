'''
=====================
编程秘笈5
=====================
'''
seqs = [
		'ATCCAGCT',
		'GGGCAACT',
		'ATGGATCT',
		'AAGCAACC',
		'TTGGAACT',
		'ATGCCATT',
		'ATGGCACT'
		]
n = len(seqs[0])
#print(n)
profile = {'A':[0]*n, 'C':[0]*n,'G':[0]*n, 'T':[0]*n }

for seq in seqs:
	for i, char in enumerate(seq):
		profile[char][i] += 1

consensus1 = ''
consensus2 = ''
consensus = ''
for i in range(n):
	col = [(profile[nt][i], nt) for nt in 'ATCG']
	col = sorted(col)
	#print(col)
	second = max(col[1:])[0]
	consensus1 += max(col)[1]
	consensus2 += max(col[:3])[1]

for a in range(len(consensus1)):
	consensus += '[' + consensus1[a] + consensus2[a] + ']'
	a += 1

print(consensus)