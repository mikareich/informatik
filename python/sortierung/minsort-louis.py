import random

def minsort(list):
    if len(list) <= 1:
        return list

    mitte = list[0]
    left = [x for x in list[1:] if x <= mitte]
    right = [x for x in list[1:] if x > mitte]
    return minsort(left) + [mitte] + minsort(right)

def generate_list(length):
    return [random.randint(0, length) for i in range(length)]

print('100 Elemente:' + str(minsort(generate_list(100))))
print('==============================')
print('1000 Elemente:' + str(minsort(generate_list(1000))))
print('==============================')
print('10000 Elemente:' + str(minsort(generate_list(10000))))
print('==============================')
print('100000 Elemente:' + str(minsort(generate_list(100000))))