
# NUMBERS, STRING,    BOOLEAN,    LIST,    TUPLE,     DICTIONARY,  USER DEFINED
#  SZÁMOK, ZSINOR, LOGIKAI VÁLTOZÓ, LISTA, RENDEZETT N-ES, SZÓTÁR, FELHASZNÁLÓ DEFINIÁLT

szam1 = 10        # number
szam2 = 20.76473  # number
szam3 = 32.3e18   # number tudomanyos szam
szam4 = .876j     # number komplex szam


#----------------------------------------------------------------------------------------------------------------------

# STRING

nev1 = "Eniko"
hajszin = 'szoke'
mondas = 'ki koran kel, aranyat lel'

#----------------------------------------------------------------------------------------------------------------------

# boolean

igaz = True

hamis = False

#----------------------------------------------------------------------------------------------------------------------

lista = []    # ezzel a zarojellel jeloljuk

#----------------------------------------------------------------------------------------------------------------------

my_tuple = ()  # ezzel a zarojellel jeloljuk
my_tuple = [(1, 'apple'), (2, 'apple')]
my_dictionary = dict(my_tuple) # kiirtam a szotarat, amibe beleraktam egy tuple-t
print(my_dictionary)
print(my_tuple)
#----------------------------------------------------------------------------------------------------------------------

my_dict = {'name':'John', 1:[2 ,3 ,4]}

print(my_dict)
# dict = dictionary tehat szotar

# szotarakat kulcsokkal indexeljük, a kulcsok megváltozhatatlan adattipusok lehetnek, így a szovegek es a
# szamok mindig lehetnek kulcsok a python nyelvben

# a szotarakra gondolj ugy mint kulcs érték párok rendezetlen halmazára
# kapcsos zarojelek  hasznalata kotelezo ( az teszi szotárrá)

#-----------------------------------------------------------------------------------------------------------------------


print (type(my_tuple))   # ezzel nézem meg a típust, a type-al, ez még biztos tanulást igényel
                         # mostmár megértettem, a konzolra kiirja a zarojelben levo tipus tipusat(2020.07.29)

# Updated on 2020.07.29
# Made on 2020.07.28 By Robi

