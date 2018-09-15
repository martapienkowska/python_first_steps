klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
deklucz = {v: k for k, v in klucz.items()}


def szyfrator():
    text = input("Wpisz tekst do szyfratora: ")
    text_2 = ""
    for i in text:
        if i in klucz:
            text_2 += klucz[i]
        else:
            text_2 += i
    print(text_2)


szyfrator()


def deszyfrator():
    text = input("Wpisz tekst do deszyfratora: ")
    text_3 = ""
    for i in text:
        if i in deklucz:
            text_3 += deklucz[i]
        else:
            text_3 += i
    print(text_3)


deszyfrator()
