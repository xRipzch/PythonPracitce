# pyright: basic
"""
=============================================================
  PYTHON EXAM PRACTICE 4 — BASICS & BEYOND
  Udfyld funktionerne - erstat 'pass' med din kode.
  Kør filen med:  python practice4.py
  Hver opgave printer PASS / FAIL / SKIP
=============================================================
"""


# ============================================================
# SEKTION 1: INPUT, TYPE CASTING & GRUNDLÆGGENDE TYPER
# ============================================================
# input() læser en string fra terminalen:
#   name = input("Hvad hedder du? ")   -> altid en string!
#   age = int(input("Alder? "))        -> cast til int
#
# Type casting (konvertering):
#   int("42")       -> 42          (string til int)
#   float("3.14")   -> 3.14        (string til float)
#   str(42)         -> "42"        (int til string)
#   int(3.9)        -> 3           (float til int, RUNDER NED)
#   int("3.9")      -> FEJL!       (kan ikke direkte, brug float() først)
#   bool(0)         -> False       (0, "", [], None er False)
#   bool(1)         -> True        (alt andet er True)
#
# type() checker typen:
#   type(42)        -> <class 'int'>
#   type("hi")      -> <class 'str'>
#
# isinstance() checker om noget er en bestemt type:
#   isinstance(42, int)     -> True
#   isinstance("hi", str)   -> True
# ============================================================

# Q1: Simuler terminal input: data er strengen "25".
#     Cast den til int og returner resultatet.
data_1 = "25"


def answer_1(my_var):
    pass


# Q2: Data er strengen "3.14". Cast den til float og returner.
data_2 = "3.14"


def answer_2(my_var):
    pass


# Q3: Data er strengen "7.9". Cast den til float FØRST, derefter til int.
#     Returner resultatet (int).
data_3 = "7.9"


def answer_3(my_var):
    pass


# Q4: Data er en int. Cast den til string og returner.
data_4 = 1337


def answer_4(my_var):
    pass


# Q5: Data er strengen "  42  " (med mellemrum).
#     Strip whitespace, cast til int, og returner.
data_5 = "  42  "


def answer_5(my_var):
    pass


# Q6: Returner TYPEN af data som en string.
#     Eksempel: hvis data er 42, returner "int". Hvis "hi", returner "str".
#     Hint: type(x).__name__ giver typenavnet som string.
data_6 = [1, 2, 3]


def answer_6(my_var):
    pass


# ============================================================
# SEKTION 2: IF / ELSE & BOOLEAN LOGIK
# ============================================================
# Sammenligning:
#   ==  !=  <  >  <=  >=
#
# Boolsk logik:
#   and   -> begge skal være True
#   or    -> mindst én skal være True
#   not   -> vender True/False
#
# if / elif / else:
#   if x > 10:
#       print("stor")
#   elif x > 5:
#       print("medium")
#   else:
#       print("lille")
#
# Ternary operator (kort if/else):
#   result = "ja" if x > 0 else "nej"
#
# Truthy/Falsy:
#   Falsy: 0, 0.0, "", [], {}, set(), None, False
#   Alt andet er Truthy
# ============================================================

# Q7: Data er en alder (int). Returner "barn" hvis under 13,
#     "teenager" hvis 13-17, "voksen" hvis 18+.
data_7 = 15


def answer_7(my_var):
    pass


# Q8: Data er et tal. Returner True hvis det er POSITIVT og LIGE, ellers False.
data_8 = 24


def answer_8(my_var):
    pass


# Q9: Data er en string. Returner True hvis den IKKE er tom, ellers False.
#     (Tænk truthy/falsy)
data_9 = "hello"


def answer_9(my_var):
    pass


# Q10: Data er et årstal. Returner True hvis det er et SKUDÅR.
#      Skudår: deleligt med 4, MEN IKKE med 100, MEDMINDRE også deleligt med 400.
#      Eksempler: 2000 -> True, 1900 -> False, 2024 -> True, 2023 -> False
data_10 = 2024


def answer_10(my_var):
    pass


# ============================================================
# SEKTION 3: STRING FORMATERING & MANIPULATION
# ============================================================
# f-strings:
#   f"Hej {name}"                -> indsæt variabel
#   f"{price:.2f}"               -> 2 decimaler: "3.14"
#   f"{num:05d}"                 -> nul-pad: "00042"
#   f"{'hi':>10}"                -> højrejusteret: "        hi"
#   f"{'hi':<10}"                -> venstrejusteret: "hi        "
#
# Andre formateringsmetoder:
#   "{}".format(value)           -> ældre metode
#   s.zfill(5)                   -> "42" -> "00042"
#   s.center(20, "-")            -> centreret med fill char
#
# String checks:
#   s.isdigit()    -> True hvis alle tegn er tal
#   s.isalpha()    -> True hvis alle tegn er bogstaver
#   s.isalnum()    -> True hvis alle tegn er bogstaver/tal
#   s.isupper()    -> True hvis alle bogstaver er STORE
#   s.islower()    -> True hvis alle bogstaver er små
# ============================================================

# Q11: Data er en tuple (name, age). Returner f-string: "Hej {name}, du er {age} år gammel"
data_11 = ("Alice", 30)


def answer_11(my_var):
    pass


# Q12: Data er en float. Returner den formateret med præcis 2 decimaler som string.
#      Eksempel: 3.1 -> "3.10"
data_12 = 3.1


def answer_12(my_var):
    pass


# Q13: Data er en string. Returner True hvis den KUN indeholder cifre.
data_13 = "123456"


def answer_13(my_var):
    pass


# Q14: Data er et tal (int). Returner det som string med nul-padding til 5 cifre.
#      Eksempel: 42 -> "00042"
data_14 = 42


def answer_14(my_var):
    pass


# Q15: Data er en string. Returner True hvis den starter med stort bogstav
#      OG resten er små bogstaver.
#      Eksempel: "Hello" -> True, "hello" -> False, "HELLO" -> False
data_15 = "Hello"


def answer_15(my_var):
    pass


# ============================================================
# SEKTION 4: LISTER — MERE ØVELSE
# ============================================================
# Ekstra list metoder:
#   lst.count(x)     -> antal forekomster af x
#   lst.extend(lst2) -> tilføj alle elementer fra lst2
#   lst.copy()       -> overfladisk kopi
#   min(lst)         -> mindste element
#   max(lst)         -> største element
#
# Unpacking:
#   first, *rest = [1, 2, 3, 4]   -> first=1, rest=[2,3,4]
#   first, *mid, last = [1,2,3,4] -> first=1, mid=[2,3], last=4
# ============================================================

# Q16: Data er en liste. Returner en tuple med (min, max, sum, len).
data_16 = [15, 42, 8, 23, 4, 67]


def answer_16(my_var):
    pass


# Q17: Data er en liste. Returner det FØRSTE og SIDSTE element som en tuple.
#      Brug unpacking!
data_17 = [10, 20, 30, 40, 50]


def answer_17(my_var):
    pass


# Q18: Data er en liste af strings. Returner en ny liste med LÆNGDEN af hver string.
#      Eksempel: ["hi", "bye"] -> [2, 3]
data_18 = ["python", "java", "c", "javascript", "go"]


def answer_18(my_var):
    pass


# Q19: Data er en liste af tal. Returner antallet af gange 3 forekommer.
data_19 = [3, 1, 4, 3, 5, 3, 2, 3]


def answer_19(my_var):
    pass


# Q20: Data er en liste med blandede typer. Returner en ny liste med KUN integers.
#      Eksempel: [1, "hi", 3.14, 2, True] -> [1, 2]
#      Hint: isinstance(x, int) og not isinstance(x, bool)
data_20 = [42, "hello", 3.14, 7, True, "world", 99, None, 0]


def answer_20(my_var):
    pass


# ============================================================
# SEKTION 5: DICTIONARIES — MERE ØVELSE
# ============================================================
# Nested dicts:
#   d = {"user": {"name": "Alice", "age": 30}}
#   d["user"]["name"]  -> "Alice"
#
# dict.get() med default:
#   d.get("missing", "default_value")  -> "default_value"
#
# Iteration:
#   for key in d:                -> kun keys
#   for key, value in d.items(): -> keys og values
# ============================================================

# Q21: Data er en dict. Returner værdien for nøglen "status".
#      Hvis "status" IKKE findes, returner "unknown".
#      Brug .get()!
data_21 = {"host": "10.0.0.1", "port": 8080}


def answer_21(my_var):
    pass


# Q22: Data er en nested dict. Returner værdien af "city" inde i "address".
data_22 = {
    "name": "Bob",
    "address": {"street": "Elm St", "city": "Copenhagen", "zip": "2100"},
}


def answer_22(my_var):
    pass


# Q23: Data er en dict med {navn: alder}. Returner en ny dict med KUN
#      de personer der er 18 eller ældre.
data_23 = {"Alice": 25, "Bob": 16, "Charlie": 30, "Diana": 14, "Eve": 19}


def answer_23(my_var):
    pass


# Q24: Data er en liste af strings. Returner en dict med {string: længde}.
#      Eksempel: ["hi", "bye"] -> {"hi": 2, "bye": 3}
data_24 = ["apple", "banana", "cherry"]


def answer_24(my_var):
    pass


# ============================================================
# SEKTION 6: LOOPS — MERE ØVELSE
# ============================================================
# zip(): iterer over to lister parallelt
#   for a, b in zip(list1, list2):
#       print(a, b)
#
# enumerate() med start:
#   for i, val in enumerate(lst, start=1):
#       print(i, val)   # starter fra 1
#
# while med break:
#   while True:
#       if condition:
#           break
# ============================================================

# Q25: Data er to lister i en tuple. Brug zip() til at lave en liste af tuples.
#      Eksempel: ([1,2], ["a","b"]) -> [(1,"a"), (2,"b")]
data_25 = ([10, 20, 30], ["x", "y", "z"])


def answer_25(my_var):
    pass


# Q26: Data er en liste af tal. Brug en while-loop til at finde det FØRSTE tal
#      der er større end 50. Returner det. Hvis intet tal > 50, returner -1.
data_26 = [12, 34, 8, 67, 45, 89]


def answer_26(my_var):
    pass


# Q27: Brug enumerate til at lave en dict med {indeks: element} for ALLE elementer.
#      Eksempel: ["a","b"] -> {0: "a", 1: "b"}
data_27 = ["alpha", "beta", "gamma", "delta"]


def answer_27(my_var):
    pass


# Q28: Data er et positivt tal. Brug en while-loop til at beregne summen
#      af alle cifre i tallet.
#      Eksempel: 1234 -> 1+2+3+4 = 10
#      Hint: tal % 10 giver sidste ciffer, tal // 10 fjerner det.
data_28 = 9876


def answer_28(my_var):
    pass


# ============================================================
# SEKTION 7: EXCEPTION HANDLING — MERE ØVELSE
# ============================================================
# Multiple except:
#   try:
#       ...
#   except ValueError:
#       ...
#   except KeyError:
#       ...
#   except (TypeError, IndexError):
#       ...
#
# Fange fejlbesked:
#   except ValueError as e:
#       print(f"Fejl: {e}")
# ============================================================

# Q29: Data er en liste af strings der skal konverteres til ints.
#      Returner en liste af tuples: (original_string, konverteret_int).
#      Hvis konvertering fejler, brug None i stedet for int.
#      Eksempel: ["5", "abc"] -> [("5", 5), ("abc", None)]
data_29 = ["10", "hello", "42", "3.14", "99"]


def answer_29(my_var):
    pass


# Q30: Data er en dict og en nøgle i en tuple: (dict, key).
#      Prøv at hente værdien. Hvis KeyError, returner "key not found".
data_30 = ({"a": 1, "b": 2}, "c")


def answer_30(my_var):
    pass


# ============================================================
# SEKTION 8: FUNKTIONER — MERE ØVELSE
# ============================================================
# *args og **kwargs:
#   def func(*args):       -> args er en tuple af alle positionelle args
#   def func(**kwargs):    -> kwargs er en dict af alle keyword args
#
# Default parametre:
#   def greet(name, greeting="Hello"):
#       return f"{greeting}, {name}!"
# ============================================================

# Q31: Returner True hvis ALLE tal i listen er positive (> 0).
data_31 = [5, 12, 3, 8, 1]


def answer_31(my_var):
    pass


# Q32: Returner Fibonacci-listen op til N elementer.
#      Fibonacci: hvert tal er summen af de to foregående.
#      Start med [0, 1]. Eksempel med N=7: [0, 1, 1, 2, 3, 5, 8]
data_32 = 10


def answer_32(my_var):
    pass


# Q33: Data er en string. Returner den med hvert ord capitalized (title case)
#      MEN brug IKKE .title() — gør det manuelt med split/join.
data_33 = "the quick brown fox"


def answer_33(my_var):
    pass


# ============================================================
# SEKTION 9: FILE I/O
# ============================================================

# Q34: Skriv tallene 1-10 (inklusiv) til /tmp/practice4_q34.txt, ét per linje.
#      Læs filen og returner SUMMEN af alle tallene.
data_34 = None


def answer_34(my_var):
    pass


# ============================================================
# SEKTION 10: IMPORT MODULER
# ============================================================

# Q35: Brug math modulet til at returnere PI afrundet til 4 decimaler (som float).
data_35 = None


def answer_35(my_var):
    pass


# Q36: Brug random modulet med seed 42 til at generere en liste af 5 tilfældige
#      tal mellem 1 og 100 (inklusiv). Returner listen.
#      Hint: random.seed(42) og random.randint(1, 100)
data_36 = None


def answer_36(my_var):
    pass


# ============================================================
# SEKTION 11: KOMBINATIONS-OPGAVER
# ============================================================

# ---- VIGTIG NOTE OM input() ----
# I virkeligheden ville du bruge input() til at læse fra terminalen:
#
#   name = input("Navn: ")             # -> "Alice"
#   age = int(input("Alder: "))        # -> 25 (cast til int!)
#   height = float(input("Højde: "))   # -> 1.82 (cast til float!)
#
# Eksempel: Læs navn og alder, gem i en dict:
#   name = input("Navn: ")
#   age = int(input("Alder: "))
#   person = {"name": name, "age": age}
#
# Eksempel: Læs navn og alder, gem i en tuple:
#   name = input("Navn: ")
#   age = int(input("Alder: "))
#   person = (name, age)
#
# Eksempel: Læs en hel linje og split den:
#   line = input("Skriv navn,alder,by: ")  # bruger skriver "Alice,25,Cph"
#   parts = line.split(",")
#   name = parts[0]
#   age = int(parts[1])
#   city = parts[2]
#
# Vi kan IKKE teste input() automatisk (det venter på tastatur),
# så i opgaverne herunder er data = det som input() ville returnere.
# Du skal parse/caste det præcis som du ville efter et input()-kald.
# ------------------------------------

# Q37: Forestil dig at brugeren har skrevet "Alice,25,Copenhagen" i terminalen.
#      (data = det input() returnerer)
#      Parse den og returner en dict: {"name": "Alice", "age": 25, "city": "Copenhagen"}
#      Bemærk: age skal være en INT, ikke en string!
data_37 = "Alice,25,Copenhagen"


def answer_37(my_var):
    pass


# Q38: Data er en liste af dicts med "name" og "grade" (string: "A", "B", "C", "D", "F").
#      Returner en dict med {grade: [liste af names]}, kun for grades der eksisterer.
#      Sortér navnene i hver grade-liste alfabetisk.
data_38 = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
    {"name": "Eve", "grade": "B"},
]


def answer_38(my_var):
    pass


# Q39: Data er en string. Tæl antal STORE bogstaver, små bogstaver, cifre og andre tegn.
#      Returner en dict: {"upper": X, "lower": X, "digits": X, "other": X}
data_39 = "Hello World! 123"


def answer_39(my_var):
    pass


# Q40: Data er en liste af tal. Returner en ny liste hvor hvert tal er
#      erstattet af "even" eller "odd".
#      Eksempel: [1, 2, 3] -> ["odd", "even", "odd"]
data_40 = [10, 15, 22, 33, 44, 51]


def answer_40(my_var):
    pass


# Q41: Data er en string med flere linjer.
#      Returner en liste med LINJE-NUMRE og linjer som tuples (startende fra 1).
#      Eksempel: "a\nb" -> [(1, "a"), (2, "b")]
data_41 = "first\nsecond\nthird\nfourth"


def answer_41(my_var):
    pass


# Q42: Data er en liste af tuples: (produkt, pris).
#      Returner en formateret string med hver linje som "produkt: XX.XX kr"
#      med prisen på 2 decimaler. Linjer adskilt af newline.
data_42 = [("Kaffe", 25.5), ("Te", 18.0), ("Juice", 32.75)]


def answer_42(my_var):
    pass


# Q43: Data er en string med tal adskilt af blandede separatorer (komma, semikolon, mellemrum).
#      Erstat alle separatorer med komma, split, cast til int, og returner summen.
#      Hint: brug .replace() flere gange
data_43 = "10,20;30 40,50;60"


def answer_43(my_var):
    pass


# Q44: Data er et password (string). Returner en dict med validerings-tjek:
#      {"length_ok": bool, "has_upper": bool, "has_lower": bool,
#       "has_digit": bool, "has_special": bool}
#      length_ok: mindst 8 tegn
#      has_special: indeholder mindst ét tegn der IKKE er bogstav eller ciffer
data_44 = "Passw0rd!"


def answer_44(my_var):
    pass


# Q45: Data er en liste af tal. Returner en dict med:
#      {"min": X, "max": X, "avg": X, "median": X}
#      avg skal være float med 2 decimaler.
#      median: sortér listen, tag midterste element (for ulige antal).
data_45 = [23, 1, 45, 12, 67]


def answer_45(my_var):
    pass


# Q46: Simuleret terminal-input: forestil dig en loop der kalder input() 3 gange.
#      Brugeren skriver "navn alder" hver gang. Data simulerer dette som én string
#      med newlines. Parse hver linje og returner en dict med {navn: alder_som_int}.
#      I virkeligheden ville koden se sådan ud:
#        people = {}
#        for _ in range(3):
#            line = input("Skriv navn og alder: ")
#            name, age = line.split()
#            people[name] = int(age)
data_46 = "Alice 25\nBob 30\nCharlie 22"


def answer_46(my_var):
    pass


# Q47: Data er en liste af tal. Returner en NY liste hvor negative tal er
#      erstattet af 0 (clamped). Positive tal og 0 forbliver uændrede.
#      Eksempel: [5, -3, 0, -1, 8] -> [5, 0, 0, 0, 8]
data_47 = [10, -5, 3, -8, 0, 15, -2]


def answer_47(my_var):
    pass


# Q48: Data er en liste af strings. Returner en ENKELT string hvor
#      elementerne er joined med " -> " (pil).
#      Eksempel: ["a", "b", "c"] -> "a -> b -> c"
data_48 = ["start", "middle", "end"]


def answer_48(my_var):
    pass


# Q49: Data er en tuple: (liste_af_tal, target_sum).
#      Returner True hvis NOGEN to tal i listen summerer til target_sum.
#      Eksempel: ([1, 3, 5, 7], 8) -> True (3+5=8)
data_49 = ([2, 7, 11, 15], 9)


def answer_49(my_var):
    pass


# Q50: Data er en string med Python-agtigt input: "name=Alice age=25 role=admin"
#      Parse den til en dict: {"name": "Alice", "age": "25", "role": "admin"}
data_50 = "name=Alice age=25 role=admin"


def answer_50(my_var):
    pass


# ============================================================
# ============================================================
#  TEST RUNNER - Rør ikke ved koden herunder!
#  Kør: python practice4.py
# ============================================================
# ============================================================

if __name__ == "__main__":
    import base64
    import copy
    import math
    import os
    import pickle
    import random

    # Build expected answers
    _A = {}
    _A[1] = 25
    _A[2] = 3.14
    _A[3] = 7
    _A[4] = "1337"
    _A[5] = 42
    _A[6] = "list"
    _A[7] = "teenager"
    _A[8] = True
    _A[9] = True
    _A[10] = True
    _A[11] = "Hej Alice, du er 30 år gammel"
    _A[12] = "3.10"
    _A[13] = True
    _A[14] = "00042"
    _A[15] = True
    _A[16] = (4, 67, 159, 6)
    _A[17] = (10, 50)
    _A[18] = [6, 4, 1, 10, 2]
    _A[19] = 4
    _A[20] = [42, 7, 0]
    _A[21] = "unknown"
    _A[22] = "Copenhagen"
    _A[23] = {"Alice": 25, "Charlie": 30, "Eve": 19}
    _A[24] = {"apple": 5, "banana": 6, "cherry": 6}
    _A[25] = [(10, "x"), (20, "y"), (30, "z")]
    _A[26] = 67
    _A[27] = {0: "alpha", 1: "beta", 2: "gamma", 3: "delta"}
    _A[28] = 30
    _A[29] = [("10", 10), ("hello", None), ("42", 42), ("3.14", None), ("99", 99)]
    _A[30] = "key not found"
    _A[31] = True
    _A[32] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    _A[33] = "The Quick Brown Fox"
    # Q34: write 1-10, read back, return sum
    _A[34] = 55
    # Q35: pi rounded to 4 decimals
    _A[35] = round(math.pi, 4)
    # Q36: random with seed 42
    random.seed(42)
    _A[36] = [random.randint(1, 100) for _ in range(5)]
    _A[37] = {"name": "Alice", "age": 25, "city": "Copenhagen"}
    _A[38] = {"A": ["Alice", "Charlie"], "B": ["Bob", "Eve"], "C": ["Diana"]}
    _A[39] = {"upper": 2, "lower": 8, "digits": 3, "other": 3}
    _A[40] = ["even", "odd", "even", "odd", "even", "odd"]
    _A[41] = [(1, "first"), (2, "second"), (3, "third"), (4, "fourth")]
    _A[42] = "Kaffe: 25.50 kr\nTe: 18.00 kr\nJuice: 32.75 kr"
    _A[43] = 210
    _A[44] = {
        "length_ok": True,
        "has_upper": True,
        "has_lower": True,
        "has_digit": True,
        "has_special": True,
    }
    _A[45] = {"min": 1, "max": 67, "avg": 29.6, "median": 23}
    _A[46] = {"Alice": 25, "Bob": 30, "Charlie": 22}
    _A[47] = [10, 0, 3, 0, 0, 15, 0]
    _A[48] = "start -> middle -> end"
    _A[49] = True
    _A[50] = {"name": "Alice", "age": "25", "role": "admin"}

    _tests = [
        (1, answer_1, data_1, "Basics: cast string til int"),
        (2, answer_2, data_2, "Basics: cast string til float"),
        (3, answer_3, data_3, "Basics: string -> float -> int"),
        (4, answer_4, data_4, "Basics: int til string"),
        (5, answer_5, data_5, "Basics: strip + cast"),
        (6, answer_6, data_6, "Basics: type som string"),
        (7, answer_7, data_7, "If/else: alders-kategorier"),
        (8, answer_8, data_8, "If/else: positiv og lige"),
        (9, answer_9, data_9, "If/else: truthy/falsy"),
        (10, answer_10, data_10, "If/else: skudår"),
        (11, answer_11, data_11, "Strings: f-string formatering"),
        (12, answer_12, data_12, "Strings: 2 decimaler"),
        (13, answer_13, data_13, "Strings: isdigit"),
        (14, answer_14, data_14, "Strings: zero-padding"),
        (15, answer_15, data_15, "Strings: capitalize check"),
        (16, answer_16, data_16, "Lists: min/max/sum/len"),
        (17, answer_17, data_17, "Lists: first og last"),
        (18, answer_18, data_18, "Lists: længde af strings"),
        (19, answer_19, data_19, "Lists: count"),
        (20, answer_20, data_20, "Lists: filtrer kun ints"),
        (21, answer_21, data_21, "Dicts: .get() med default"),
        (22, answer_22, data_22, "Dicts: nested dict"),
        (23, answer_23, data_23, "Dicts: filtrer dict"),
        (24, answer_24, data_24, "Dicts: string til længde"),
        (25, answer_25, data_25, "Loops: zip()"),
        (26, answer_26, data_26, "Loops: while + break"),
        (27, answer_27, data_27, "Loops: enumerate til dict"),
        (28, answer_28, data_28, "Loops: ciffer-sum med while"),
        (29, answer_29, data_29, "Exception: konverter med None"),
        (30, answer_30, data_30, "Exception: KeyError"),
        (31, answer_31, data_31, "Functions: alle positive"),
        (32, answer_32, data_32, "Functions: fibonacci"),
        (33, answer_33, data_33, "Functions: manual title case"),
        (34, answer_34, data_34, "File I/O: skriv og sum"),
        (35, answer_35, data_35, "Import: math.pi"),
        (36, answer_36, data_36, "Import: random med seed"),
        (37, answer_37, data_37, "Combo: parse CSV-input"),
        (38, answer_38, data_38, "Combo: grouper grades"),
        (39, answer_39, data_39, "Combo: char type tæller"),
        (40, answer_40, data_40, "Combo: even/odd labels"),
        (41, answer_41, data_41, "Combo: linjenumre"),
        (42, answer_42, data_42, "Combo: formateret prisliste"),
        (43, answer_43, data_43, "Combo: blandede separatorer"),
        (44, answer_44, data_44, "Combo: password validering"),
        (45, answer_45, data_45, "Combo: statistik dict"),
        (46, answer_46, data_46, "Combo: parse multiline input"),
        (47, answer_47, data_47, "Combo: clamp negative"),
        (48, answer_48, data_48, "Combo: join med pil"),
        (49, answer_49, data_49, "Combo: two sum"),
        (50, answer_50, data_50, "Combo: parse key=value"),
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

    # Cleanup
    tmp = "/tmp/practice4_q34.txt"
    if os.path.exists(tmp):
        os.remove(tmp)

    print("=" * 60)
    print(
        f"  {passed} PASS / {failed} FAIL / {skipped} SKIP  (af {len(_tests)} opgaver)"
    )
    print("=" * 60)
    print()
