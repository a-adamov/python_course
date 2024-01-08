# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#
# В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# alphabet = {
#     "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1,
#     "D": 2, "G": 2,
#     "B": 3, "C": 3, "M": 3, "P": 3,
#     "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
#     "K": 5,
#     "J": 8, "X": 8,
#     "Q": 10, "Z": 10,
#     "А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1,
#     "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2,
#     "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3,
#     "Й": 4, "Ы": 4,
#     "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5,
#     "Ш": 8, "Э": 8, "Ю": 8,
#     "Ф": 10, "Щ": 10, "Ъ": 10
# }
#
# word = (input("Введите слово: ")).upper()
# points = 0
# for letter in word:
#     points += alphabet[letter]
#
# print(f"Количество очков: {points}")

rus = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ШЭЮ',
    10: 'ФЩЪ'
}

eng = {
    1: 'AEIOULNSTR',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}

rus_alphabet = ''
for letters in [v for k,v in rus.items()]:
    rus_alphabet += letters

eng_alphabet = ''
for letters in [v for k,v in eng.items()]:
    eng_alphabet += letters


word = (input("Введите слово: ")).upper()
points = 0

for letter in word:
    if letter in rus_alphabet:
        for i in rus:
            if letter in rus[i]:
                points += i
    else:
        for i in eng:
            if letter in eng[i]:
                points += i

print(f"Количество очков: {points}")
print(rus_alphabet)