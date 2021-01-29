
jelszo = 'kisuborka'

bemenet = input('mi a jelszó?')   # input = globális függvény, amin bemeneteket tud fogadni a program(pl betűket)
                                  # amíg nem írok be valamit az imput részére, addig nem enged tovább a vonalak többi reszere
proba = 0                         # ezzel adok meg probakat, es azert 0 mert onnan indul a szamolas

while bemenet != jelszo:          # sor jelentese: ha a bemenet nem egyezik a jelszoval...
    proba += 1                    # while loopon belül a proba! sor jelentese: az input nem egyezik a jelszoval ezert +1...
    if proba == 3:                # 3. hiba utan a rendszer megszakad a break miatt
        print('Nincs több probákozás!')
        break
    print('Téves jelszó, probald ujra!')   # sor jelentese+ ha nem irtad be jol a jelszot, írd ki a stringet
    bemenet = input('Na mi a jelszó?')     # itt megvaltoztattam a valtozót, azt hiszem.. (de csak ebben a testben)

if bemenet == jelszo:             #  sor jelentese: ha eltaláltuk a jelszót:...
    print ('Üdv!')

# Updated: 2020.07.28
# Made on 2020.07.28 By Robi