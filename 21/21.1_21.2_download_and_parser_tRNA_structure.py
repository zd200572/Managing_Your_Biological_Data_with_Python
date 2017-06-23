'''
====================================
 download and parser tRNA structure
====================================
'''

from Bio import PDB
pdb1 = PDB.PDBList()
pdb1.retrieve_pdb_file('1EHZ')
parser = PDB.PDBParser()
structure = parser.get_structure('1EHZ', 'eh/pdb1EHZ.ent')

i = 0
j = 0
k = 0
for model in structure:
	for chain in model:
		#print(chain)
		for  residue in chain:
			i += 1
			#print(i, residue.resname, residue.id[1])
			if residue.id[0][0] == 'H':
				j  += 1					
			for atom in residue:
					#print(atom.name, atom.coord)
					k  += 1
print('resudue number: %s,' % i, 'H-like residue number: %s,' % j, 'total atom number: %s.' % k)