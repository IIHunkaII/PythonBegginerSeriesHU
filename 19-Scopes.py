
# variable scope = valtozok lathatosaga, es elettartama - lokális es globalis valtozok

# function scope, module scope, class scope

# MODULE SCOPE
# minden amit ehhez tartozik az globalis modul
# modulnak szamit egy python fájl

# a = 1                # ez is egy globalis valtozo module

# FUNCTION SCOPE ÉS ÉLETTARTAM
def test():             # függvényt hozok létre
    global a, b         # beallitom hogy melyik 'a'-ra gondoljon a gep
    a = 12              # Az'a' és a 'b' csak addig él,míg a parancs le nem fut a 'def'testében,FUNCTION scopehoz tartozik
    b = 15              # tehat ezek csak funkciot tolt be a testben, nem allandoak 16-17es vonal
    print(a, b)
test()                  # test még nem tudom mit jelent ebben a sorban, ezzel hivom meg a fuggvenyt
print(a, b)

# igy rakok barmit function scope-pá
def test ():            # függvénybe rakom az if true-t mert ha nem raknam module scope lenne
    if True:
        c = 78

print(c)                # így nem is talalja a rendszer a c-t, ha ki akarnad irni azt bele kene irni a 23as sorba


def test2():                # fuggvenybe rakom, hogy lokalissa valjon
    for i in range (5):     # i = index
        b = 54              # EZEK MIND ATFOLYNAK A MODULE SCOPE-BA CSAK NEM FOG LATSZANI MERT ERRORT IR AZ AZELOTTI
        pass                # MÜVELETEM ( idővel kiraktam a fuggvenyt szoval igy megint lokalis lesz)
        print(i)
        print(b)

test2()

# FONTOS, A while A for ÉS AZ if CIKLUSOKNAK NINCS SAJÁT SCOPE-JUK Javaban ilyen nincs

# Updated: 2020.07.29
# Made on 2020.07.29 By Robi
