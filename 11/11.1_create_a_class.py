'''#11.1 class ion_channel:

	def __init__(self, protein_name, PDB_mark, a, b):
		self.protein_name = protein_name
		self.PDB_mark = PDB_mark
		self.a = a
		self.b = b
'''
#11.2	def __repr__(self):
#		return '%s, %s, %s, %s\n' % (self.protein_name, self.PDB_mark, self.a, self.b)
'''#11.3	def format_list(self):
		li = ''
		li = self.protein_name + '\t' + self.PDB_mark + '\t' + self.a + '\t' + self.b + '\n'
		return li
	def __repr__(self):
		return self.format_list()
'''

from ion_channel_module import ion_channel

P1 = ion_channel('P', 'ljvm', '354.2', '351.7')
P2 = ion_channel('M', 'lmsl', '359.2', '345.7')
P3 = ion_channel('C', 'lkpl', '361.3', '344.6')
print(P1, P2, P3)

'''	table_of_ion_channel = [[protein_name, PDB_mark, a, b],
							[P, ljvm, 354.2, 351.7],
							[M, lmsl, 359.2, 345.7],
							[C, lkpl, 361.3, 344.6]]
'''	
