"""
author: Tereza Kotmelova

"""

texts = ['''
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

oddelovac = '=' * 30
uzivatele = {
  'bob': '123',
  'ann': 'pass123',
  'mike': 'password123',
  'liz': 'pass123',
}

username = input('Uživatelské jméno: ')
password = input('Heslo: ')

if uzivatele.get(username) == password:
    print(oddelovac)

else:
    print('Špatné uživatelské jméno nebo heslo.')
    exit()
    print(oddelovac)

vyber = int(input('Níže provedeme analýzu jednoho ze tří textů:'))
print(oddelovac)
vybrany_text = str(texts[vyber - 1])

if vyber in range(1, 4):
    print(vybrany_text)
    print(oddelovac)
else:
    print("Špatná volba. Vyber číslo mezi 1-3")
    exit()

text = []
for slovo in vybrany_text.split():
    slovo = slovo.strip('.,')
    text.append(slovo)
print(oddelovac)

pocet_slov = str(len(text))

titlecase = 0
uppercase = 0
lowercase = 0
numbers = 0
pocet = {}
suma = 0
i = 0

while i < len(text):

    if text[i].istitle():
        titlecase += 1
    elif text[i].isupper():
        uppercase += 1
    elif text[i].islower():
        lowercase += 1
    elif text[i].isnumeric():
        numbers += 1
        suma = suma + float(text[i])

    ln = len(text[i])
    pocet[ln] = pocet.get(1, 0) + 1

    i += 1

print(f"V textu je:", pocet_slov, "slov")
print(f"V textu je:", titlecase, " slov zacinajicich velkym pismenem")
print(f"V textu je:", uppercase, "slov psanych velkym ppismem")
print(f"V textu je::", lowercase, "slov psanych malym pismem")
print(f"V textu je:", numbers, "cisel")
print(oddelovac)

length = []
for slovo in text:
    length.append(len(slovo))
length.sort()

for stars in set(length):
    print(stars, "*" * length.count(stars), length.count(stars))

print(oddelovac)

print("Součet všech čísel v textu je:" + str(suma))
print(oddelovac)
