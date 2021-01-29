

#----------------------------------------------------------------------------------------------------------------------


# exception handling (error handling) azaz kivételkezelés (hibakezeles)
try:
    print (pelda)
except NameError as e:
    print (e, ' - igy adj nevet az errornak!')



    print ('A program vege!')  # mutatja h a program lefutott az error ellenére

#----------------------------------------------------------------------------------------------------------------------


''' Kivételekhez hibakod helyett irhato ez is: continue igy a rendszer ignorálni 
fogja azokat a karaktereket 
amikkel nem tud számolni 
'''

lista = ('1', '2', '3', None, '4', '', '5', True, 'Bözsi', '74.67')

for i in lista:
    try:
        print (int(i)*2)
    except: continue

#a True-t ugy fogja fol a fordito mint egy 1-est ezert van vegen a 2 es

#----------------------------------------------------------------------------------------------------------------------


try:
    print (bla)
except:
    print ('nem jo valtozo nev')
else:
    print ('az else')
finally:
    print('try vege')

    # try - except a leggyakoribb
    # a finally mindig lefut
    # az else uzenet csak akkor jelenik meg ha NINCS error

# Updated: 2020.07.27
# Made on 2020.07.27 By Robi