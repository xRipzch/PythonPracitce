# pyright: basic
"""
=============================================================
  PYTHON EXAM PRACTICE 2
  Udfyld funktionerne - erstat 'pass' med din kode.
  Kør filen med:  python practice2.py
  Hver opgave printer PASS / FAIL / SKIP (hvis du ikke har udfyldt den endnu)
=============================================================
"""


# ============================================================
# SEKTION 1: VARIABLER & GRUNDLÆGGENDE OPERATIONER
# ============================================================
# En variabel er et navn der peger på en værdi.
# Man tildeler med = tegnet.
#
#   x = 10            # int (heltal)
#   name = "Alice"    # str (tekststreng)
#   pi = 3.14         # float (decimaltal)
#   is_ok = True      # bool (True / False)
#
# Typer kan konverteres:
#   int("42") -> 42       str(42) -> "42"
#   float("3.14") -> 3.14 int(3.9) -> 3 (runder ned)
#
# Aritmetik:
#   +  -  *  /           (standard)
#   //                    (heltalsdivision: 7 // 2 = 3)
#   %                     (modulo/rest: 7 % 2 = 1)
#   **                    (potens: 2 ** 3 = 8)
# ============================================================

# Q1: Returner data + 100

data_1 = 42


def answer_1(my_var):
    pass


# Q2: Returner længden af strengen (antal tegn)
data_2 = "cybersecurity"


def answer_2(my_var):
    pass


# ============================================================
# SEKTION 2: STRINGS (Tekststrenge)
# ============================================================
# En string er en sekvens af tegn: "hello" eller 'hello'
#
# Vigtige metoder:
#   s.upper()            -> "HELLO"
#   s.lower()            -> "hello"
#   s.replace(old, new)  -> erstat tekst
#   s.split(sep)         -> split til liste   "a,b".split(",") -> ["a","b"]
#   "sep".join(lst)      -> saml liste        "-".join(["a","b"]) -> "a-b"
#   s.strip()            -> fjern whitespace i start/slut
#   s.startswith("x")    -> True/False
#   s.endswith("x")      -> True/False
#   s.count("x")         -> antal forekomster af "x"
#   len(s)               -> antal tegn
#
# Slicing: s[start:stop:step]
#   s[0:3]    -> de første 3 tegn
#   s[-3:]    -> de sidste 3 tegn
#   s[::-1]   -> hele strengen baglæns
#
# f-strings (formatering):
#   f"Hej {name}, du er {age} år"
#   f"{3.14159:.2f}" -> "3.14"
# ============================================================

# Q3: Returner kun de første 5 tegn i strengen
data_3 = "encryption"


def answer_3(my_var):
    pass


# Q4: Returner strengen med ALLE mellemrum fjernet
data_4 = "h e l l o w o r l d"


def answer_4(my_var):
    pass


# Q5: Tæl antal gange bogstavet 'a' forekommer (CASE INSENSITIVE - både 'A' og 'a')
data_5 = "AbracadAbra"


def answer_5(my_var):
    pass


# Q6: Split strengen ved kommaer og returner som en liste
data_6 = "alpha,beta,gamma,delta,epsilon"


def answer_6(my_var):
    pass


# ============================================================
# SEKTION 3: LISTS (Lister)
# ============================================================
# En liste er en ORDNET, MUTERBAR samling: [1, 2, 3]
#
# Indeksering (0-baseret):
#   lst[0]   -> første element
#   lst[-1]  -> sidste element
#
# Slicing:
#   lst[:3]    -> de første 3 elementer
#   lst[-4:]   -> de sidste 4 elementer
#   lst[::-1]  -> listen baglæns
#   lst[::2]   -> hvert andet element
#
# Vigtige metoder:
#   lst.append(x)      -> tilføj til slutningen
#   lst.insert(i, x)   -> indsæt ved indeks i
#   lst.remove(x)      -> fjern første forekomst af x
#   lst.pop(i)         -> fjern og returner element ved indeks i
#   lst.index(x)       -> returner indeks for x
#   sorted(lst)        -> returner NY sorteret liste
#   lst.sort()         -> sorter IN-PLACE (returnerer None!)
#   len(lst)           -> antal elementer
#   sum(lst)           -> summen af alle tal
#
# List comprehension:
#   [x * 2 for x in lst]            -> fordobl alle
#   [x for x in lst if x > 5]       -> filtrer
# ============================================================

# Q7: Returner de SIDSTE 4 elementer fra listen
data_7 = [12, 45, 78, 23, 56, 89, 34, 67]


def answer_7(my_var):
    pass


# Q8: Returner en liste med kun de tal der er STØRRE end 50
data_8 = [12, 67, 34, 89, 5, 52, 43, 91, 28]


def answer_8(my_var):
    pass


# Q9: Returner listen i OMVENDT rækkefølge (baglæns)
data_9 = [10, 20, 30, 40, 50]


def answer_9(my_var):
    pass


# Q10: Returner PRODUKTET af alle tal i listen (gang alle sammen)
data_10 = [2, 3, 4, 5]


def answer_10(my_var):
    pass


# Q11: Returner INDEKSET (positionen) for værdien 99 i listen
data_11 = [10, 30, 50, 70, 99, 120]


def answer_11(my_var):
    pass


# Q12: Returner en ny liste hvor hvert ULIGE tal er fordoblet, LIGE tal forbliver uændrede
# Eksempel: [1, 2, 3] -> [2, 2, 6]
data_12 = [1, 2, 3, 4, 5, 6, 7, 8]


def answer_12(my_var):
    pass


# ============================================================
# SEKTION 4: TUPLES (Tupler)
# ============================================================
# En tuple er en ORDNET, IMMUTABLE (uforanderlig) samling.
# Defineres med parenteser: (1, 2, 3)
#
# Forskellen fra lister:
#   - Tuples kan IKKE ændres efter oprettelse
#   - Tuples bruger () i stedet for []
#   - Tuples kan bruges som dictionary keys (lister kan ikke)
#
# Operationer:
#   t[0]          -> første element
#   t[0:2]        -> slice
#   len(t)        -> antal elementer
#   t1 + t2       -> sammensæt to tuples
#   a, b = (1,2)  -> unpacking
# ============================================================

# Q13: Returner antallet af elementer i tuplen
data_13 = ("network", "security", "firewall", "encryption", "protocol")


def answer_13(my_var):
    pass


# Q14: Data er en liste af tuples med (navn, alder).
#      Returner NAVNET på den ældste person.
data_14 = [("Alice", 32), ("Bob", 45), ("Charlie", 28), ("Diana", 51)]


def answer_14(my_var):
    pass


# Q15: Data er en tuple af to tuples. Returner dem sammensat til én tuple.
# Eksempel: ((1,2), (3,4)) -> (1, 2, 3, 4)
data_15 = ((1, 2, 3), (4, 5, 6))


def answer_15(my_var):
    pass


# ============================================================
# SEKTION 5: DICTIONARIES (Ordbøger)
# ============================================================
# En dictionary er en samling af KEY:VALUE par: {"key": value}
#
# Vigtige operationer:
#   d[key]              -> hent værdi (KeyError hvis key mangler)
#   d.get(key, default) -> hent værdi, returner default hvis key mangler
#   d[key] = value      -> tilføj eller opdater
#   del d[key]          -> slet key-value par
#   d.keys()            -> alle keys
#   d.values()          -> alle values
#   d.items()           -> alle (key, value) par
#   key in d            -> True hvis key findes
#   len(d)              -> antal par
#
# Dict comprehension:
#   {k: v * 2 for k, v in d.items()}
#
# dict() + zip():
#   dict(zip(keys_list, values_list))
# ============================================================

# Q16: Returner en SORTERET liste af alle keys i dictionaryen
data_16 = {"banana": 3, "apple": 5, "cherry": 2, "date": 8}


def answer_16(my_var):
    pass


# Q17: Returner True hvis nøglen 'admin' FINDES i dictionaryen, ellers False
data_17 = {"user": "john", "role": "editor", "admin": True, "level": 5}


def answer_17(my_var):
    pass


# Q18: Returner en NY dict hvor keys og values er byttet om
# Eksempel: {"a": 1} -> {1: "a"}
data_18 = {"a": 1, "b": 2, "c": 3}


def answer_18(my_var):
    pass


# Q19: Data er en tuple af to lister: (keys, values).
#      Brug zip() til at lave en dictionary.
data_19 = (["name", "age", "city"], ["Alice", 30, "Copenhagen"])


def answer_19(my_var):
    pass


# ============================================================
# SEKTION 6: SETS (Mængder)
# ============================================================
# Et set er en UORDNET samling af UNIKKE elementer: {1, 2, 3}
# Tomt set: set()   (IKKE {} som er en tom dict!)
#
# Vigtige operationer:
#   s.add(x)          -> tilføj element
#   s.remove(x)       -> fjern (fejl hvis mangler)
#   s.discard(x)      -> fjern (ingen fejl hvis mangler)
#   s1 | s2           -> union (alle fra begge)
#   s1 & s2           -> intersection (fælles)
#   s1 - s2           -> difference (kun i s1)
#   s1.issubset(s2)   -> True hvis alle elementer i s1 også er i s2
#   len(s)            -> antal elementer
# ============================================================

# Q20: Returner et set med elementer der er i den FØRSTE liste men IKKE i den anden (difference)
data_20 = ([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])


def answer_20(my_var):
    pass


# Q21: Returner union (alle elementer fra begge sets)
data_21 = ({10, 20, 30}, {30, 40, 50})


def answer_21(my_var):
    pass


# Q22: Returner True hvis det første set er en SUBSET af det andet
data_22 = ({1, 2, 3}, {1, 2, 3, 4, 5})


def answer_22(my_var):
    pass


# ============================================================
# SEKTION 7: LOOPS (Løkker) inkl. NESTED LOOPS
# ============================================================
# for-loop: iterer over en sekvens
#   for item in [1, 2, 3]:
#       print(item)
#
# range():
#   range(5)          -> 0, 1, 2, 3, 4
#   range(2, 8)       -> 2, 3, 4, 5, 6, 7
#   range(0, 20, 3)   -> 0, 3, 6, 9, 12, 15, 18
#
# while-loop:
#   while x < 10:
#       x += 1
#
# enumerate(): giver (indeks, element)
#   for i, val in enumerate(["a", "b"]):
#       print(i, val)   # 0 a, 1 b
#
# Nested loops:
#   for i in range(3):
#       for j in range(3):
#           print(i, j)
#
# break:    stop loopet helt
# continue: spring til næste iteration
# ============================================================

# Q23: Brug en loop til at beregne FAKULTET (factorial) af data
# Fakultet: 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
data_23 = 6


def answer_23(my_var):
    pass


# Q24: FizzBuzz! Returner en liste for tallene 1 til data (inklusiv).
#      - Hvis tallet er deleligt med 3: "Fizz"
#      - Hvis tallet er deleligt med 5: "Buzz"
#      - Hvis tallet er deleligt med BEGGE 3 og 5: "FizzBuzz"
#      - Ellers: tallet som string (f.eks. "1", "2", "4")
data_24 = 15


def answer_24(my_var):
    pass


# Q25: Brug nested loops til at generere ALLE par (i, j) som tuples
#      hvor i går fra 1 til data OG j går fra 1 til data (begge inklusiv)
# Eksempel med data=2: [(1,1), (1,2), (2,1), (2,2)]
data_25 = 3


def answer_25(my_var):
    pass


# ============================================================
# SEKTION 8: EXCEPTION HANDLING (Fejlhåndtering)
# ============================================================
# try/except fanger fejl så programmet ikke crasher.
#
#   try:
#       result = 10 / 0
#   except ZeroDivisionError:
#       result = "fejl"
#
# Struktur:
#   try:      -> kode der kan fejle
#   except:   -> hvad der sker ved fejl
#   else:     -> kører kun hvis INGEN fejl
#   finally:  -> kører ALTID (cleanup)
#
# Almindelige exceptions:
#   ValueError        -> int("abc")
#   TypeError         -> 1 + "a"
#   IndexError        -> [1,2][5]
#   KeyError          -> {}["missing"]
#   ZeroDivisionError -> 10 / 0
#   FileNotFoundError -> open("missing.txt")
# ============================================================

# Q26: Prøv at tilgå indeks 10 i listen.
#      Returner elementet hvis det lykkes, ellers returner "index out of range"
data_26 = [5, 10, 15, 20, 25]


def answer_26(my_var):
    pass


# Q27: Data er en liste af strings. Prøv at konvertere hvert element til int med int().
#      Returner en liste med KUN de elementer der lykkes.
# Eksempel: ["42", "hello", "7"] -> [42, 7]
data_27 = ["42", "hello", "7", "3.14", "99", "world"]


def answer_27(my_var):
    pass


# ============================================================
# SEKTION 9: FUNCTIONS (Funktioner)
# ============================================================
# En funktion er en genbrugelig blok af kode.
#
# Definition:
#   def funktions_navn(param1, param2):
#       return resultat
#
# Default parametre:
#   def greet(name, greeting="Hello"):
#       return f"{greeting}, {name}"
#
# Flere returværdier (returnerer tuple):
#   def min_max(lst):
#       return min(lst), max(lst)
#
# Lambda (anonym funktion):
#   double = lambda x: x * 2
#   sorted(lst, key=lambda x: x[1])
# ============================================================

# Q28: Returner True hvis strengen er et PALINDROM (læses ens forfra og bagfra)
# Ignorer store/små bogstaver (case insensitive)
# Eksempel: "racecar" -> True, "hello" -> False
data_28 = "racecar"


def answer_28(my_var):
    pass


# Q29: Returner det NÆSTSTØRSTE tal i listen (second largest, unikke værdier)
# Eksempel: [5, 3, 9, 1, 9] -> 5 (9 er størst, 5 er næststørst)
data_29 = [15, 42, 8, 23, 42, 4]


def answer_29(my_var):
    pass


# ============================================================
# SEKTION 10: FILE I/O (Læs/skriv filer)
# ============================================================
# Læs fil:
#   with open("fil.txt", "r") as f:
#       content = f.read()        -> hele filen som string
#       lines = f.readlines()     -> liste af linjer
#
# Skriv fil:
#   with open("fil.txt", "w") as f:  -> overskriver
#       f.write("Hello\n")
#
#   with open("fil.txt", "a") as f:  -> appender
#       f.write("More\n")
#
# Modes: "r" = read, "w" = write (overskriver!), "a" = append
# with-statement lukker filen automatisk.
# ============================================================

# Q30: Skriv dict'en til /tmp/practice2_q30.txt som "key:value" linjer (én per linje).
#      Læs filen tilbage og rekonstruer en dict fra indholdet.
#      Returner den rekonstruerede dict.
data_30 = {"host": "192.168.1.1", "port": "8080", "protocol": "https"}


def answer_30(my_var):
    pass


# ============================================================
# SEKTION 11: IMPORTING MODULES (Importere moduler)
# ============================================================
# Import hele modulet:
#   import math
#   math.sqrt(16)       -> 4.0
#
# Import specifik funktion:
#   from math import sqrt, ceil, floor
#   sqrt(16)
#
# Import med alias:
#   import json as j
#
# Nyttige standardmoduler:
#   math     -> sqrt, pi, floor, ceil
#   os       -> filstier, miljøvariabler
#   sys      -> argv, path
#   random   -> randint, choice, shuffle
#   json     -> loads (parse), dumps (serialize)
#   re       -> regular expressions
# ============================================================

# Q31: Brug math modulet til at returnere CEIL (rund op) af data
# Eksempel: 7.3 -> 8

#data_31 = 7.3

data_31 = 7.3
from math import ceil as c
def answer_31(my_var):
    pass


# Q32: Brug json modulet til at konvertere dict'en til en JSON-string
data_32 = {"name": "Bob", "age": 25}

import json
def answer_32(my_var):
    pass


# ============================================================
# SEKTION 12: KOMBINATIONS-OPGAVER
# ============================================================
# Her blandes flere koncepter - ligesom til eksamen!
# ============================================================

# Q33: Data er en log-string med linjer.
#      Returner en dict med {IP-adresse: antal_requests}
#      (IP-adressen er det FØRSTE felt i hver linje)
data_33 = """192.168.1.1 - - [10/Oct/2024] "GET /index" 200 1234
192.168.1.2 - - [10/Oct/2024] "GET /about" 200 5678
192.168.1.1 - - [10/Oct/2024] "POST /login" 302 0
192.168.1.3 - - [10/Oct/2024] "GET /index" 404 0
192.168.1.1 - - [10/Oct/2024] "GET /dashboard" 200 9012"""


def answer_33(my_var):
    pass


# Q34: Returner den streng i listen der har FLEST vokaler (a, e, i, o, u)
data_34 = ["hello", "beautiful", "sky", "queue"]


def answer_34(my_var):
    pass


# Q35: Fordel tallene i tre grupper: positive, negative og zero.
#      Returner {"positive": [...], "negative": [...], "zero": [...]}
#      Behold den originale rækkefølge.
data_35 = [5, -3, 0, 12, -7, 0, 8, -1]


def answer_35(my_var):
    pass


# Q36: Data er en liste af dicts med "item" og "category".
#      Returner en SORTERET liste af alle UNIKKE "category" værdier.
data_36 = [
    {"item": "sword", "category": "weapon"},
    {"item": "shield", "category": "armor"},
    {"item": "potion", "category": "consumable"},
    {"item": "bow", "category": "weapon"},
    {"item": "helmet", "category": "armor"},
]


def answer_36(my_var):
    pass


# Q37: Returner True hvis passwordet opfylder ALLE krav:
#      - Mindst 8 tegn langt
#      - Indeholder mindst ét STORT bogstav
#      - Indeholder mindst ét TAL (ciffer)
data_37 = "Secure99"


def answer_37(my_var):
    pass


# Q38: Data er en liste af dicts med "name" og "score".
#      Returner en liste af NAVNE sorteret efter score FALDENDE (højeste først).
data_38 = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95},
]


def answer_38(my_var):
    pass


# Q39: Caesar cipher! Skift hvert bogstav i strengen N pladser frem i alfabetet.
#      Data er en tuple: (tekst, N). Kun små bogstaver, ingen specialtegn.
#      Wrap around: 'z' + 1 = 'a'
# Eksempel: ("abc", 2) -> "cde"
data_39 = ("hello", 3)


def answer_39(my_var):
    pass


# Q40: Returner en dict med bogstavfrekvenser (kun bogstaver, alt i lowercase).
#      Ignorer mellemrum og specialtegn.
# Eksempel: "Hi!" -> {"h": 1, "i": 1}
data_40 = "Hello World!"


def answer_40(my_var):
    pass


# ============================================================
# SEKTION 13: EKSTRA ØVELSER
# ============================================================

# Q41: Returner en liste af tal fra data der er BÅDE lige OG større end gennemsnittet
data_41 = [10, 25, 30, 45, 50, 15, 20]


def answer_41(my_var):
    pass


# Q42: Data er en matrice (liste af lister).
#      Returner summen af DIAGONALEN (elementer hvor række-indeks == kolonne-indeks)
# Eksempel: [[1,2],[3,4]] -> 1+4 = 5
data_42 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def answer_42(my_var):
    pass


# Q43: Data er en string med komma-separerede "key=value" par.
#      Returner en dictionary.
# Eksempel: "a=1,b=2" -> {"a": "1", "b": "2"}
data_43 = "host=localhost,port=5432,db=mydb,user=admin"


def answer_43(my_var):
    pass


# Q44: Data er en liste med duplikater.
#      Returner en ny liste med duplikater fjernet, MEN behold ORIGINAL rækkefølge.
# Eksempel: [3, 1, 3, 2, 1] -> [3, 1, 2]
data_44 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


def answer_44(my_var):
    pass


# Q45: Returner HVERT ANDET element fra listen, startende fra det første
# Eksempel: [1, 2, 3, 4, 5, 6] -> [1, 3, 5]
data_45 = [10, 20, 30, 40, 50, 60, 70, 80]


def answer_45(my_var):
    pass


# Q46: Data er to strings i en tuple. Returner True hvis de er ANAGRAMMER
#      (indeholder præcis de samme bogstaver, bare i anden rækkefølge)
# Eksempel: ("abc", "cab") -> True
data_46 = ("listen", "silent")


def answer_46(my_var):
    pass


# Q47: Data er en liste af tuples: (navn, [liste af scores]).
#      Returner en dict med {navn: max_score}
data_47 = [("Alice", [85, 92, 78]), ("Bob", [90, 88, 95]), ("Charlie", [70, 82, 76])]


def answer_47(my_var):
    pass


# Q48: Returner strengen i TITLE CASE (første bogstav i hvert ord er stort)
# Hint: Python har en built-in metode til dette!
data_48 = "the quick brown fox jumped"

def answer_48(my_var):
    pass


# Q49: Data er en liste af tal. Returner en RUNNING SUM liste.
# Eksempel: [1, 2, 3] -> [1, 3, 6]  (1, 1+2, 1+2+3)
data_49 = [5, 3, 8, 1, 4]


def answer_49(my_var):
    pass


# Q50: Data er en dict med {elev: [liste af karakterer]}.
#      Returner NAVNET på eleven med det højeste gennemsnit.
data_50 = {"Alice": [90, 85, 92], "Bob": [78, 82, 80], "Charlie": [95, 88, 91]}


def answer_50(my_var):
    pass


# ============================================================
# ============================================================
#  TEST RUNNER - Rør ikke ved koden herunder!
#  Kør: python practice2.py
# ============================================================
# ============================================================

if __name__ == "__main__":
    import base64
    import copy
    import os
    import pickle

    _E = b"gAWVJAQAAAAAAAB9lChLAUuOSwJLDUsDjAVlbmNyeZRLBIwKaGVsbG93b3JsZJRLBUsFSwZdlCiMBWFscGhhlIwEYmV0YZSMBWdhbW1hlIwFZGVsdGGUjAdlcHNpbG9ulGVLB12UKEs4S1lLIktDZUsIXZQoS0NLWUs0S1tlSwldlChLMksoSx5LFEsKZUsKS3hLC0sESwxdlChLAksCSwZLBEsKSwZLDksIZUsNSwVLDowFRGlhbmGUSw8oSwFLAksDSwRLBUsGdJRLEF2UKIwFYXBwbGWUjAZiYW5hbmGUjAZjaGVycnmUjARkYXRllGVLEYhLEn2UKEsBjAFhlEsCjAFilEsDjAFjlHVLE32UKIwEbmFtZZSMBUFsaWNllIwDYWdllEsejARjaXR5lIwKQ29wZW5oYWdlbpR1SxSPlChLAUsCSwOQSxWPlChLMksUSyhLCksekEsWiEsXTdACSxhdlCiMATGUjAEylIwERml6epSMATSUjARCdXp6lGgjjAE3lIwBOJRoI2gljAIxMZRoI4wCMTOUjAIxNJSMCEZpenpCdXp6lGVLGV2UKEsBSwGGlEsBSwKGlEsBSwOGlEsCSwGGlEsCSwKGlEsCSwOGlEsDSwGGlEsDSwKGlEsDSwOGlGVLGowSaW5kZXggb3V0IG9mIHJhbmdllEsbXZQoSypLB0tjZUsciEsdSxdLHn2UKIwEaG9zdJSMCzE5Mi4xNjguMS4xlIwEcG9ydJSMBDgwODCUjAhwcm90b2NvbJSMBWh0dHBzlHVLH0sISyCMGnsibmFtZSI6ICJCb2IiLCAiYWdlIjogMjV9lEshfZQoaDpLA4wLMTkyLjE2OC4xLjKUSwGMCzE5Mi4xNjguMS4zlEsBdUsijAliZWF1dGlmdWyUSyN9lCiMCHBvc2l0aXZllF2UKEsFSwxLCGWMCG5lZ2F0aXZllF2UKEr9////Svn///9K/////2WMBHplcm+UXZQoSwBLAGV1SyRdlCiMBWFybW9ylIwKY29uc3VtYWJsZZSMBndlYXBvbpRlSyWISyZdlChoDYwDQm9ilGgajAdDaGFybGlllGVLJ4wFa2hvb3KUSyh9lCiMAWiUSwGMAWWUSwGMAWyUSwOMAW+USwKMAXeUSwGMAXKUSwGMAWSUSwF1SyldlChLHksyZUsqSw9LK32UKGg5jAlsb2NhbGhvc3SUaDuMBDU0MzKUjAJkYpSMBG15ZGKUjAR1c2VylIwFYWRtaW6UdUssXZQoSwNLAUsESwVLCUsCSwZlSy1dlChLCkseSzJLRmVLLohLL32UKGgaS1xoUEtfaFFLUnVLMIwrVGhlIFF1aWNrIEJyb3duIEZveCBKdW1wcyBPdmVyIFRoZSBMYXp5IERvZ5RLMV2UKEsFSwhLEEsRSxVlSzJoUXUu"
    _A = pickle.loads(base64.b64decode(_E))

    _tests = [
        (1, answer_1, data_1, "Variabler: data + 100"),
        (2, answer_2, data_2, "Variabler: længde af string"),
        (3, answer_3, data_3, "Strings: første 5 tegn"),
        (4, answer_4, data_4, "Strings: fjern mellemrum"),
        (5, answer_5, data_5, "Strings: tæl bogstav (case insensitive)"),
        (6, answer_6, data_6, "Strings: split ved komma"),
        (7, answer_7, data_7, "Lists: sidste 4 elementer"),
        (8, answer_8, data_8, "Lists: tal større end 50"),
        (9, answer_9, data_9, "Lists: omvendt rækkefølge"),
        (10, answer_10, data_10, "Lists: produkt af alle tal"),
        (11, answer_11, data_11, "Lists: find indeks"),
        (12, answer_12, data_12, "Lists: fordobl ulige tal"),
        (13, answer_13, data_13, "Tuples: antal elementer"),
        (14, answer_14, data_14, "Tuples: ældste person"),
        (15, answer_15, data_15, "Tuples: sammensæt tuples"),
        (16, answer_16, data_16, "Dicts: sorterede keys"),
        (17, answer_17, data_17, "Dicts: tjek om key findes"),
        (18, answer_18, data_18, "Dicts: byt keys og values"),
        (19, answer_19, data_19, "Dicts: zip to lister"),
        (20, answer_20, data_20, "Sets: difference"),
        (21, answer_21, data_21, "Sets: union"),
        (22, answer_22, data_22, "Sets: subset"),
        (23, answer_23, data_23, "Loops: fakultet"),
        (24, answer_24, data_24, "Loops: FizzBuzz"),
        (25, answer_25, data_25, "Loops: nested par"),
        (26, answer_26, data_26, "Exception: index out of range"),
        (27, answer_27, data_27, "Exception: konverter gyldige ints"),
        (28, answer_28, data_28, "Functions: palindrom"),
        (29, answer_29, data_29, "Functions: næststørste tal"),
        (30, answer_30, data_30, "File I/O: skriv og læs dict"),
        (31, answer_31, data_31, "Import: math.ceil"),
        (32, answer_32, data_32, "Import: json.dumps"),
        (33, answer_33, data_33, "Combo: IP request tælling"),
        (34, answer_34, data_34, "Combo: flest vokaler"),
        (35, answer_35, data_35, "Combo: positive/negative/zero"),
        (36, answer_36, data_36, "Combo: unikke kategorier"),
        (37, answer_37, data_37, "Combo: password validering"),
        (38, answer_38, data_38, "Combo: sortér efter score"),
        (39, answer_39, data_39, "Combo: Caesar cipher"),
        (40, answer_40, data_40, "Combo: bogstavfrekvenser"),
        (41, answer_41, data_41, "Ekstra: lige tal > gennemsnit"),
        (42, answer_42, data_42, "Ekstra: diagonal sum"),
        (43, answer_43, data_43, "Ekstra: key=value parsing"),
        (44, answer_44, data_44, "Ekstra: fjern dups, behold orden"),
        (45, answer_45, data_45, "Ekstra: hvert andet element"),
        (46, answer_46, data_46, "Ekstra: anagrammer"),
        (47, answer_47, data_47, "Ekstra: max score per person"),
        (48, answer_48, data_48, "Ekstra: title case"),
        (49, answer_49, data_49, "Ekstra: running sum"),
        (50, answer_50, data_50, "Ekstra: højeste gennemsnit"),
    ]

    passed = 0
    failed = 0
    skipped = 0

    print()
    print("=" * 60)
    print("  RESULTATER")
    print("=" * 60)

    for q_num, func, data, desc in _tests:
        try:
            d = copy.deepcopy(data)
            result = func(d)
            expected = _A[q_num]
            if result is None:
                print(f"  [SKIP] Q{q_num:02d}: {desc}")
                skipped += 1
            elif result == expected:
                print(f"  [PASS] Q{q_num:02d}: {desc}")
                passed += 1
            else:
                print(f"  [FAIL] Q{q_num:02d}: {desc}")
                print(f"         Dit svar: {result}")
                failed += 1
        except Exception as e:
            print(f"  [ERR]  Q{q_num:02d}: {desc}")
            print(f"         {type(e).__name__}: {e}")
            failed += 1

    # Cleanup file I/O test
    tmp = "/tmp/practice2_q30.txt"
    if os.path.exists(tmp):
        os.remove(tmp)

    print("=" * 60)
    print(
        f"  {passed} PASS / {failed} FAIL / {skipped} SKIP  (af {len(_tests)} opgaver)"
    )
    print("=" * 60)
    print()
