import math
class DendrictLengths:
	def __init__(self, file_name):
		self.file_name = file_name
	
	
	def get_length(self):
		length = []
		inf = open(self.file_name)
		for line in inf:
			length.append(line.strip()) 
		return length

	def __repr__(self):
		return 'Data set with %s dendritic lengths' % len(self.get_length())
		#return '%s' % self.get_length() #test_this_program

	def get_average(self):
		sum = 0.0
		average = 0.0
		for a in self.get_length():
			sum += float(a)
		average = sum / len(self.get_length())
		return average

	def get_sttddev(self):
		total = 0.0
		for a in self.get_length():
			total += (float(a) - self.get_average()) ** 2
		sttddev = math.sqrt(total / len(self.get_length()))
		return sttddev