values = [0, 3, 10, 6]

def same_by(characteristic, objects):
    list1 = [characteristic(x) for x in objects]
    for i in range(len(objects) - 1):
        if characteristic(list1[i]) != characteristic(list1[i+1]):
            return False
    return True


if same_by(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')