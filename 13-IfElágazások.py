
# if statements, conditionals - elagazasok, kondicionalisok

eletkor = 00                                     # itt add meg az életkorodat!

if eletkor < 18:
    if eletkor >= 16:                            # nesting = if kondicio letrehozasa az if kondicion belul (line 7)
        print('Egy kis sort megihatsz...')
    else:                                        # azert van else, mert ennel kisebb eletkor mindig oda fog kerulni
        print ('Se cigi, se pia, '               # hiszen belementunk az "if életkor kevesebb mint 18" testebe
               'nem múltál el 16!')

elif eletkor >= 18 and eletkor <30:              # elif = elágazások (the if statement) statement = állítás
    print('Jo bulizast!')
elif eletkor > 30 and eletkor < 65:              # végtelen elif-et tudok csinálni az if-en belül
    print ('Csak mértékkel!')                    # azert van else a 17. vonalon, mert az eletkor mar tobb mint a definiált
else:                                            # ha az összes boolean képlet hamisnak bizonyul, ott jön jól az else
    print('Nyugdíjas élet')                      # az IF-ből és az ELSE-ből MINDIG csak 1 van

                                                 # FONTOS!
                                                 #  AZ ELIF: mindig csak azokkal foglalkozik, amiket elsőre igaznak
                                                 # talál a fordito, bele megy a testébe és onnan elemzi tovább,
                                                 # többit átugorja, hiába lehet igaz a következő!!

# Updated: 2020.07.28
# Made on 2020.07.28 By Robi