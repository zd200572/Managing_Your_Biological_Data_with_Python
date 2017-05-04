from math import sqrt
from distance import calc_dist
from parse_pdb import parse_atom_line

def get_ca_atoms(pdb_filename):
    '''returns a list of all C-alpha atoms in chain A'''
    pdb_file = open(pdb_filename.decode(), "r")
    ca_list = []
    for line in pdb_file:
        if line.startswith('ATOM'):
            data = parse_atom_line(line)
            chain, res_type, res_num, atom, x, y, z = data
            if atom == 'CA' and chain == 'A': 
                ca_list.append(data)
    pdb_file.close()
    return ca_list

maxval = 10000
n = ''
ca_atoms = get_ca_atoms("1TLD.pdb")
for i, atom1 in enumerate(ca_atoms):
    # save coordinates in a variable
    name1 = atom1[1] + atom1[2]
    coord1 = atom1[4:]
    # compare atom1 with all other atoms
    for j in range(i+1, len(ca_atoms)):
        atom2 = ca_atoms[j]
        name2 = atom2[1] + atom2[2]
        coord2 = atom2[4:]
        # calculate the distance between atoms
        dist = calc_dist(coord1, coord2)
        name = [name1, name2]
        temp = dist
        if temp < maxval:
            maxval =temp
            n = name
print(n, maxval)