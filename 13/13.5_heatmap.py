import rpy2.robjects as ro
import time
r = ro.r
y= r.seq(1, 10000)
matrix = r.matrix(y, ncol = 66)
r.heatmap(matrix, cexRow=0.5) #because unkown of this function, so just the easiest one,just for fun
time.sleep(10)