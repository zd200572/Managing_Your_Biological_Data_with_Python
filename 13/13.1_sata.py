import rpy2.robjects as ro
r = ro.r
table = r("read.table('test.csv', sep = ',')")
print(table)
m = r.mean(table[0], trim = 0, na_rm = 'False')
sdev = r.sd(table[0], na_rm = 'FALSE')
value = 0.01844
zscore = (m[0] - value) / sdev[0]
print(zscore)
x = r.abs(zscore)
pvalue = r.pnorm(-x[0])
print(pvalue[0])