liste=[101001, 11,9,4,3,0,6,1, -1, -0.00001, 23*10]
def sortierenI():
    laenge=len(liste)-1
    Speicher=[]
    Runde=0
    while Runde != len(liste):
        index=0
        while index!=laenge:
            if liste[index]>liste[index+1]:
                Speicher = liste[index]
                liste[index]=liste[index+1]
                liste[index+1]=Speicher
                print(liste)
            elif len(liste)>index+2 and liste[index]>liste[index+2]:
                Speicher = liste[index]
                liste[index]=liste[index+2]
                liste[index+2]=Speicher
                print(liste)
            elif len(liste)>index+3 and liste[index]>liste[index+3]:
                Speicher = liste[index]
                liste[index]=liste[index+3]
                liste[index+3]=Speicher
                print(liste)
            elif len(liste)>index+4 and liste[index]>liste[index+4]:
                Speicher = liste[index]
                liste[index]=liste[index+4]
                liste[index+4]=Speicher
                print(liste)
            elif len(liste)>index+5 and liste[index]>liste[index+5]:
                Speicher = liste[index]
                liste[index]=liste[index+5]
                liste[index+5]=Speicher
            index+=1
        Runde+=1
    print(liste) 
sortierenI()

