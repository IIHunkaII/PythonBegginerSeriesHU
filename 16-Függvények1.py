

nevek1 = ['Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi', 'Zsuzsi', 'Evi', 10, True]
nevek2 = ['Pityu', 'Ati', 'Peti', 'Bence', 'Feri']

#for nev in nevek1:
    #print(nev)               # igy irom ki mindenki nevet
                              # zavart, ezert raktam kommentbe
                              # gyorsabban ugyanezt a 13 as vonalon latod hogy
#for nev in nevek2:
    #print(nev)

def nev_printer(nev_lista):          # def = definiált függvény lehet bármi ugyan azok a szabalyok mint a valtozoknal
    for nev in nev_lista:            # függvényt def-fel kezdünk, nev printer csak egy elnevezes printer=nyomtató
        if isinstance(nev, str):     # 13-as vonalon a zarojelben adjuk meg a bemenetét
            print(nev.upper())       # a 28es és a 29es vonalon írhatod be a kivant listat
        else:                        # .upper = minden string nagybetűs lesz - str = String
            print ('nem string tipus, hanem: ' + str (type(nev)))
                                     # a 15-16os vonalrol késöbb tanulok

                                     # 17-18as sorbarban mivel nem csak stringet tartalmaz a lista, a rendszer errort
                                     # irna ki, ezert a tobbi tipussal annyit csinálunk hogy
                                     # ismerteti a sajat tipusat a konzolon

                                     #  ' + str (type(nev))) errol kesobb tudunk meg tobbet, a lenyeg az hogy leirja a
                                     # tipusat a konzolra
                                     # +-szal összefűzöm

nev_printer(nevek1)
nev_printer(nevek2)

# függvényeket azert jobb hasznalni a folyamatos copy-paste, copy-paste helyett, mert tisztább lesz a programod

# Updated: 2020.07.29
# Made on 2020.07.29 By Robi



















