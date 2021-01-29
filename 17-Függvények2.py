
a = 20                  # igy adjuk meg az ertekeket
b = 10

def osszeadas1():       # meg nem tudom miert kell zarojel
    print(a+b)          # itt szabjuk meg sorkizarral hogy mi tortennyen
                        # zarojelek = parameterek, talán szürö hogy mit akarsz elvegezni, beleirhatsz
                        # EZT MÉG NEM ÉRTEM!

def osszeadas2(a, b, c=4):
    return a+b+c

def osszeadas3(*args):   # ha több parametert akarok megadni, akkor rakd ki a *args-ot
    return sum(args)     # args = parameterek,neve barmi lehet, függvény bemenet röviditve
                         # hogyan hozd vissza a függvény bemenet összegét? (line 14)
osszeadas1()             # ezzel végezzük el az egyenletet, még nem tudom miert kell zarojel

def udvozlesek(*args):                            # végetelen szamu bemeneteket a csillag argsal vegzem el
    koszones = 'Ennyi fele koszones letezik: '    # udvozlesen belul koszones(SORKIZART!)
    for k in args:                                #line 20: létrehoz egy for loopot, az argson fog atlepni(k mint koszones)
        koszones += k                             #hozzafűzi a koszones valtozohoz a k-t, ezzel a modszerrel
        koszones += ", "                          # ez a sor azert kell, mert kulonben a szavak egybefolynának

    print(koszones[0:len(koszones)-2])            # ebben a sorban adom meg hogy mennyit vágjon le a szövegből és hogy
                                                  # honnan kezdodjon ( 0 tól elozo elotti karakterig tehat -2 a len-nel)

udvozlesek ('szia', 'szevasz', 'Hello', 'Cs')     # igy irom ki hogy mit tartalmazzzon

osszeg = osszeadas2(45, 25)#osszeg valtozohoz kerult az osszeadas2return-el visszahoztuk az a+b értéket, és a 45,25hozzaadodik
print (osszeg)             # ez mind a 10es, 11es es a 18as illetve a 19es sorban jatszodik le
                           # nehezitettem azzal, hogy hozzaadtam c erteket

print (osszeadas3(10, 20,  30, 40, 50, 60, 70, 80, 90, 100))    # kiprinteltem a 13as sort, itt megadtam az args
                                                                # értékeit amit össze kell adnia

# Updated: 2020.07.29
# Made on 2020.07.29 By Robi


