
file = open ('20-kiegészítő.txt', 'r', encoding='utf-8')  # így olvassuk be a file-t a beepitett fuggvennyel(18. lecke)
# 'r' = read(olvassa be), ezen a helyen adjuk meg h milyen modban nyissa meg
# encoding = utf-8 karakter kodolast hasznal ÍGY már felismeri az á, é, ü, ú stb-t
# ha ÍGY hasznalom a filet akkor soha ne felejtsd el lezárni

sor = file.readline()   # ezzel csinalom meg hogy kiirja a fajl tartalmat a konzolra
print(sor.strip())      # sor.strip() = nem hagy üres sorokat a sorok között


sor = file.readline()  # copy-paste-elem hogy minden sort kiirja, mert amugy soronkent megy
print(sor.strip())

file.close()


# EGYSZERUBB MODSZEREK LENT


# FOR MÓDSZER
for sor in file:         # így is meg lehet csinálni
    print(sor.strip())   # ez a legegyszerubb

# WHILE MÓDSZER
line = file.readline()   # elsonek be kell olvasni legalabb egy sort hozza
while sor:               #
    print(sor.strip())
    sor = file.readline()
# a különbseg a for loop es a while ciklus kozott hogy a while nál elore be kell olvasni egy sort
# LEFORDITVA= a while tiklus addig fog menni, míg talál sort a fileban



# WITH KULCSSZO MODSZER
with open('20-kiegészítő.txt', 'r', encoding='utf-8') as file:      # with = context manager, as file = mint fájl
    for sor in file:
        print(sor.strip())                                          # kulonbseg hogy itt magatol lezarja a filet

# EGYEB TUDNIVALOK
'''
Mappa kivalasztasa
('LearningBSCS/20-kiegészítő.txt', 'r', encoding='utf-8')
LearningBSCS/ - ezzel mondom meg hogy melyik mappában keresse a filet
(azert kommentelem ezt ki mind mert megtalalna a filet a kod nelkul is mert ugyan abba van a ketto) 
'''

# READLINES / READLINE / READ   - EZEK A METODUSOK LETEZNEK

# readline = csak egy sort olvas be      readline = egy sor a filebol
sor = file.readline()
print(sor)

while sor:
    print (sor.strip())
    sor = file.readline()


# readlines = egy sorban kiirja a fajl egesz tartalmat a konzolra
sor = file.readlines()
print(sor)


# read = az egeszet kimasolja es ugy vetiti a konzolra, mint stringet, rengeteg soros szovegnel inkabb olvasd be soronkent
sor = file.read()
print(sor)

# Updated: 2020.08.01
# Made on 2020.08.01 By Robi
















