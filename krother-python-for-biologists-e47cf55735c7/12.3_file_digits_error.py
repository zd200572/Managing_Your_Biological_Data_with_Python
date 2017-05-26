def read_from_file(filename):
    inf = open(filename, 'r')
    list = []
    for line in inf:
        list.append(float(line.strip()))
    return list

def clal_average(list):
    sum = 0.0
    average = 0.0
    for a in list:
        sum += a
    average = sum / len(list)
    return average

def cal_sttdev(list):
    sttdev = 0.0
    total = 0.0
    for a in list:
        total += (a - average) ** 2
    sttdev = total / len(list)
    return sttdev

read_from_file('1.txt')
clal_average(list)
cal_sttdev(list)