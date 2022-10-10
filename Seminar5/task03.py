def encode(text):
    count = 1
    result = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def decode(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


text = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {encode(text)}")
print(f"Текст после дешифровки: {decode(encode(text))}")