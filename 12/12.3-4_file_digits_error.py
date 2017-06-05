def read_from_file(filename):
    try:
        inf = open(filename, 'r')
        list = []
        for line in inf:
            try:
                list.append(float(line.strip()))
                    #print(list)
            except ValueError:
                print("non-digit included")
                #print(list)
        print(list)
        return list
    except IOError:
            print('FIle is not exist!')
            raise SystemExit

def clal_average(list):
    sum = 0.0
    average = 0.0
    for a in list:
        try:
            sum += a
            average = sum / len(list)
        except ValueError:
            print("non-digit included")
    print(average)
    return average

def cal_sttdev(list, average):
    sttdev = 0.0
    total = 0.0
    for a in list:
        total += (a - average) ** 2
    sttdev = total / len(list)
    print(sttdev)
    return sttdev

a = read_from_file('2.txt')
b = clal_average(a)
cal_sttdev(a, b)