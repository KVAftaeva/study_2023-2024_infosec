alphabeth = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
             'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',
             'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
             'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
             'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '.', ',', '!', '?', ' ']

def decrypt(text1, text2, gamma):
    text1Len = len(text1)
    text2Len = len(text2)
    gammaLen = len(gamma)

    keyText = []
    for i in range(text1Len // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(text1Len % gammaLen):
        keyText.append(gamma[i])

    code1 = []
    code2 = []

    for i in range(text1Len):
        code1.append(alphabeth[(alphabeth.index(text1[i]) + alphabeth.index(keyText[i])) % 71])

    for i in range(text2Len):
        code2.append(alphabeth[(alphabeth.index(text2[i]) + alphabeth.index(keyText[i])) % 71])

    return(print(*code1,sep=''),print(*code2,sep=''))

def decrypt2(code1, code2, text1):
    code1Len = len(code1)
    code2Len = len(code2)
    text1Len = len(text1)

    text2 = []

    for i in range(code1Len):
        text2.append(alphabeth[(alphabeth.index(code1[i]) - (alphabeth.index(code2[i]) - alphabeth.index(text1[i]))) % 71])

    return(print(*text2,sep=''))

decrypt('С Новым Годом, друзья!', 'С Левым Годом, друзья!', 'ААъАЙААААААААААААААААА')
print()
decrypt2('С Голым Годом, друзья!', 'С Белым Годом, друзья!', 'С Левым Годом, друзья!' )



