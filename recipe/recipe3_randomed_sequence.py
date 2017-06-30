# create random seuence using dice
import random

nucleotides = list('ACGT')
probs = {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}
assert sum(probs.values()) == 1.0

dna = ''
while len(dna) < 100:
	nuc = random.choice(nucleotides)
	dice = random.random()
	if dice < probs[nuc]:
		dna += nuc
print(dna)