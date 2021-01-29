

lista1 = ('Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi')

# INDEXELÉS KÖVETKEZIK
# akkor használom mikor csak 1 valamit akarunk visszakapni a listában
# négyzetes zárojelet rakunk bele, és megadjuk h hányadik sorban van a kiszemelt
# az elso mindig a 0, a masodik mindig az 1 es igy tovabb...
print (lista1[0])
print (lista1[-1])      # így (minusz-al) adjuk meg hátulról adja vissza.. itt nincs -0 !!!

#----------------------------------------------------------------------------------------------------------------------

#szeletelés
print(lista1[2:5])      # kivalasztod hogy mettol meddig mutassa
print(lista1[2:])       # így csak végigmegy, jelen esetben a 2estől
                        # fontos hogy legyen ott a kettőspont!

#----------------------------------------------------------------------------------------------------------------------

# MULTI DIMENZIÓS LISTÁK (két dimenziós)

lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]      # listák a listán belül

print(lista2)   # kiírtam csak simán

# ha csak az egyik listát akarom, 29as sávban látod hogy kell

print (lista2[1])

print (lista2[1][2])   # Így választhatom ki a kis listában lévő számot !!!INDEXRE FIGYELJ!!! Megjegyezni!

# ezzel a modszerrel tudsz játékokat csinálni, amelyik rácsalapu

#-----------------------------------------------------------------------------------------------------------------------

# RANGE / TÁVOLSÁG

tartomany = range (100)       #így keszítünk tartományt
print (tartomany)             # lathato hogy nem irja ki az osszes szamot, ha ezt akarjuk, nézz lejjebb

print(list(tartomany))         # így tudjuk listába tenni
                               # így nem megy el 100ig, csak azt mutatja meg, hogy hány
                               # számból áll a tartomány(0-val egyutt)

# Updated: 2020.07.28
# Made on 2020.07.28 By Robi
