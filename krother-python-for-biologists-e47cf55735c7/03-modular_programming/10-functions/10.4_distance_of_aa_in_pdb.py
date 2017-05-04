import struct
from math import sqrt

def calDist(p1, p2):
	temp = pow(p1[0] - p1[0], 2) + \
	pow(p1[1] - p2[1], 2) + \
	pow(p1[2] - p2[2], 2)
	temp = sqrt(temp)
	return temp

def getInterface(filename, chain1, chain2):
	in_file = open(filename)
	pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'
	A, B, result = [], [], []
	for line in in_file:
		if line[0:4] == 'ATOM':
			col = struct.unpack(pdb_format, line)
			a_name = col[3].strip()
			chain = col[7].strip()
			amino_number = col[5].strip() + col[8].strip()
			x = col[11].strip()
			y = col[12].strip()
			z = col[13].strip()
			if a_name == 'CA':
				if chain == chain1:
					A.append((amino_number, x, y, z))
				if chain == chain2:
					B.append((amino_number, x, y, z))
			#calculate pairs of atoms with distance < 6
	for i in range(len(A)):
		for j in range(len(B)):
			v1 = (float(A[i][1]), float(A[i][2]), float(A[i][3]))
			v2 = (float(B[j][1]), float(B[j][2]), float(B[j][3]))
			temp = calDist(v1, v2)
			if temp < 6:
				result.append((A[i][0], B[j][0], temp))
	return result

print(getInterface('3G5U.pdb', 'A', 'B'))