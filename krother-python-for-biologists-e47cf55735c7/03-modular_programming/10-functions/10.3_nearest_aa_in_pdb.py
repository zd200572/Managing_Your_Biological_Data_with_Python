#10.3_nearest_aa
from math import sqrt
from struct import unpack

def calc_dist(p1, p2):
    '''returns the distance between two 3D points'''
    temp = pow(p1[0] - p1[0], 2) + \
    pow(p1[1] - p2[1], 2) + \
    pow(p1[2] - p2[2], 2)
    temp = sqrt(temp)
    return temp
def min_dist(arglist):
    '''
    returns the closest residue pair and their 
    CA_CA distance
    '''
    #initialize variables
    maxval = 10000
    resdue_pair = ()
    #read arglist starting from the 1st position
    for i in range(len(arglist)):
        #save x,y,z coordinates from the rglist
        #i-element into the atom1 variable
        atom1 = arglist[i][1:]
        #run over all other elements
        for j in range(i+1, len(arglist)):
            atom2 = arglist[j][1:]
            #calculate the distance
            temp = calc_dist(atom1, atom2)
            #check if the distance is lower than 
            #the previously recored lowest value
            if temp < maxval:
                #save the new data
                residue_pair = (arglist[i][0], \
                                            arglist[j][0])
                maxval = temp 
    return residue_pair, maxval
    
def get_list_ca_atoms(pdb_file, chain):
    '''
    returns a list of CA atoms, the residues
    they belong to, and their x, y, z coordinates
    from the input PDB file
    '''
    in_file = open(pdb_file)
    CA_list = []
    pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'
    for line in in_file:
        temp = unpack(pdb_format, line)
        temp = [i.strip() for i in temp]
        #only save CA coords belonged to input chain
        if temp[0] == 'ATOM' and temp[7]  == chain and \
            temp[3] == 'CA':
            #creat a tuple (aa_number, x, y, z)
            temp = (temp[5] + temp[8], float(temp[11]), \
            float(temp[12]), float(temp[13]))
            #add the tuple to the list
            CA_list.append(temp)
    in_file.close()
    return CA_list
    
#obtain the list of CA atoms of chain A
CA_list = get_list_ca_atoms('3G5U.pdb', 'A')
#identify the closest atoms
res_pair, dist = min_dist(CA_list)
print('the distance between', res_pair, 'is:', dist)
