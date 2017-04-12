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

table_nested_dict = []
n = 0
key = table[0]
for row in table[1:]:
    n += 1
    list = [{key[0]: row[0]}, {key[1]: row[1]}, {key[2]: row[2]}, {key[3]: row[3]}]
    table_nested_dict.append(list)
for row in table_nested_dict:
    print(row, '\n')

