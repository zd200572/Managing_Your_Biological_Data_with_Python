import os
filelist = []
filelist = os.listdir('/home/zd200572')
n = len(filelist)
print('sample count:', n)
###under here is my program to make a hard program to count the file number, but an error always reported, I cannot solve it now!

for x in filelist:
	if os.path.exists('/home/zd200572/' + x):
		if '.' or ' ' in x:
			if x.split('.')[0] != '':
				n += 1
			#else:
		#		n += len(os.listdir(x))
		else:
				n += len(os.listdir('/home/zd200572/' + x))
print("The number of all files in user dir is %s", n)
