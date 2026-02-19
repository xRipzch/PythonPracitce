# pyright: basic
"""
=============================================================
  PYTHON EXAM PRACTICE 3
  Udfyld funktionerne - erstat 'pass' med din kode.
  Kør filen med:  python practice3.py
  Hver opgave printer PASS / FAIL / SKIP (hvis du ikke har udfyldt den endnu)
=============================================================
"""


# ============================================================
# SEKTION 1: LIST COMPREHENSIONS (Avanceret)
# ============================================================
# List comprehension = en kompakt måde at lave lister på.
#
# Grundform:
#   [udtryk for element in iterable]
#
# Med filter:
#   [udtryk for element in iterable if betingelse]
#
# Med transformation + filter:
#   [x * 2 for x in range(10) if x % 2 == 0]
#   -> [0, 4, 8, 12, 16]
#
# Nested comprehension (flatten):
#   [x for sublist in nested for x in sublist]
#   [[1,2],[3,4]] -> [1, 2, 3, 4]
#
# Med tuples:
#   [(x, x**2) for x in range(4)]
#   -> [(0, 0), (1, 1), (2, 4), (3, 9)]
# ============================================================

# Q1: Returner en liste med KVADRATTAL af alle LIGE tal fra 1 til data (inklusiv)
# Eksempel med data=10: [4, 16, 36, 64, 100]
data_1 = 20


def answer_1(my_var):
    pass


# Q2: Returner en liste af tuples: (tal, tal²) for tal 1 til data (inklusiv)
# Eksempel med data=3: [(1, 1), (2, 4), (3, 9)]
data_2 = 5


def answer_2(my_var):
    pass


# Q3: Flatten (fladgør) den nested liste til én liste med list comprehension
data_3 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]


def answer_3(my_var):
    pass


# Q4: Returner de strings der indeholder bogstavet 'e', konverteret til UPPERCASE
#     Behold den originale rækkefølge.
data_4 = ["apple", "banana", "cherry", "date", "fig", "grape"]


def answer_4(my_var):
    pass


# ============================================================
# SEKTION 2: DICT COMPREHENSIONS
# ============================================================
# Dict comprehension = kompakt måde at lave dictionaries.
#
# Grundform:
#   {key: value for element in iterable}
#
# Fra range:
#   {x: x**2 for x in range(5)}
#   -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#
# Med filter:
#   {k: v for k, v in d.items() if v > 10}
#
# Fra to lister med zip:
#   {k: v for k, v in zip(keys, values)}
# ============================================================

# Q5: Returner en dict med {tal: tal³} (kubiktal) for tal 1 til data (inklusiv)
# Eksempel med data=3: {1: 1, 2: 8, 3: 27}
data_5 = 6


def answer_5(my_var):
    pass


# Q6: Returner en NY dict med KUN de entries hvor value er STØRRE end 50
data_6 = {"a": 23, "b": 67, "c": 45, "d": 89, "e": 12}


def answer_6(my_var):
    pass


# Q7: Parse strengen til en dict. Format: "key=value,key=value,..."
# Eksempel: "a=1,b=2" -> {"a": "1", "b": "2"}
data_7 = "name=Alice,age=30,city=Copenhagen"


def answer_7(my_var):
    pass


# Q8: Merge to dicts. Ved konflikter (samme key): brug værdien fra den ANDEN dict.
data_8 = ({"a": 1, "b": 2, "c": 3}, {"b": 20, "d": 40})


def answer_8(my_var):
    pass


# ============================================================
# SEKTION 3: LAMBDA & SORTING (Avanceret)
# ============================================================
# Lambda er en "anonym funktion" - en funktion uden navn.
#
#   lambda x: x * 2         # fordobl
#   lambda x: x[1]          # tag andet element
#   lambda x: len(x)        # længde
#
# Bruges ofte med sorted():
#   sorted(lst, key=lambda x: x[1])     # sortér efter 2. element
#   sorted(lst, key=lambda x: len(x))   # sortér efter længde
#   sorted(lst, key=lambda x: x.lower()) # case-insensitive sort
#   sorted(lst, reverse=True)            # faldende orden
#
# Bruges med filter():
#   list(filter(lambda x: x > 5, [1, 8, 3, 9]))  -> [8, 9]
#
# Bruges med map():
#   list(map(lambda x: x * 2, [1, 2, 3]))  -> [2, 4, 6]
# ============================================================

# Q9: Sortér listen af tuples efter det ANDET element (score), STIGENDE
data_9 = [("alice", 85), ("bob", 72), ("charlie", 91), ("diana", 68)]


def answer_9(my_var):
    pass


# Q10: Sortér listen af strings efter deres LÆNGDE, korteste først
data_10 = ["python", "go", "javascript", "c", "ruby"]


def answer_10(my_var):
    pass


# Q11: Sortér listen af dicts efter "age" nøglen, STIGENDE
data_11 = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]


def answer_11(my_var):
    pass


# Q12: Sortér ordene i sætningen ALFABETISK (case insensitive), returner som string
# Hint: sorted() med key=lambda w: w.lower()
data_12 = "The Quick Brown Fox Jumps Over The Lazy Dog"


def answer_12(my_var):
    pass


# ============================================================
# SEKTION 4: STRING METODER (Avanceret)
# ============================================================
# Ekstra string-teknikker:
#
#   s.isdigit()          -> True hvis alle tegn er cifre
#   s.isalpha()          -> True hvis alle tegn er bogstaver
#   s.isalnum()          -> True hvis alle er bogstaver/cifre
#   s.isupper()          -> True hvis alle er STORE
#   s.islower()          -> True hvis alle er små
#
#   ord('a') -> 97       -> Unicode-nummer for tegn
#   chr(97) -> 'a'       -> Tegn fra Unicode-nummer
#
#   s.title()            -> "hello world" -> "Hello World"
#   s.capitalize()       -> "hello world" -> "Hello world"
#   s.center(20, '-')    -> "---hello world----"
# ============================================================

# Q13: Returner True hvis strengen er et PALINDROM (læses ens begge veje)
#      Ignorer mellemrum og store/små bogstaver.
# Eksempel: "Race Car" -> True, "Hello" -> False
data_13 = "Race Car"


def answer_13(my_var):
    pass


# Q14: Tæl antal VOKALER (a, e, i, o, u) i strengen (case insensitive)
data_14 = "Programming is awesome"


def answer_14(my_var):
    pass


# Q15: Fjern DUPLIKEREDE ord fra sætningen, behold FØRSTE forekomst, bevar rækkefølgen
# Eksempel: "the cat the dog" -> "the cat dog"
data_15 = "the cat sat on the mat the cat"


def answer_15(my_var):
    pass


# Q16: Konverter en "snake_case" string til "camelCase"
# Eksempel: "my_var_name" -> "myVarName"
# Hint: split ved _, capitalize alle undtagen det første, join
data_16 = "hello_world_foo_bar"


def answer_16(my_var):
    pass


# ============================================================
# SEKTION 5: NESTED DATA STRUCTURES (Indlejrede strukturer)
# ============================================================
# Data i den virkelige verden er ofte NESTED (indlejret):
#
#   Liste af dicts:
#     users = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
#     users[0]["name"]  -> "Alice"
#
#   Dict af lister:
#     data = {"fruits": ["apple", "banana"], "vegs": ["carrot"]}
#     data["fruits"][1]  -> "banana"
#
#   Dict af dicts:
#     config = {"db": {"host": "localhost", "port": 5432}}
#     config["db"]["port"]  -> 5432
#
# Iteration:
#   for user in users:
#       print(user["name"])
#
#   for category, items in data.items():
#       for item in items:
#           print(category, item)
# ============================================================

# Q17: Returner en liste med alle "email" værdier fra listen af dicts
data_17 = [
    {"name": "Alice", "email": "alice@test.com"},
    {"name": "Bob", "email": "bob@test.com"},
    {"name": "Charlie", "email": "charlie@test.com"},
]


def answer_17(my_var):
    pass


# Q18: Find NAVNET på personen med den HØJESTE score (på tværs af alle teams)
data_18 = {
    "team_a": [("Alice", 85), ("Bob", 72)],
    "team_b": [("Charlie", 91), ("Diana", 68)],
}


def answer_18(my_var):
    pass


# Q19: Returner SUMMEN af alle tal i den nested dict (alle values i alle sub-dicts)
data_19 = {"a": {"x": 10, "y": 20}, "b": {"x": 30, "y": 40}}


def answer_19(my_var):
    pass


# Q20: Grupér listen af tuples efter FØRSTE element.
#      Returner {kategori: [liste af anden-elementer]}
# Eksempel: [("a", 1), ("b", 2), ("a", 3)] -> {"a": [1, 3], "b": [2]}
data_20 = [
    ("fruit", "apple"),
    ("veggie", "carrot"),
    ("fruit", "banana"),
    ("veggie", "broccoli"),
    ("fruit", "cherry"),
]


def answer_20(my_var):
    pass


# ============================================================
# SEKTION 6: FUNKTIONER (Avanceret)
# ============================================================
# Mere avancerede funktioner og algoritmer.
#
# Fibonacci-sekvensen:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#   Hvert tal er summen af de to foregående.
#   fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)
#
# Primtal: et tal > 1 der kun er deleligt med 1 og sig selv.
#   2, 3, 5, 7, 11, 13, ...
#
# Faktorer af N: alle tal der går op i N.
#   Faktorer af 12: [1, 2, 3, 4, 6, 12]
#
# GCD (Greatest Common Divisor / Største fælles divisor):
#   GCD(12, 8) = 4
# ============================================================

# Q21: Returner det N'te Fibonacci-tal (0-indekseret)
# fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, ...
data_21 = 10


def answer_21(my_var):
    pass


# Q22: Returner True hvis data er et primtal, ellers False
data_22 = 97


def answer_22(my_var):
    pass


# Q23: Returner en SORTERET liste af alle faktorer af data
# Eksempel med data=12: [1, 2, 3, 4, 6, 12]
data_23 = 36


def answer_23(my_var):
    pass


# Q24: Returner GCD (største fælles divisor) af de to tal
# Hint: Brug Euclids algoritme: gcd(a, b) = gcd(b, a % b) indtil b == 0
data_24 = (48, 18)


def answer_24(my_var):
    pass


# ============================================================
# SEKTION 7: ENUMERATE & ZIP
# ============================================================
# enumerate() giver (indeks, element) par:
#   for i, val in enumerate(["a", "b", "c"]):
#       print(i, val)  # 0 a, 1 b, 2 c
#
# zip() parrer elementer fra flere iterables:
#   list(zip([1,2,3], ["a","b","c"]))
#   -> [(1, "a"), (2, "b"), (3, "c")]
#
# zip() med 3+ lister:
#   list(zip(names, scores, grades))
#   -> [("Alice", 85, "A"), ("Bob", 92, "A+"), ...]
#
# zip() stopper ved den korteste liste.
# ============================================================

# Q25: Brug enumerate - returner en dict med {indeks: værdi} for alle elementer > 20
data_25 = [5, 35, 12, 42, 8, 28]


def answer_25(my_var):
    pass


# Q26: Zip de to lister sammen. Returner en liste af tuples hvor SUMMEN > 10
# Eksempel: ([1,5], [6,3]) -> par: (1,6)=7, (5,3)=8 -> ingen > 10 -> []
data_26 = ([1, 5, 3, 8, 2], [6, 3, 9, 4, 7])


def answer_26(my_var):
    pass


# Q27: Zip tre lister til en liste af dicts med keys: "name", "score", "grade"
data_27 = (["Alice", "Bob", "Charlie"], [85, 92, 78], ["A", "A+", "B+"])


def answer_27(my_var):
    pass


# Q28: Find ALLE indekser hvor værdien forekommer i listen
# Data er en tuple: (listen, søgeværdi)
data_28 = ([10, 20, 30, 20, 40, 20], 20)


def answer_28(my_var):
    pass


# ============================================================
# SEKTION 8: KOMBINATIONS-OPGAVER
# ============================================================
# Her blandes ALLE koncepter - ligesom til eksamen!
# ============================================================

# Q29: Caesar cipher DECODE: skift hvert bogstav N pladser TILBAGE i alfabetet
#      Data er en tuple: (krypteret_tekst, N). Kun små bogstaver.
# Eksempel: ("def", 3) -> "abc"
data_29 = ("khoor", 3)


def answer_29(my_var):
    pass


# Q30: Returner de TOP 3 hyppigste ord som en liste af tuples: [(ord, antal), ...]
#      Sorteret efter antal FALDENDE. Ved lige antal: behold rækkefølgen fra teksten.
data_30 = "the cat sat on the mat the cat sat"


def answer_30(my_var):
    pass


# Q31: ROT13 encode: skift hvert bogstav 13 pladser frem.
#      Bevar store/små bogstaver. Ikke-bogstaver forbliver uændrede.
# Eksempel: "Ab!" -> "No!"
data_31 = "Hello World"


def answer_31(my_var):
    pass


# Q32: Returner True hvis strengen er en gyldig IPv4-adresse.
#      Krav: 4 oktetter adskilt af '.', hver oktet er et tal mellem 0 og 255.
data_32 = "192.168.1.1"


def answer_32(my_var):
    pass


# Q33: Konverter en BINÆR string til et DECIMALTAL (heltal)
# Eksempel: "1010" -> 10
data_33 = "11010"


def answer_33(my_var):
    pass


# Q34: Konverter et decimaltal til en BINÆR string (uden "0b" prefix)
# Eksempel: 10 -> "1010"
data_34 = 42


def answer_34(my_var):
    pass


# Q35: Matrice ADDITION: læg to matricer sammen element for element
# Eksempel: ([[1,0],[0,1]], [[1,1],[1,1]]) -> [[2,1],[1,2]]
data_35 = ([[1, 2], [3, 4]], [[5, 6], [7, 8]])


def answer_35(my_var):
    pass


# Q36: Find elementer der er FÆLLES i ALLE tre lister, returner sorteret
data_36 = ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [5, 4, 8, 9, 10])


def answer_36(my_var):
    pass


# Q37: Inverter en dict der har lister som values.
#      Input:  {person: [skills]}
#      Output: {skill: [persons]}  (personer sorteret alfabetisk)
data_37 = {
    "alice": ["python", "java"],
    "bob": ["python", "go"],
    "charlie": ["java", "go"],
}


def answer_37(my_var):
    pass


# Q38: Grupér ord efter deres LÆNGDE.
#      Returner {længde: [ord]}. Behold ordenes originale rækkefølge.
data_38 = ["hi", "the", "cat", "a", "sat", "on", "it"]


def answer_38(my_var):
    pass


# Q39: Parse HTTP-log og tæl HTTP-metoder (GET, POST, etc.)
#      Hver linje har format: "METHOD /path"
#      Returner {method: antal}
data_39 = "GET /index\nPOST /login\nGET /about\nGET /index\nDELETE /user\nPOST /login"


def answer_39(my_var):
    pass


# Q40: Find alle personer der har ALLE karakterer >= 80.
#      Data er en liste af (navn, karakter) tuples.
#      Returner en sorteret liste af navne.
data_40 = [
    ("Alice", 85),
    ("Alice", 92),
    ("Alice", 78),
    ("Bob", 88),
    ("Bob", 91),
    ("Charlie", 82),
    ("Charlie", 95),
]


def answer_40(my_var):
    pass


# Q41: Konverter en liste af Celsius-temperaturer til Fahrenheit.
#      Formel: F = C * 9/5 + 32
#      Afrund til 1 decimal med round(x, 1)
data_41 = [0, 20, 37, 100]


def answer_41(my_var):
    pass


# Q42: Find det LÆNGSTE FÆLLES PREFIX i en liste af strings
# Eksempel: ["flower", "flow", "flight"] -> "fl"
data_42 = ["interview", "internet", "internal", "interpret"]


def answer_42(my_var):
    pass


# Q43: Lav et tekst-HISTOGRAM. For hvert key i dict'en, lav en linje: "key: ###..."
#      Antal '#' = value. Linjer adskilles med "\n". Behold dict'ens rækkefølge.
# Eksempel: {"a": 3, "b": 1} -> "a: ###\nb: #"
data_43 = {"python": 5, "java": 3, "go": 7}


def answer_43(my_var):
    pass


# Q44: Returner True hvis ALLE parenteser er BALANCEREDE: (), [], {}
# Eksempel: "{[()]}" -> True, "([)]" -> False
data_44 = "{[()]}"


def answer_44(my_var):
    pass


# Q45: Konverter et romertal til et heltal.
#      I=1, V=5, X=10, L=50, C=100, D=500, M=1000
#      Regel: Hvis et mindre tal står FØR et større, trækkes det fra.
#      IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
data_45 = "XLII"


def answer_45(my_var):
    pass


# Q46: Returner intersection (fællesmængde) af alle sets i listen
data_46 = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]


def answer_46(my_var):
    pass


# Q47: Data er en liste af (navn, beløb) transaktioner.
#      Returner en dict med {navn: netto_saldo} (summen af alle beløb per person)
data_47 = [("Alice", 100), ("Bob", -50), ("Alice", -30), ("Bob", 80), ("Charlie", 50)]


def answer_47(my_var):
    pass


# Q48: Returner det MEST HYPPIGE element. Ved uafgjort: returner det MINDSTE.
# Eksempel: [1, 2, 2, 3, 3] -> 2 (2 og 3 har begge 2 forekomster, 2 er mindst)
data_48 = [1, 2, 2, 3, 3, 4]


def answer_48(my_var):
    pass


# Q49: Run-length encoding: komprimér gentagne tegn.
# Eksempel: "aabbc" -> "a2b2c1"
data_49 = "aaabbbccddddee"


def answer_49(my_var):
    pass


# Q50: Data er en matrice (liste af lister). Returner en liste med KOLONNE-summer.
# Eksempel: [[1,2],[3,4]] -> [4, 6]  (kolonne 0: 1+3=4, kolonne 1: 2+4=6)
data_50 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def answer_50(my_var):
    pass


# ============================================================
# ============================================================
#  TEST RUNNER - Rør ikke ved koden herunder!
#  Kør: python practice3.py
# ============================================================
# ============================================================

if __name__ == "__main__":
    import base64
    import copy
    import os
    import pickle

    _E = b"gAWVswQAAAAAAAB9lChLAV2UKEsESxBLJEtAS2RLkEvETQABTUQBTZABZUsCXZQoSwFLAYaUSwJLBIaUSwNLCYaUSwRLEIaUSwVLGYaUZUsDXZQoSwFLAksDSwRLBUsGSwdLCEsJZUsEXZQojAVBUFBMRZSMBkNIRVJSWZSMBERBVEWUjAVHUkFQRZRlSwV9lChLAUsBSwJLCEsDSxtLBEtASwVLfUsGS9h1SwZ9lCiMAWKUS0OMAWSUS1l1Swd9lCiMBG5hbWWUjAVBbGljZZSMA2FnZZSMAjMwlIwEY2l0eZSMCkNvcGVuaGFnZW6UdUsIfZQojAFhlEsBaBBLFIwBY5RLA2gRSyh1SwldlCiMBWRpYW5hlEtEhpSMA2JvYpRLSIaUjAVhbGljZZRLVYaUjAdjaGFybGlllEtbhpRlSwpdlChoG4wCZ2+UjARydWJ5lIwGcHl0aG9ulIwKamF2YXNjcmlwdJRlSwtdlCh9lChoE4wDQm9ilGgVSxl1fZQoaBNoFGgVSx51fZQoaBOMB0NoYXJsaWWUaBVLI3VlSwyMK0Jyb3duIERvZyBGb3ggSnVtcHMgTGF6eSBPdmVyIFF1aWNrIFRoZSBUaGWUSw2ISw5LCEsPjBJ0aGUgY2F0IHNhdCBvbiBtYXSUSxCMEGhlbGxvV29ybGRGb29CYXKUSxFdlCiMDmFsaWNlQHRlc3QuY29tlIwMYm9iQHRlc3QuY29tlIwQY2hhcmxpZUB0ZXN0LmNvbZRlSxJoL0sTS2RLFH2UKIwFZnJ1aXSUXZQojAVhcHBsZZSMBmJhbmFuYZSMBmNoZXJyeZRljAZ2ZWdnaWWUXZQojAZjYXJyb3SUjAhicm9jY29saZRldUsVSzdLFohLF12UKEsBSwJLA0sESwZLCUsMSxJLJGVLGEsGSxl9lChLAUsjSwNLKksFSxx1SxpdlChoBUsISwSGlGVLG12UKH2UKGgTaBSMBXNjb3JllEtVjAVncmFkZZSMAUGUdX2UKGgTaCxoR0tcaEiMAkErlHV9lChoE2gvaEdLTmhIjAJCK5R1ZUscXZQoSwFLA0sFZUsdjAVoZWxsb5RLHl2UKIwDdGhllEsDhpSMA2NhdJRLAoaUjANzYXSUSwKGlGVLH4wLVXJ5eWIgSmJleXGUSyCISyFLGksijAYxMDEwMTCUSyNdlChdlChLBksIZV2UKEsKSwxlZUskXZQoSwRLBWVLJX2UKGgoXZQoaCFoH2WMBGphdmGUXZQoaCFoI2VoJl2UKGgfaCNldUsmfZQoSwJdlCiMAmhplIwCb26UjAJpdJRlSwNdlChoUWhTaFVlSwFdlGgaYXVLJ32UKIwDR0VUlEsDjARQT1NUlEsCjAZERUxFVEWUSwF1SyhdlChoLGgvZUspXZQoR0BAAAAAAAAAR0BRAAAAAAAAR0BYpmZmZmZmR0BqgAAAAAAAZUsqjAVpbnRlcpRLK4wjcHl0aG9uOiAjIyMjIwpqYXZhOiAjIyMKZ286ICMjIyMjIyOUSyyISy1LKksuj5QoSwNLBJBLL32UKGgUS0ZoLEseaC9LMnVLMEsCSzGMCmEzYjNjMmQ0ZTKUSzJdlChLDEsPSxJldS4="
    _A = pickle.loads(base64.b64decode(_E))

    _tests = [
        (1, answer_1, data_1, "Comprehension: kvadrat af lige tal"),
        (2, answer_2, data_2, "Comprehension: (tal, tal²) tuples"),
        (3, answer_3, data_3, "Comprehension: flatten nested list"),
        (4, answer_4, data_4, "Comprehension: filter + uppercase"),
        (5, answer_5, data_5, "Dict comp: kubiktal"),
        (6, answer_6, data_6, "Dict comp: filter values > 50"),
        (7, answer_7, data_7, "Dict comp: parse key=value string"),
        (8, answer_8, data_8, "Dict comp: merge to dicts"),
        (9, answer_9, data_9, "Sorting: tuples efter score"),
        (10, answer_10, data_10, "Sorting: strings efter længde"),
        (11, answer_11, data_11, "Sorting: dicts efter age"),
        (12, answer_12, data_12, "Sorting: ord alfabetisk"),
        (13, answer_13, data_13, "Strings: palindrom check"),
        (14, answer_14, data_14, "Strings: tæl vokaler"),
        (15, answer_15, data_15, "Strings: fjern dup ord"),
        (16, answer_16, data_16, "Strings: snake_case -> camelCase"),
        (17, answer_17, data_17, "Nested: extract emails"),
        (18, answer_18, data_18, "Nested: højeste score"),
        (19, answer_19, data_19, "Nested: sum af nested dict"),
        (20, answer_20, data_20, "Nested: grupér tuples"),
        (21, answer_21, data_21, "Functions: fibonacci"),
        (22, answer_22, data_22, "Functions: primtal"),
        (23, answer_23, data_23, "Functions: faktorer"),
        (24, answer_24, data_24, "Functions: GCD"),
        (25, answer_25, data_25, "Enumerate: filter med indeks"),
        (26, answer_26, data_26, "Zip: filter par med sum > 10"),
        (27, answer_27, data_27, "Zip: tre lister til dicts"),
        (28, answer_28, data_28, "Enumerate: find alle indekser"),
        (29, answer_29, data_29, "Combo: Caesar decode"),
        (30, answer_30, data_30, "Combo: top 3 ordfrekvens"),
        (31, answer_31, data_31, "Combo: ROT13"),
        (32, answer_32, data_32, "Combo: valider IP-adresse"),
        (33, answer_33, data_33, "Combo: binær til decimal"),
        (34, answer_34, data_34, "Combo: decimal til binær"),
        (35, answer_35, data_35, "Combo: matrice addition"),
        (36, answer_36, data_36, "Combo: fælles i 3 lister"),
        (37, answer_37, data_37, "Combo: inverter dict af lister"),
        (38, answer_38, data_38, "Combo: grupér efter ordlængde"),
        (39, answer_39, data_39, "Combo: HTTP metode-tælling"),
        (40, answer_40, data_40, "Combo: alle karakterer >= 80"),
        (41, answer_41, data_41, "Combo: Celsius til Fahrenheit"),
        (42, answer_42, data_42, "Combo: længste fælles prefix"),
        (43, answer_43, data_43, "Combo: tekst-histogram"),
        (44, answer_44, data_44, "Combo: balancerede parenteser"),
        (45, answer_45, data_45, "Combo: romertal til int"),
        (46, answer_46, data_46, "Combo: intersection af sets"),
        (47, answer_47, data_47, "Combo: netto saldo"),
        (48, answer_48, data_48, "Combo: mest hyppige element"),
        (49, answer_49, data_49, "Combo: run-length encoding"),
        (50, answer_50, data_50, "Combo: kolonne-summer"),
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

    print("=" * 60)
    print(
        f"  {passed} PASS / {failed} FAIL / {skipped} SKIP  (af {len(_tests)} opgaver)"
    )
    print("=" * 60)
    print()
