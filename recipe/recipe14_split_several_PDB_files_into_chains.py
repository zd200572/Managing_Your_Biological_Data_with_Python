###split several PDB files into chains
import struct
import os.path
filename = '1TLD.pdb'
#def split_chains(filename):
in_file = open(filename)
pdb_id = filename.split('.')[0]
pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s6s4s2s3s'
chain_old = '@'
for line in in_file:
   print(line)
   if line[0:4] == "ATOM":
   	col = struct.unpack(pdb_format, line)
   	chain = col[7].strip()
   	if chain != chain_old:
   		if os.path.exists(pdb_id+chain_old+'.pdb'):
   			chain_file.close()
   			print("closed:", pdb_id+chain_old+'.pdb')
   			chain_file = open(pdb_id+chain+'.pdb','w')
   			chain_file.write(line)
   			chain_old = chain
   		else:
   			chain_file.write(line)
   	chain_file.close()
  #print("closed:", pdb_id+chain_old+'.pdb')

#split_chains('1TLD.pdb')