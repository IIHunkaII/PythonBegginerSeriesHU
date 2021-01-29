
# for loop - for ciklus

# akkor használjuk amikor valamit, 1nél sokkal többször akarunk lefutttatni

print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')        # ha ez kevésnek bizonyul, itt jön jól a for loop (ez 9 db hello)
print('Hello')
print('Hello')
print('Hello')
print('Hello')

for i in range (9):   # így használd! Amit sorbehuzassal irsz be, a rendszer azt fogja elvégezni
    print('Hello')    # az "i" lehet bármilyen névvel ellátva, hiszen változó (i = iterator - ismétlődő)
# tehat osszesen 18 Hello van
#  A :-RA FIGYELJ ODA!
# amit a loop sorbehuzassal irsz be az lesz vegezve

for bla in range(11):
    print(bla)       # nincs macskakorom, tehat nem veszi string-nek, ezert nem irja le azt h bla, hanem változónak nézi

tartomany = range(10)
#print (tartomany)    # kovertáld listává hogy az összes számjegy megjelenjen
                      # (EZÉRT RAKTAM EZT A SORBAN LÉVŐ PARANCSOT KOMMENTBE HOGY NE ZAVARJON)
print (list(tartomany))

# Másik modja:

lista1 = ('Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi')

print(len(lista1))   # ha ezt akarjuk loopolni, nézd a 36. vonalat Ez irja ki hogy mennyi részből áll a lista(5)

for i in range(len(lista1)):       # a hossz miatt van belőle 5 (annyiszor fut le, amilyen a len) olyan, mintha 5öt írnék
    print(lista1[i])               # ebben a sorban az i=index minden típus értékét felveszi és azt tűzi ki, így megy át a másikra
                                   #  addig, míg a parancs le nem áll --TEHÁT KIIRJA A TIPUST SORONKENT EGYESEVEL A KONZOLRA

# Több tanulást igényel!

# Updated: 2020.07.28
# Made on 2020.07.28 By Robi