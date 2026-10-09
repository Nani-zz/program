# Задание шифр Цезаря
def tozezhar(sent: str, shag: int):
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    leng = ''
    if sent[0] in ABC:
        leng = 'английский'
    elif sent[0] in RUS:
        leng = 'русский'
    print(leng)
    korkas = ''
    if leng == 'английский':
        korkas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif leng == 'русский':
        korkas = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    newsent = ''
    for i in range(len(sent)):
        if (korkas.find(sent[i]) + (shag)) <= (len(korkas) - 1):
            newsent += korkas[korkas.find(sent[i]) + (shag)]
        elif (korkas.find(sent[i]) + (shag)) > (len(korkas) - 1):
            newsent += korkas[(korkas.find(sent[i]) + (shag)) - (len(korkas))]
    return newsent
def outzezhar(sent: str, shag: int):
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    leng = ''
    if sent[0] in ABC:
        leng = 'английский'
    elif sent[0] in RUS:
        leng = 'русский'
    print(leng)
    korkas = ''
    if leng == 'английский':
        korkas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif leng == 'русский':
        korkas = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    newsent = ''
    for i in range(len(sent)):
        if (korkas.find(sent[i]) - (shag)) >= 0:
            newsent += korkas[korkas.find(sent[i]) - (shag)]
        elif (korkas.find(sent[i]) - (shag)) < 0:
            newsent += korkas[(korkas.find(sent[i]) - (shag)) + (len(korkas))]
    return newsent

print('Расшифровать / Зашифровать')
shto = input()
sent = input()
shag = int(input())
if shto == 'Расшифровать':
    print(outzezhar(sent, shag))
else:
    print(tozezhar(sent, shag))
