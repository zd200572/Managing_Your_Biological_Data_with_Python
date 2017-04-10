'''

Function for parsing PDB lines.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in chapter 10 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
import struct

pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'

def parse_atom_line(line):
    '''Returns an ATOM line parsed to a tuple '''
    tmp = struct.unpack(pdb_format, line)
    atom = tmp[3].strip()
    res_type = tmp[5].strip()
    res_num = tmp[8].strip()
    chain = tmp[7].strip()
    x = float(tmp[11].strip())
    y = float(tmp[12].strip())
    z = float(tmp[13].strip())
    return chain, res_type, res_num, atom, x, y, z
