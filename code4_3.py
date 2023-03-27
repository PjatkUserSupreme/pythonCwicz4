def caesar_cipher(wiadomosc, klucz, alfabet=''):
    wiadomosc = wiadomosc.lower()
    if not alfabet:
        alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z']

    odpowiedz = ""

    for znak in wiadomosc:
        if znak in alfabet:
            pos = alfabet.index(znak)
            odpowiedz += alfabet[(pos + klucz) % len(alfabet)]
        else:
            odpowiedz += znak

    return odpowiedz

data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"

enc = caesar_cipher(data, 3,["a","B"])
print(enc)