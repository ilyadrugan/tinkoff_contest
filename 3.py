from copy import copy
str = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
slovo = list('ОБЛАКО')
# for letter in str:
#     alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     slovo[2]=letter
#     alph = alph.split(slovo[0])
#     alph[0], alph[1] = list(alph[0]), list(alph[1])
#     alph[0].append(slovo[0])
#     tmp = copy(alph[1])
#     alph[1] = copy(alph[0])
#     alph[0] = copy(tmp)
#     # print(alph[0], alph[1])
#     znaki = list('.,?')
#     alph[0].extend(alph[1])
#     alph[0].extend(znaki)
#     alphabet = alph[0]
#     print(alphabet)
#     # alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,?')
#     slovar = {}
#     for i, a in enumerate(alphabet):
#         slovar[a] = i
#     # print(slovar)
#     invertSlovar = {}
#     for k, v in slovar.items():
#         invertSlovar[v] = k
#     print(invertSlovar)
#     newSlovar = {}
#     for k, v in invertSlovar.items():
#         chast = k // 6
#         ost = k % 6
#
#         newSlovar[6*ost+chast] = v
#
#     newWord = ''
#     for l in slovo:
#         chast = slovar[l]//6
#         ost = slovar[l]%6
#         newWord+=invertSlovar[6*ost+chast]
#         print("исходный индекс",slovar[l], "частное",chast, "остаток",ost, "новый индекс",6*ost+chast, "новая буква",invertSlovar[6*ost+chast])
#
#     print(newWord)
#     if (newWord[1]==','):
#         print('ТРЕТЬЯ БУКВА ИСХОДНОГО СЛОВА:', letter)
#         break

#дешифратор
alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# slovo[2]=letter
alph = alph.split(slovo[0])
alph[0], alph[1] = list(alph[0]), list(alph[1])
alph[0].append(slovo[0])
tmp = copy(alph[1])
alph[1] = copy(alph[0])
alph[0] = copy(tmp)
# print(alph[0], alph[1])
znaki = list('.,?')
alph[0].extend(alph[1])
alph[0].extend(znaki)
alphabet = alph[0]
print(alphabet)
# alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,?')
slovar = {}
for i, a in enumerate(alphabet):
    slovar[a] = i
print(slovar)
invertSlovar = {}
for k, v in slovar.items():
    invertSlovar[v] = k
# print(invertSlovar)

newSlovar = {}
for k, v in invertSlovar.items():
    chast = k // 6
    ost = k % 6
    newSlovar[6*ost+chast] = v
invertNEWSlovar = {}
for k, v in newSlovar.items():
    invertNEWSlovar[v] = k
print(newSlovar)
print(invertNEWSlovar)

newWord = ''
for l in slovo:
    chast = slovar[l]//6
    ost = slovar[l]%6
    newWord+=invertSlovar[6*ost+chast]
    print("исходная буква",l,"исходный индекс",slovar[l], "частное",chast, "остаток",ost, "новый индекс",6*ost+chast, "новая буква",invertSlovar[6*ost+chast])

print(newWord)


oldWord = []
word = list('АТ,ОКА')

for l in word:

    oldWord.append(invertSlovar[invertNEWSlovar[l]])
print(oldWord)
