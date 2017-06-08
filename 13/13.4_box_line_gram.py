#13.4_box_line_gram.py
import rpy2.robjects as ro
import time
r = ro.r
table = r("read.table('boxplot.csv', sep = ',')")
r.boxplot(table[1], table[3], table[4], col = 'orange', xlab = 'x', \
	main = 'Boxplot', ylab = 'y')
time.sleep(10)