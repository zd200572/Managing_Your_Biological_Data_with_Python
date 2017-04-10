#coding=utf-8
genbank_file = open("C:\Users\shenyou\Desktop\\bioinfo\krother-python-for-biologists-e47cf55735c7\02-data_management\04-parsing_dataAY810830.gb", 'r',#coding=utf-8)
output_file = open("AY810830.fasta","w")

fla = False
for line in genbank_file:
    if line[0:9] == 'ACCESSION':
        accession = line.split()[1].strip()
        output_file.write('>' + accession + '\n')
    if line[0:6] == 'ORIGIN': 
        fla = True
    elif fla:
        fields = line.split()
        if fields != []:
            seq = ''.join(fields[1:])
            output_file.write(seq.upper() + '\n')
            
genbank_file.close()
output_file.close()