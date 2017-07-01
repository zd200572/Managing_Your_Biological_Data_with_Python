###A Real Case of Structural Superimposition
# Superimpose the catalytic triads of two different serine
# proteases(on CA and N atoms of res H57, D102, and S195 of chain A)
from Bio import PDB
# Retrieve PDB files
pdbl = PDB.PDBList()
pdbl.retrieve_pdb_file("1EQ9")
pdbl.retrieve_pdb_file("1FXY")
# Parse the two structures
from Bio.PDB import PDBParser, Superimposer, PDBIO
parser = PDB.PDBParser()
struct_1 = parser.get_structure("1EQ9", "eq/pdb1eq9.ent")
struct_2 = parser.get_structure("1FXY", "fx/pdb1fxy.ent")
# get the catalytic triads
res_57_struct_1 = struct_1[0]['A'][57]
res_102_struct_1 = struct_1[0]['A'][102]
res_195_struct_1 = struct_1[0]['A'][195]
res_57_struct_2 = struct_2[0]['A'][57]
res_102_struct_2 = struct_2[0]['A'][102]
res_195_struct_2 = struct_2[0]['A'][195]
# Build 2 lists of atoms for calculating a rot.-trans. matrix
# (target and probe).
target = []
backbone_names = ['CA', 'N']
for name in backbone_names:
  target.append(res_57_struct_1[name])
  target.append(res_102_struct_1[name])
  target.append(res_195_struct_1[name])
probe = []
for name in backbone_names:
  probe.append(res_57_struct_2[name])
  probe.append(res_102_struct_2[name])
  probe.append(res_195_struct_2[name])
# Check whether target and probe lists are equal in size.
# This is needed for calculating a rot.-trans. matrix
assert len(target) == len(probe)
# Calculate the rotation-translation matrix.
sup = Superimposer()
sup.set_atoms(target, probe)
# Apply the matrix. Remember that it can be applied only on
# lists of atoms.
struct_2_atoms = [at for at in struct_2.get_atoms()]
sup.apply(struct_2_atoms)
# Write the rotation-translated structure
out = PDBIO()
out.set_structure(struct_2)
out.save('1FXY-superimposed.pdb')