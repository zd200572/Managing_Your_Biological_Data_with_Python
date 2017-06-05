def read_from_file(filename):
    try:
        list = []
        number = None
        while number != 'q':
            number = input('Insert a number: ')
            list.append(float(number))
        return list
    except ValueError:
        print("non-digit included")
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