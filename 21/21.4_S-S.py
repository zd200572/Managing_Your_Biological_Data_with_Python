'''
==========================
calculate the S-S
==========================
'''
from Bio import PDB
from Bio.PDB import Vector
pdb1 = PDB.PDBList()
pdb1.retrieve_pdb_file('1C9X')
parser = PDB.PDBParser()
structure = parser.get_structure('1C9X', 'c9/pdb1C9X.ent')
Atom1 = []
Atom2 = []
resid = []
list = []
dict = {}
for model in structure:
	for chain in model:
		#print(chain)
		for  residue in chain:
			#print(i, residue.resname, residue.id[1])
			if residue.resname == 'CYS':
				list.append(residue.id[1])
				for atom in residue: 
					if atom.name == 'CB':
						Atom1.append(atom)
					elif atom.name == 'SG':
						Atom2.append(atom)

i = 0						
for i in range(len(Atom1)):
	resid.append([Atom1[i], Atom2[i]])
	i += 1
j = 0
for j in range(len(list)):
	dict[list[j]] = resid[j]
	j += 1

#print(atom1, atom1)
					
for resi in resid:
	for res in resid:
		atom1 = resi[0]
		atom2 = resi[1]
		atom3 = res[1]
		atom4 = res[0]
		distance = atom3 - atom2
		v1 = atom1.get_vector()
		v2 = atom2.get_vector()
		v3 = atom3.get_vector()
		v4 = atom4.get_vector()
		vector = Vector.calc_dihedral(v1, v2, v3, v4)
		if 85 < vector < 95 :
			if 1.9 < distance < 2.1:
				print('S-S:')
