#!/usr/bin/env python3
# Ying Lu
# Comp340 - Decipher HW
import re
dict = {
    'pee': '+',
    'gah': '-',
    'milk': '*',
    'heh': '/',
    'mama': '(',
    'dada': ')',
    ' ': ' ',
    'b': '0',  # number of a's = num value
    'ba': '1',
    'baa': '2',
    'baaa': '3',
    'baaaa': '4',
    'baaaaa': '5',
    'baaaaaa': '6',
    'baaaaaaa': '7',
    'baaaaaaaa': '8',
    'baaaaaaaaa': '9'
}

tokens = sorted(dict.keys(), key=len, reverse=True)
print("decipher tokens: ", tokens)


def decipher(babyExp):
    i = 0
    result = []

    while i < len(babyExp):
        matched = False
        for tok in tokens:
            if babyExp.startswith(tok, i):
                result.append(dict[tok])
                i += len(tok)
                matched = True
                break
        if not matched:
            return ("no match found")
    return "".join(result)
