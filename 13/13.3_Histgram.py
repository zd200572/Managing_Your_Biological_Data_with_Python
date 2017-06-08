#13.3_Histgram.py
'''beacuse importr can not work in python3, 
so I just have a try of hist function.
That's it!
'''
import time
import rpy2.robjects as ro
r = ro.r
table = r("read.table('histgram.csv', sep = ',')")
#grdevices = importr('grDevices')
#grdevices.pdf(file = 'Histgram.pdf', width = 512, height = 512)
r.hist(table[1], xlab = 'x', main = 'Didtribution of values')
r.box()
time.sleep(10)

