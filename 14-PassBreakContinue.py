
# pass, continue es break kulcsszavak

#while True:     # a while True-hoz mindig kell valamit hozzáírni, különben hibás, mert nincs állítás
    #pass        # a pass-el viszont átugorhatjuk ezt a problemat (ha hozzairjuk)
                 # kommentbe rakom h ne zavarjon

#for i in range (10):
#   if i == 5:    # break kulcsszoval lehet megallitani a ciklust, persze írd hozza!!!
#        break    # a 9es es a 10 sorban ezt tettem:a szam nem lehet 5 mert akkor break aktivalodik és megszakitja a loopot
#    print (i)    # kommentbe rakom h ne zavarjon


#for i in range (10):
#   if i == 5:
#       continue  # ezzel kihagyom az 5-öst, nem fogja kiirni a konzolra azt a szamot
#   print(i)



szamlalo = 0

while True:
    szamlalo +=1                 # a 24 es es a 25 csik azt teszi, hogy kizarolag maradek nelküli, páros betüket atlepi!
    if szamlalo % 2 == 0:        # sorbehuzast nem elfelejteni
        continue
    print (szamlalo)
    if szamlalo > 20:            # ezzel állítjuk le az örökös loopot (28 es 29es vonalban)
        break
# EZEKET MIND ÉRDEMES MEGTANULNI!

# Updated: 2020.07.28
# Made on 2020.07.28 By Robi