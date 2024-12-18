"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Katerina Markova
email: cathy.markova@gmail.com
discord: kate_marko1_54460
"""

print("$ python projekt1.py")
user_list = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
oddelovac = 40 * "-"
uzivatel = input("User name: ")
heslo = input("Password: ")
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

if (uzivatel.lower() in user_list.keys()
        and heslo.lower() == user_list.get(uzivatel)):
    print(oddelovac)
    print(f"Welcome to the app, {uzivatel}.\n"
          f"We have 3 texts to be analysed.")

else:
    print("unregistered user, terminating the program..")
    exit()
#text_1 = TEXTS[0]
#text_2 = TEXTS[1]
#text_3 = TEXTS[2]

while True:
    try:
        text_volba = int(input("Enter a number btw. 1 and 3 to select: "))
        if text_volba not in range(1, 4):
            print("Wrong number. Try again.")
        else:
            break
    except ValueError:
        print("Wrong entry, not a number.")

upraveny_text = (TEXTS[text_volba-1]
                 .replace(",", "")
                 .replace(".", "")
                 .strip().split())
pocet_slov = len(upraveny_text)
print(f"There are {pocet_slov} words in selected text.")
slova_zac_vel_pis = 0
slova_s_mal_pis = 0
pocet_cisel = 0
slova_jen_velka = 0
suma_cisel = 0
for word in upraveny_text:
    if word.istitle():
        slova_zac_vel_pis += 1
    elif word.islower():
        slova_s_mal_pis += 1
    elif word.isdigit():
        pocet_cisel += 1
        suma_cisel += int(word)
    elif word.isupper() and word.isalpha():
        slova_jen_velka += 1
to_be = ""
to_be1 = ""
num_words = ""
#úprava slovesa a koncovek podle počtu ve výsledném printu
if int(slova_jen_velka) == 1:
    to_be = "is"
    num_words = "word"
else:
    to_be = "are"
    num_words = "words"
if int(pocet_cisel) == 1:
    to_be1 = "is"
    num_strings = "string"
else:
    to_be1 = "are"
    num_strings = "strings"
print(f"There are {slova_zac_vel_pis} titlecase words.")
print(f"There are {slova_s_mal_pis} lowercase words. ")
print(f"There {to_be} {slova_jen_velka} uppercase {num_words}.")
print(f"There {to_be1} {pocet_cisel} numeric {num_strings}.")
print(f"The sum of all the numbers {suma_cisel}")
print(oddelovac)
seznam_delka_slov = [len(word)for word in upraveny_text]
max_delka_slova = max(seznam_delka_slov)
nejvyssi_pocet_znaku = [len([word for word in upraveny_text if len(word) == i])
                        for i in range(1, max_delka_slova + 1)]

def vypocitej_vyskyt_dat(text):
    vyskyt = dict()
    cislo = 0
    for cislo in text:
        vyskyt[cislo] = vyskyt.setdefault(cislo, 0) + 1
    return vyskyt

slovnik_vyskytu = vypocitej_vyskyt_dat(seznam_delka_slov)
nejvyssi_vyskyt = max(slovnik_vyskytu.values())
sirka_sloupce_occurences = nejvyssi_vyskyt
print(f"{'LEN'.rjust(4)}|"
      f"{'OCCURENCES'.center(sirka_sloupce_occurences + 1, ' ')}|"
      f"{'NR.'.ljust(3)}")
for i in (range(1, max_delka_slova + 1)):
    vyskyt = slovnik_vyskytu.get(i, 0)
    print(f"{str(i).rjust(4, ' ')}|"
          f"{('*' * vyskyt).ljust(sirka_sloupce_occurences + 1)}|"
          f"{(str(vyskyt)).ljust(3)}")