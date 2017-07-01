###RNA 3D Homology Modeling with ModeRNA
from moderna import *
ehz = load_model('1ehz.ent', 'A')
clean_structure(ehz)
print(get_sequence(ehz))
print(get_secstruc(ehz))
m = create_model()
copy_some_residues(ehz['1':'15'], m)
write_model(m, '1ehz_15r.ent')
temp = load_template('1ehz_15r.ent')
ali = load_alignment('''> model sequence
ACUGUGAYUA[UACCU#PG
> template: first 15 bases from 1ehz
GCGGA--UUUALCUCAG''')
model = create_model(temp, ali)
print(get_sequence(model))