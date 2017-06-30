#REVERSE_AND_RANDOMLY SEQUENCES
seq = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
seq_list = list(seq)
seq_list.reverse()
rev_seq = ''.join(seq_list)
print(rev_seq)

#method2
rev = ''
for s in reversed(seq):
	rev += s
print(rev)

#random_sequence
import random
ran_seq = ''.join(random.sample(seq, len(seq)))
print(ran_seq)

#random.choice method
ran = ''.join([random.choice(seq) \
	 for x in range(len(seq))])
print(ran)

#shuffle the same composition
data = list(seq)
random.shuffle(data)
shuffled_seq = ''.join(data)
print(shuffled_seq)