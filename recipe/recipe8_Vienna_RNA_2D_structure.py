class RNAStructure:
    def __init__(self, vienna):
        lines = vienna.split('\n')
        self.name = lines[0].strip()
        self.sequence = lines[1].strip()
        self.basepairs = \
            sorted(self.parse_basepairs(lines[2].strip()))
    def parse_basepairs(self, dotbracket):
        stack = []
        for i, char in enumerate(dotbracket):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
        yield j, i
vienna = '''> two hairpin loops
AAACCCCGUUUCGGGGAACCACCA
((((...)))).((((..)).)).
'''
rna = RNAStructure(vienna)
print(rna.name)
print(rna.sequence)
print(rna.basepairs)
for base1, base2 in rna.basepairs:
   print('(%i, %i)'%(base1, base2))