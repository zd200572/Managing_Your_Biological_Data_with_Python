from math import sqrt
from struct import unpack
def calc_dist(p1, p2):
   '''returns the distance between two 3D points'''
   tmp = pow(p1[0] - p2[0], 2) + \
      pow(p1[1] - p2[1], 2) + \
     pow(p1[2] - p2[2], 2)
   tmp = sqrt(tmp)
  return tmp
def min_dist(arglist):
  '''
   returns the closest residue pair and their
  CA_CA distance
  '''
   # initialize variables
   maxval = 10000
   residue_pair = ()
   # read arglist starting from the 1st position
   for i in range(len(arglist)):
     # save x,y,z coordinates from the arglist
     # i-element into the atom1 variable
    atom1 = arglist[i][1:]
     # run over all other elements
     for j in range(i + 1, len(arglist)):
      atom2 = arglist[j][1:]
      # calculate the distance
      tmp = calc_dist(atom1, atom2)
      # check if the distance is lower than
      # the previously recorded lowest value
      if tmp < maxval :
        # save the new data
        residue_pair = (arglist[i][0], \
                arglist[j][0])
        maxval = tmp
   return residue_pair, maxval
   def get_list_ca_atoms(pdb_file, chain):
  '''
   returns a list of CA atoms, the residues
   they belong to, and their x,y,z coordinates
   from the input PDB file
  '''
   in_file = open(pdb_file)
   CA_list = []
   pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s6s4s2s3s'
   for line in in_file:
    tmp = unpack(pdb_format, line)
     tmp = [i.strip() for i in tmp]
     # only save CA coords belonging to input chain
     if tmp[0] =="ATOM" and tmp[7] == chain and \
      tmp[3] == "CA":
       # create a tuple (aa_number, x, y, x)
      tmp = (tmp[5]+tmp[8], float(tmp[11]), \
      float(tmp[12]), float(tmp[13]))
       # add the tuple to the list
      CA_list.append(tmp)
  in_file.close()
  return CA_list
# obtain the list of CA atoms of Chain A
CA_list = get_list_ca_atoms("2H8L.pdb", "A")
# identify the closest atoms
res_pair, dist = min_dist(CA_list)
print 'The distance between', res_pair, 'is:', dist