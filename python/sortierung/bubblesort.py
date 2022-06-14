import random

def bubblesort(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - i - 1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

def generiereListe(laenge):
    return [random.randint(0, laenge) for i in range(laenge)]

print('100 Elemente:' + str(bubblesort(generiereListe(100))))
print('==============================')
print('1000 Elemente:' + str(bubblesort(generiereListe(1000))))
print('==============================')
print('10000 Elemente:' + str(bubblesort(generiereListe(10000))))
print('==============================')
print('100000 Elemente:' + str(bubblesort(generiereListe(100000))))