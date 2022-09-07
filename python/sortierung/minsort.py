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
print('Elemente: \033[93m 10000 \033[92m\n' + str(minsort(generate_list(100000))))
print('\033[0m Passed time: \033[93m',timer.endTimer())