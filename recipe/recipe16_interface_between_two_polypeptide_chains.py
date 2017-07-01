#the same as 10.5 

#without Biopython
import struct
from math import sqrt
def calcDist(p1, p2):
    tmp = pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2) + \
      pow(p1[2]-p2[2], 2)
   tmp = sqrt(tmp)
   return tmp
def getInterface(filename, chain1, chain2):
   in_file = open(filename)
   pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s6s4s2s3s'
   A, B, result = [], [], []
   for line in in_file:
    if line[0:4] == "ATOM":
      col = struct.unpack(pdb_format, line)
      a_name = col[3].strip()
      chain = col[7].strip()
      amino_numer = col[5].strip() + col[8].strip()
      x = col[11].strip()
      y = col[12].strip()
      z = col[13].strip()
      if a_name == "CA":
        if chain == chain1:
          A.append((amino_numer, x, y, z))
        if chain == chain2:
          B.append((amino_numer, x, y, z))
   #calculate pairs of atoms with distance < 6
   for i in range(len(A)):
    for j in range(len(B)):
      v1 = (float(A[i][1]), float(A[i][2]), float(A[i][3]))
      v2 = (float(B[j][1]), float(B[j][2]), float(B[j][3]))
      tmp = calcDist(v1, v2)
      if tmp < 6:
      result.append((A[i][0], B[j][0], tmp))
  return result
print(getInterface("2H8L.pdb", "A", "B"))

#with Biopython
from Bio import PDB
parser = PDB.PDBParser()
s = parser.get_structure("2H8L","2H8L.pdb")
first_model = s[0]
chain_A = first_model["A"]
chain_B = first_model["B"]
for res1 in chain_A:
for res2 in chain_B:
d = res1["CA"]-res2["CA"]
if d <= 6.0:
print(res1.resname,res1.get_id()[1], res2.resname,\
	res2.get_id()[1], d)