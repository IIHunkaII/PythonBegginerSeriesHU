
# list (mutable) jelentése = lista (modosithato)


lista1 = [] # egy ures lista

print (lista1) # printeljuk az ures listat a konzolra

lista1.append(101)          # append = csatolni valamit
lista1.append(100)
lista1.append(102)          # hozzaadunk number-öket a listához
lista1.append(140)
lista1.append(500)

print (lista1)              # megnezzük mit tartalmaz

lista1.append('Eniko')
lista1.append('Adam')       # hozzaadtam stringeket
lista1.append('Eniko')

print(lista1)               # ujra megnezem h most összesen mit tartalmaz a lista 1

lista1.remove('Eniko')      # kiveszem őt mert ketszer szerepel (remove-al)

print(lista1)               # kiprintelem h lathato legyen a különbseg

#lista1.clear()              # így törlöm a listában lévő objektumokat - HOGY NE ZAVARJON KOMMENTBE RAKTAM!

#print(lista1)               # ismet leirom h lathato legyen a kulonbseg - HOGY NE ZAVARJON KOMMENTBE RAKTAM!

lista1.insert(5, 'Bozsi')    # igy rakok be objektumokat, a szam a sorrendet jelenti, hogy hova keruljon a cucc

print(lista1)                # ismet kiprintelem

lista1.reverse()             # ertelem szeruen megforditja a listat

print(lista1)                # ismet kiprintelem

lista2 = [15, 8, 78, 23, 1, 65, 184] # egy új lista

lista2.sort()                      # szortírozza növekvő sorrenben (számot számmal, betűt betűvel lehet csak szortirozni

print(lista2)                      # tudod hogy miért...

lista3 = ['Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi']  # string mappa

lista3.sort()                      # ABC sorrendbe rakja

print(lista3)                      # ...

alpha = ['f', 'n', 'u', 'd', 's', 'a', 'g', 'w', 'i', 'j', 'z', 'x', 'm', 'b', 'o',
         'r', 'q', 'p', 'e', 't', 'c', 'v', 'h', 'l', 'y', 'k']      # az angol abc listaja, normalisan elnevezve,
                                                                     # és keverve

alpha.sort()                       # sorrendbe rakás...

print(alpha)                       # ...


print(len(alpha))                  # ezzel tudod meg h hány karaktert használtál fel egy listához LEN=LENGTH

print(len(lista1))                 # ugyan az mint a felso ( az 5db szám és a 3 név)

# Updated: 2020.07.28
# Made on 2020.07.28 By Robi