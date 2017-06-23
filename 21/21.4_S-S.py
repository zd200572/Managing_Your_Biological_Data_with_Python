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

CB = []
SG = []
for model in structure:
	for chain in model:
		#print(chain)
		for  residue in chain:
			#print(i, residue.resname, residue.id[1])
			if residue.resname == 'CYS':
				for atom in residue: 
					if atom.name == 'CB':
						CB.append(atom)
					elif atom.name == 'SG':
						SG.append(atom)
					
print(CB, SG)
					
'''
v1 = atom1.get_vector()
v2 = atom2.get_vector()
v3 = atom3.get_vector()
v4 = atom4.get_vector()
'''