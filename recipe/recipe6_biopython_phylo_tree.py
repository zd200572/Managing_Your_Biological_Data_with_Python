#biopython phylo tree
from Bio import Phylo
tree = Phylo.read('newick_small.txt', 'newick')
Phylo.draw_ascii(tree)
a = tree.find_clades(name = 'Hadrurus_virgo').next()
b = tree.find_clades(name = 'Coleonyx_godlewskii').next()
ancestor = tree.common(a, b)
print(tree.ditance(a, b))
print(tree.distance(ancestor, a))
print(tree.distance(ancestor, b))