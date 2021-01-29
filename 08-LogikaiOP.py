
# logikai operatorok
# ezek: and or not - java nyelven: & || !

szam1 = 2
szam2 = 4
# bal oldal szerint true, a jobb szerint is, tehat TRUE (8. VONAL)
print (szam1 < szam2 and szam1 == 2)

# ÍGY MŰKÖDIK
'''
TRUE AND TRUE = TRUE
TRUE AND FALSE = FALSE
FALSE AND TRUE = FALSE
FALSE AND FALSE = FALSE

TRUE OR TRUE = TRUE
TRUE OR FALSE = TRUE
FALSE OR TRUE = TRUE
FALSE OR FALSE = FALSE

TRUE AND NOT FALSE = TRUE 
'''

print (szam1 < szam2 and szam1 == 3)  # false lesz mert az egyik hamis és 'and-et' adtam hozzá!
print (szam1 < szam2 or szam1 == 3)   #true lesz mert az egyik igaz és or-t adtam hozzá! elég ha egy igaz
print (szam1 < szam2 and not szam1 == 3)   # ez true mert tagadtuk a fales-t ÍGY: 2 kisebb mint négy és
                                           # négy NEM egyenlő hárommal
# not False = True
# not True = False

# Updated: 2020.07.28
# Made on 2020.07.28 By Robi
