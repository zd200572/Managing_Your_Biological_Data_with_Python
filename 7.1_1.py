'''
Reformat a four-column to a two-column table.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 7.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

table = [
    ['protein', 'ext1', 'ext2', 'ext3'],
    [0.16, 0.038, 0.044, 0.040],
    [0.33, 0.089, 0.095, 0.091],
    [0.66, 0.184, 0.191, 0.191],
    [1.00, 0.280, 0.292, 0.283],
    [1.32, 0.365, 0.367, 0.365],
    [1.66, 0.441, 0.443, 0.444]
    ]

table = table[1:]

sum0, sum1, sum2, sum3 = 0.0, 0.0, 0.0, 0.0
average = []
for row in table:
    #print(prot, ext)
    sum0 += row[0] 
    sum1 += row[1] 
    sum2 += row[2]
    sum3 += row[3]
average = [sum0 / 6, sum1 / 6, sum2 / 6, sum3 / 6]
table.append(average)

for row in table:
    print(row, '\n')
