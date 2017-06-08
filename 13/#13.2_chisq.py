#13.2_chisq
import rpy2.robjects as ro
r = ro.r
table = r("read.table('smoking_and_lung_cancer.txt', header = TRUE, sep = '\t')")
print(r.names(table))
cont_table = r.table(table[1], table[2])
chitest = r['chisq.test']
print(chitest(cont_table))