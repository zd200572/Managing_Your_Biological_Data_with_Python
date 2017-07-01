###Calculating RNA Base Pairs from a 3D Structure
#use pycogent
from cogent.app.rnaview import RnaView
from cogent.parse.rnaview import RnaviewParser
rna_prog
result = rna_prog('1ehz.pdb')
bpairs = result['base_pairs']
errors = result['StdErr'].read()
stdout = result['StdOut'].read()
bp_dict = RnaviewParser(bpairs)
print 'INFORMATION:'
sys.stderr.write(errors)
print stdout
print 'BASE PAIRS:'
for key in bp_dict:
     print key, bp_dict[key]
# because python2 failed in sevral recipes, 
#espically in pycogent, so just keep the format of python2

#use moderna
from moderna import *
struc = load_model('1ehz.pdb', 'A')
for bp in get_base_pairs(struc):
   print(bp)