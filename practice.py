"""
=============================================================
  PYTHON EXAM PRACTICE
  Udfyld funktionerne - erstat 'pass' med din kode.
  Kør filen med:  python practice.py
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

# Q1: Returner data ganget med 2
data_1 = 16
def answer_1(my_var):
    pass

# Q2: Returner data i UPPERCASE
data_2 = "this class simply rules"
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

# Q3: Returner teksten i omvendt rækkefølge (baglæns)
data_3 = "There is nothing called too much work"
def answer_3(my_var):
    pass

# Q4: Erstat 'be' med 'python' i sætningen
data_4 = "To be, or not to be, that is the question"
def answer_4(my_var):
    pass

# Q5: Returner sætningen med 'the star' erstattet af 'the rats'
data_5 = "I spend all night staring at the star"
def answer_5(my_var):
    pass

# Q6: Returner sætningen hvor hvert ORD er vendt om, men ordene beholder deres plads
# Eksempel: "hello world" -> "olleh dlrow"
data_6 = "When nothing makes sence then have another look"
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
#   lst[5]   -> sjette element
#
# Slicing:
#   lst[:3]    -> de første 3 elementer
#   lst[-4:]   -> de sidste 4 elementer
#   lst[::-1]  -> listen baglæns
#
# Vigtige metoder:
#   lst.append(x)      -> tilføj til slutningen
#   lst.insert(i, x)   -> indsæt ved indeks i
#   lst.remove(x)      -> fjern første forekomst af x
#   lst.pop(i)         -> fjern og returner element ved indeks i
#   sorted(lst)        -> returner NY sorteret liste (original uændret)
#   lst.sort()         -> sorter IN-PLACE (returnerer None!)
#   len(lst)           -> antal elementer
#   sum(lst)           -> summen af alle tal
#
# List comprehension:
#   [x * 2 for x in lst]            -> fordobl alle
#   [x for x in lst if x > 5]       -> filtrer
#   [x * 2 for x in lst if x > 5]   -> filtrer OG transformer
# ============================================================

# Q7: Returner den sorterede liste
data_7 = [5, 3, 8, 3, 76, 332, 5, 0, 3]
def answer_7(my_var):
    pass

# Q8: Returner en liste med kun de første 3 elementer
data_8 = [26, 43, 68, 53, 32, 85, 50, 63]
def answer_8(my_var):
    pass

# Q9: Returner en liste hvor hvert tal er ganget med 5
data_9 = [26, 32, 43, 50, 53, 63, 68, 85]
def answer_9(my_var):
    pass

# Q10: Returner værdien af det 6. element
data_10 = [10, 25, 34, 25, 160, 250, 315]
def answer_10(my_var):
    pass

# Q11: Returner en sorteret liste hvor duplikaterne er fjernet
data_11 = [7, 3, 2, 6, 3, 1, 6, 85, 7, 3, 6, 0, 3, 6, 5]
def answer_11(my_var):
    pass

# Q12: Returner summen af alle tallene i listen
data_12 = [23, 3413, 4534, 1345, 1, 23, 1434, 112]
def answer_12(my_var):
    pass

# Q13: Returner en liste med 20 værdier, startende fra data og +5 for hver
# Eksempel med data=10: [10, 15, 20, 25, ...]
data_13 = 25
def answer_13(my_var):
    pass

# Q14: Returner en liste med kun de LIGE tal (even numbers) fra listen
data_14 = [1, 14, 3, 22, 5, 8, 17, 30, 11, 42]
def answer_14(my_var):
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
#   a, b = (1,2)  -> unpacking
#
# Hvornår bruger man tuples?
#   - Faste datapunkter: (ip, port), (x, y), (navn, telefon)
#   - Returner flere værdier fra en funktion
#   - Som keys i dictionaries
# ============================================================

# Q15: Data er en liste af tuples med (ip, connections).
#      Returner antal connections for IP '192.168.1.212'
data_15 = [('192.168.1.24', 23), ('192.168.1.53', 2), ('192.168.1.212', 34), ('192.168.1.243', 54)]
def answer_15(my_var):
    pass

# Q16: Data er en string med "navn:tlf,navn:tlf,..."
#      Returner en liste af tuples: [("navn","tlf"), ("navn","tlf"), ...]
data_16 = "jens:32242526,peter:23451234,mogens:98768765,lars:98989898,morten:26483277"
def answer_16(my_var):
    pass

# Q17: Returner en liste med 10 kopier af tuplen
data_17 = ('x', 'y')
def answer_17(my_var):
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
#   d.pop(key)          -> slet og returner værdi
#   d.keys()            -> alle keys
#   d.values()          -> alle values
#   d.items()           -> alle (key, value) par
#   d.update({...})     -> flet anden dict ind
#   key in d            -> True hvis key findes
#   len(d)              -> antal par
#
# Dict comprehension:
#   {k: v * 2 for k, v in d.items()}
#
# dict() + zip():
#   dict(zip(keys_list, values_list))
# ============================================================

# Q18: Returner dictionary med nøglen '192.168.1.243' fjernet
data_18 = {'192.168.1.53': 2, '192.168.1.24': 23, '192.168.1.243': 54, '192.168.1.212': 34}
def answer_18(my_var):
    pass

# Q19: Tilføj nøglen 'yellow' med værdien 22 og returner resultatet
data_19 = {'blue': 32, 'red': 23, 'black': 43, 'green': 76}
def answer_19(my_var):
    pass

# Q20: Data er en liste af tuples: [(navn, episode), ...]
#      Returner en dictionary hvor episode er key og navn er value
data_20 = [("Seinfeld", "S01E01"), ("Friends", "S02E05"), ("Lost", "S03E10")]
def answer_20(my_var):
    pass

# Q21: Returner summen af alle VALUES i dictionaryen
data_21 = {"a": 10, "b": 20, "c": 30, "d": 40}
def answer_21(my_var):
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
#   len(s)            -> antal elementer
#
# Konvertering:
#   set(my_list)      -> fjerner duplikater
#   sorted(my_set)    -> sorteret liste fra set
#
# Sets er gode til:
#   - Fjerne duplikater: set([1,2,2,3]) -> {1,2,3}
#   - Hurtigt tjekke om element findes
#   - Finde fælles/unikke elementer mellem samlinger
# ============================================================

# Q22: Returner et set med alle unikke IP-adresser fra log-linjerne
#      (IP-adressen er det FØRSTE felt i hver linje)
data_22 = """64.242.88.10 - - [08/Mar/2004:10:40:09] "GET /twiki" 200 8540
64.242.88.10 - - [08/Mar/2004:10:45:25] "GET /twiki" 200 4287
10.0.0.153 - - [08/Mar/2004:10:48:02] "GET /" 304 -
10.0.0.153 - - [08/Mar/2004:10:48:05] "GET /cgi" 200 2987
128.227.88.79 - - [08/Mar/2004:11:06:20] "GET /twiki" 200 4034
10.2.0.153 - - [08/Mar/2004:10:48:06] "GET /cgi" 200 7254
64.242.88.10 - - [08/Mar/2004:11:09:24] "GET /twiki" 200 12846"""
def answer_22(my_var):
    pass

# Q23: Returner et set med elementer der findes i BEGGE lister (intersection)
data_23 = ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
def answer_23(my_var):
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

# Q24: Brug en loop til at returnere summen af alle LIGE tal i listen
data_24 = [3, 7, 2, 8, 15, 22, 31, 40, 5, 12]
def answer_24(my_var):
    pass

# Q25: Brug nested loops til at lave en flad liste fra den nested liste
# Eksempel: [[1,2],[3,4]] -> [1,2,3,4]
data_25 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def answer_25(my_var):
    pass

# Q26: Returner en liste af tal fra 1 til 100 som IKKE er delelige med data
# Eksempel med data=10: [1,2,3,4,5,6,7,8,9,11,12,...,99]
data_26 = 7
def answer_26(my_var):
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

# Q27: Prøv at konvertere data til int med int().
#      Returner tallet hvis det lykkes, ellers returner -1
data_27 = "abc123"
def answer_27(my_var):
    pass

# Q28: Prøv at dividere 100 med data.
#      Returner resultatet hvis det lykkes, ellers returner "error"
data_28 = 0
def answer_28(my_var):
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

# Q29: Returner (min, max) fra listen som en tuple
data_29 = [5, 3, 9, 1, 7]
def answer_29(my_var):
    pass

# Q30: Returner True hvis data er et primtal, ellers False
# Et primtal er kun deleligt med 1 og sig selv (1 er IKKE et primtal)
data_30 = 7
def answer_30(my_var):
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

# Q31: Skriv hvert element fra listen til /tmp/practice_q31.txt (et per linje).
#      Læs filen tilbage og returner en liste af linjer UDEN newlines.
data_31 = ["alpha", "beta", "gamma"]
def answer_31(my_var):
    pass


# ============================================================
# SEKTION 11: IMPORTING MODULES (Importere moduler)
# ============================================================
# Import hele modulet:
#   import math
#   math.sqrt(16)       -> 4.0
#
# Import specifik funktion:
#   from math import sqrt
#   sqrt(16)
#
# Import med alias:
#   import datetime as dt
#
# Nyttige standardmoduler:
#   math     -> sqrt, pi, floor, ceil
#   os       -> filstier, miljøvariabler
#   sys      -> argv, path
#   random   -> randint, choice, shuffle
#   json     -> loads (parse), dumps (serialize)
#   re       -> regular expressions
# ============================================================

# Q32: Brug math modulet til at returnere kvadratroden af data
data_32 = 144
def answer_32(my_var):
    pass

# Q33: Brug json modulet til at parse JSON-strengen til en dict
data_33 = '{"name": "Alice", "age": 30}'
def answer_33(my_var):
    pass


# ============================================================
# SEKTION 12: KOMBINATIONS-OPGAVER
# ============================================================
# Her blandes flere koncepter - ligesom til eksamen!
# ============================================================

# Q34: Returner en dict med ordtællinger: {"ord": antal}
# Eksempel: "a b a" -> {"a": 2, "b": 1}
data_34 = "hello world hello python world hello"
def answer_34(my_var):
    pass

# Q35: Returner en liste af navne der starter med 'A', konverteret til UPPERCASE
#      Behold den originale rækkefølge.
data_35 = ["Alice", "Bob", "Anna", "Charlie", "Alex"]
def answer_35(my_var):
    pass

# Q36: Data er en string med log-linjer.
#      Returner en dict med {status_kode: antal} (status_kode er næst-sidste felt)
# Eksempel linje: '10.0.0.1 - - [dato] "GET /path" 200 1234'
#                  status_kode = "200"
data_36 = """64.242.88.10 - - [08/Mar/2004:10:40:09] "GET /twiki" 200 8540
10.0.0.153 - - [08/Mar/2004:10:48:02] "GET /" 304 -
10.0.0.153 - - [08/Mar/2004:10:48:05] "GET /cgi" 200 2987
128.227.88.79 - - [08/Mar/2004:11:06:20] "GET /twiki" 404 4034
10.2.0.153 - - [08/Mar/2004:10:48:06] "GET /cgi" 200 7254"""
def answer_36(my_var):
    pass

# Q37: Data er en string med "^v<>" symboler.
#      ^ = etage op (+1), v = etage ned (-1)
#      > = rum til højre (+1), < = rum til venstre (-1)
#      Returner en tuple: (etage, rum)
data_37 = "^^>v>>^<"
def answer_37(my_var):
    pass


# ============================================================
# SEKTION 13: EKSTRA ØVELSER
# ============================================================

# Q38: Returner en liste af kvadrattal fra 1² til N² (inklusiv)
# Eksempel med data=5: [1, 4, 9, 16, 25]
data_38 = 10
def answer_38(my_var):
    pass

# Q39: Tæl antal gange bogstavet 'e' forekommer (CASE INSENSITIVE - både 'E' og 'e' tæller)
data_39 = "Excellence is not a skill It is an attitude"
def answer_39(my_var):
    pass

# Q40: Du får to dictionaries i en tuple. Merge dem til én.
#      Ved konflikter (samme key): behold den HØJESTE value.
data_40 = ({"a": 1, "b": 5, "c": 3}, {"b": 2, "c": 7, "d": 4})
def answer_40(my_var):
    pass

# Q41: Brug enumerate - returner en dict med {indeks: værdi} for alle elementer > 10
data_41 = [5, 15, 3, 22, 8, 31]
def answer_41(my_var):
    pass

# Q42: Data er en liste af strings "navn:score".
#      Returner NAVNET på den person med den højeste score.
data_42 = ["Alice:85", "Bob:92", "Charlie:78", "Diana:95"]
def answer_42(my_var):
    pass

# Q43: Data er en string med komma-separerede tal.
#      Returner gennemsnittet som float, afrundet til 2 decimaler.
data_43 = "12,35,22,17,43,8"
def answer_43(my_var):
    pass

# Q44: Data er en liste af dicts med "name" og "category".
#      Grupér dem og returner {category: [liste af names]}
data_44 = [
    {"name": "Apple", "category": "fruit"},
    {"name": "Carrot", "category": "vegetable"},
    {"name": "Banana", "category": "fruit"},
    {"name": "Broccoli", "category": "vegetable"},
    {"name": "Cherry", "category": "fruit"}
]
def answer_44(my_var):
    pass

# Q45: Fordel tallene i to grupper og returner {"even": [...], "odd": [...]}
#      Behold den originale rækkefølge.
data_45 = [1, 2, 3, 4, 5, 6, 7, 8]
def answer_45(my_var):
    pass

# Q46: Data er en liste af tuples: (produkt, pris, antal)
#      Returner den totale værdi (sum af pris * antal for alle produkter)
data_46 = [("apple", 2.5, 3), ("banana", 1.5, 5), ("cherry", 4.0, 2)]
def answer_46(my_var):
    pass

# Q47: Data er en multiline string.
#      Returner den LÆNGSTE linje (flest tegn).
data_47 = "short\na bit longer\nthe longest line here\nmedium"
def answer_47(my_var):
    pass

# Q48: Returner det element der forekommer FLEST gange i listen.
data_48 = ["10.0.0.1", "192.168.1.1", "10.0.0.1", "172.16.0.1", "10.0.0.1", "192.168.1.1"]
def answer_48(my_var):
    pass

# Q49: Data er en matrice (liste af lister). Returner den TRANSPONEREDE matrice.
# Transponering: rækker bliver til kolonner og omvendt.
# Eksempel: [[1,2],[3,4]] -> [[1,3],[2,4]]
data_49 = [[1, 2, 3], [4, 5, 6]]
def answer_49(my_var):
    pass

# Q50: Data er en liste af tuples: (elev, fag, karakter)
#      Returner en dict med {elev: gennemsnitskarakter} (som float)
data_50 = [
    ("Alice", "math", 90),
    ("Bob", "math", 75),
    ("Alice", "english", 84),
    ("Bob", "english", 81),
    ("Alice", "science", 78)
]
def answer_50(my_var):
    pass


# ============================================================
# ============================================================
#  TEST RUNNER - Rør ikke ved koden herunder!
#  Kør: python practice.py
# ============================================================
# ============================================================

if __name__ == "__main__":
    import base64, pickle, copy, os

    _E = b"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"
    _A = pickle.loads(base64.b64decode(_E))

    _tests = [
        (1,  answer_1,  data_1,  "Variabler: data * 2"),
        (2,  answer_2,  data_2,  "Variabler: uppercase"),
        (3,  answer_3,  data_3,  "Strings: reverse"),
        (4,  answer_4,  data_4,  "Strings: replace be->python"),
        (5,  answer_5,  data_5,  "Strings: the star -> the rats"),
        (6,  answer_6,  data_6,  "Strings: reverse hvert ord"),
        (7,  answer_7,  data_7,  "Lists: sorted"),
        (8,  answer_8,  data_8,  "Lists: første 3 elementer"),
        (9,  answer_9,  data_9,  "Lists: gange med 5"),
        (10, answer_10, data_10, "Lists: 6. element"),
        (11, answer_11, data_11, "Lists: sorted uden duplikater"),
        (12, answer_12, data_12, "Lists: sum"),
        (13, answer_13, data_13, "Lists: 20 værdier +5"),
        (14, answer_14, data_14, "Lists: kun lige tal"),
        (15, answer_15, data_15, "Tuples: find IP connections"),
        (16, answer_16, data_16, "Tuples: string -> liste af tuples"),
        (17, answer_17, data_17, "Tuples: 10 kopier"),
        (18, answer_18, data_18, "Dicts: fjern key"),
        (19, answer_19, data_19, "Dicts: tilføj key"),
        (20, answer_20, data_20, "Dicts: tuples -> dict"),
        (21, answer_21, data_21, "Dicts: sum af values"),
        (22, answer_22, data_22, "Sets: unikke IPs"),
        (23, answer_23, data_23, "Sets: intersection"),
        (24, answer_24, data_24, "Loops: sum af lige tal"),
        (25, answer_25, data_25, "Loops: flatten nested list"),
        (26, answer_26, data_26, "Loops: tal ikke delelige med N"),
        (27, answer_27, data_27, "Exception: int() fejler"),
        (28, answer_28, data_28, "Exception: division med 0"),
        (29, answer_29, data_29, "Functions: min/max tuple"),
        (30, answer_30, data_30, "Functions: primtal"),
        (31, answer_31, data_31, "File I/O: skriv og læs"),
        (32, answer_32, data_32, "Import: math.sqrt"),
        (33, answer_33, data_33, "Import: json.loads"),
        (34, answer_34, data_34, "Combo: ordtælling"),
        (35, answer_35, data_35, "Combo: filter + uppercase"),
        (36, answer_36, data_36, "Combo: log status tælling"),
        (37, answer_37, data_37, "Combo: ^v<> etage/rum"),
        (38, answer_38, data_38, "Ekstra: kvadrattal"),
        (39, answer_39, data_39, "Ekstra: tæl bogstav"),
        (40, answer_40, data_40, "Ekstra: merge dicts"),
        (41, answer_41, data_41, "Ekstra: enumerate filter"),
        (42, answer_42, data_42, "Combo: højeste score"),
        (43, answer_43, data_43, "Combo: gennemsnit fra string"),
        (44, answer_44, data_44, "Combo: grupér efter kategori"),
        (45, answer_45, data_45, "Combo: even/odd split"),
        (46, answer_46, data_46, "Combo: total pris*antal"),
        (47, answer_47, data_47, "Combo: længste linje"),
        (48, answer_48, data_48, "Combo: mest hyppige element"),
        (49, answer_49, data_49, "Combo: transponer matrice"),
        (50, answer_50, data_50, "Combo: elev-gennemsnit"),
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
    tmp = "/tmp/practice_q31.txt"
    if os.path.exists(tmp):
        os.remove(tmp)

    print("=" * 60)
    print(f"  {passed} PASS / {failed} FAIL / {skipped} SKIP  (af {len(_tests)} opgaver)")
    print("=" * 60)
    print()
