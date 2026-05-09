import re
dict = {
    'pee': '+',
    'gah': '-',
    'milk': '*',
    'heh': '/',
    'mama': '(',
    'dada': ')',
    'b': '0',  
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

def decipher(babyExp):
    i = 0
    result = []

    while i < len(babyExp):
        if babyExp[i].isspace():
            i += 1
            continue
        
        matched = False
        for tok in tokens:
            if babyExp.startswith(tok, i):
                result.append(dict[tok])
                i += len(tok)
                matched = True
                break
        if not matched:
            return ("no match")
    result = [i for i in result if i != ' ']
    return "".join(result)
