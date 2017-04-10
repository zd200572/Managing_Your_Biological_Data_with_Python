###gbk to fasta
#coding=utf-8
inf = open('C:\\Users\\shenyou\\Desktop\\bioinfo\\p53.gb','r')
outf = open('gbkout.fasta', 'w')
flag = 0
for line in inf:
	if line[:9] == 'ACCESSION':
		ac = line.split()[1].strip()
		outf.write('>' + ac + '\n')
	if line[:2] == '//':
		flag = 0
	if line[:6] == 'ORIGIN':
		flag = 1
	elif flag == 1:
		fields = line.split()
		#print(fields)
		if fields != []:
			seq = ''.join(fields[1:])
			outf.write(seq.upper() + '\n')
		
inf.close()
outf.close()
