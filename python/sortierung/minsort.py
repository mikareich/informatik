import random
from timer import Timer

timer = Timer()


def minsort(list):
    if len(list) <= 1:
        return list

    mitte = list[0]
    left = [x for x in list[1:] if x <= mitte]
    right = [x for x in list[1:] if x > mitte]
    return minsort(left) + [mitte] + minsort(right)

def generate_list(length):
    return [random.randint(0, length) for i in range(length)]

timer.startTimer()
print('100000 Elemente:' + str(minsort(generate_list(10000))))
print(timer.endTimer())