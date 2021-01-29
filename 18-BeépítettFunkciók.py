
# BEÉPÍTETT FÜGGVÉNYEK

'''
 DEFINÍCIÓ : abs(x)

    Return the absolute value of a number. The argument may be an integer or a floating point number.
    If the argument is a complex number, its magnitude is returned.
    If x defines __abs__(), abs(x) returns x.__abs__().
'''

# GYAKORLATBAN

print(abs(-78))

# MAGYARUL

# -78 abszolút értéke 78, ezert az eredmeny 78!
# abs abszolut

#-----------------------------------------------------------------------------------------------------------------------

'''
DEFINICIO : enumerate
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. 
The __next__() method of the iterator returned by enumerate() returns a tuple containing a count 
(from start which defaults to 0) and the values obtained from iterating over iterable.
'''

# GYAKORLATBAN


nevek1 = ['Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi', 'Zsuzsi', 'Evi']

for index, nev in enumerate(nevek1, start=1):
    print(index, nev)

# MAGYARUL

# sorrendbe teszem a stringeket (SZÁMOT RAK ELÉ NÖVEKVŐ SORRENDBE)
# startal megadhatom hogy honnan induljon a számolás

#----------------------------------------------------------------------------------------------------------------------

'''
DEFINICIO : float
Return a floating point number constructed from a number or string x.
'''

# GYAKORLATBAN

print(float('10'))

# MAGYARUL

# átváltja lebegő számmá, látható a tizedes vesszo miatt
# akkor hasznos hogyha ugy adok meg neki szamot mint egy string, ha kesobb muveletet akarok vegezni akkor hasznalom
# értelmét még nem látom

#-----------------------------------------------------------------------------------------------------------------------

'''
DEFINICIO : hex 
Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. 
If x is not a Python int object, it has to define an __index__() method that returns an integer. 
'''

# GYAKORLATBAN

print (hex(125))

# MAGYARUL

# jelentése hexadecionális számok
# visszaadja egy számnak a hexadecimális értékét
# nem tudom még mi ez

#-----------------------------------------------------------------------------------------------------------------------


# kisebb fogalmak

'''
isinstance - viszzaad egy true-t vagy egy false-t, aszerint hogy a string tipusu-e vagy sem ( még nem értem )
isinstance forditasa: példa = instance in = valamiben 
megnézi a függvényt EZT MÉG SZINTE ALIG ÉRTEM 
függvények1-es projekt 15. vonalában látsz rá példát (16-DIK LECKE)
 '''



'''
len - visszaadja, hogy egy listában hány darab valami szerepel 
nem csak listában jo, hanem stringre is 
a 9. projekt 60 as vonalán látsz rá példát 
a stringben karaktert számol lásd, 99. vonalon (kiirja a konzol a karakterek szamat)
'''

print(len("hello, hogy vagy?"))



'''
max - mindig a legnagyobb szamot jeleniti meg a konzolra
peldat lasd a 118. vonalon
min - ugyan az ellentetesen
'''
print(max(7, 4, 0, 45, 789, 1262))
print(min(7, 4, 0, 45, 789, 1262))



'''
pow - haványozás
ugyan az mint ez **
pelda a 119. vonalon
'''
print(2**10)
print(pow(2, 10))



'''
LIST ÉS RANGE KOMBÓ
mit csinál? az osszes szamot leirja sorrendben 
a harmadik érték, a lépést jelöli (a 128-as sorban kettesevel megy)
'''
print(list(range(50, 100, 2)))


'''
ezzel lehet megforditani listak tartalmanak sorrendjet
print(list(reversed(barmilyenlista))
'''



'''
round - kerekites
 kerekiti a szamokat 
 pelda a 146os vonalon
  a 2. szám (itt a 1-es) megszabja hogy meddig vágja le nekünk a tizedes vessző után! (és onnan kerekiti a szamot)
  
 12.50-nél még lefele kerekit!
'''

print(round(12.51, 1))



'''
sum - össszegek
'''

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (sum(szamok))



'''
type - típus
a 4 es projektben
mit csinal? visszaadja egy valtozonak a tipusat 
leirja a konzolra a zarojelben irt tipusfajta nevet 
'''
print(type(10))
print(type(False))

# Updated: 2020.07.29
# Made on 2020.07.29 By Robi






