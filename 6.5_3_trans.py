tracking = open('transcripts.tracking', 'r')
ou_file = open('transcripts-filtered_3.tracking', 'w')
for track in tracking:
	columns = track.strip().split('\t')
	wildtype = columns[4:7].count('-')
	treatment = columns[7:10].count('-')
	if wildtype == 0 or treatment == 0:
		ou_file.write(track)
tracking.close()
ou_file.close()