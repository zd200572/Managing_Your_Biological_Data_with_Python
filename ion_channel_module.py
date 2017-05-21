class ion_channel:	#11.4_make a alone module

	def __init__(self, protein_name, PDB_mark, a, b):
		self.protein_name = protein_name
		self.PDB_mark = PDB_mark
		self.a = a
		self.b = b

	def __repr__(self):
		return '%s, %s, %s, %s\n' % (self.protein_name, self.PDB_mark, self.a, self.b)