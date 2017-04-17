inf = open('Homo.fasta', 'r')

for line in inf:
    if line.startswith('>') and flag ==1:
        