import random
from timer import Timer

timer = Timer()



def bubblesort(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - i - 1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

def generiereListe(laenge):
    return [random.randint(0, laenge) for i in range(laenge)]

timer.startTimer()
print('Elemente: \033[93m 10000 \033[92m\n' + str(bubblesort(generiereListe(10000))))
print('\033[0m Passed time: \033[93m', timer.endTimer())