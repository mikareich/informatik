#%%

def caesar():
    """
    Verschlüsselung mit dem Caesar-Verschlüsselungsverfahren.
    """
    # Eingabe
    text = input("Text: ")
    verschiebung = int(input("Verschiebung: "))
    # Verschlüsselung
    verschluesselt = ""
    for zeichen in text:
        if zeichen.isalpha():
            if zeichen.isupper():
                verschluesselt += chr((ord(zeichen) -
                                      ord('A') + verschiebung) % 26 + ord('A'))
            else:
                verschluesselt += chr((ord(zeichen) -
                                      ord('a') + verschiebung) % 26 + ord('a'))
        else:
            verschluesselt += zeichen
    # Ausgabe
    print("Verschlüsselt:", verschluesselt)


caesar()
