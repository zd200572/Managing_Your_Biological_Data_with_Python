'''
====================================
 download and parser tRNA structure
====================================
'''

from Bio import PDB
parser = PDB.PDBParser()
structure = parser.get_structure('1EHZ', 'eh/pdb1EHZ.ent')

atom1 = structure[0]['A'][1]['P']
#atom2 = structure[0]['A'][72]['P']
#atom3 = structure[0]['A'][54]['P']
atom4 = structure[0]['A'][64]['P']
# I think this test means that the two residues using the same P atom, so just use P in one residue, am I right?
distance = atom4 - atom1
print(distance)
