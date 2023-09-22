special_letters = 'åøæ'
num_spec_letters = len(special_letters)

def prettyPrint(text):
    splittedText = text.split("\n")
    for line in splittedText:
        print(line)


def getNewLetterUpper(letter, s):
    if letter.lower() in special_letters:
        return letter.upper()
    return chr((ord(letter) + s - 65) % 26 + 65)


def getNewLetterLower(letter, s):
    if letter in special_letters:
        return letter
    return chr((ord(letter) + s - 97) % 26 + 97)


def getComplementLetter(letter):
    return chr((26 - (ord(letter) - 97)) % 26 + 97)

"""
text - text to be encrypted.
word - is used for encryption. Must consist of small letters without
        any special characters.
"""
def encrypt(text, word):
    output = "";
    s = [ord(w) - 97 for w in word]
    k = len(word)
    i = 0
    while i < len(text):
        letter = text[i]
        if not letter.isalpha():
            output += letter
            i += 1
            continue
        if letter.isupper():
            newLetter = getNewLetterUpper(letter, s[i%k])
            output += newLetter
        else:
            newLetter = getNewLetterLower(letter, s[i%k])
            output += newLetter
        i += 1
    return output


def decrypt(text, word):
    newWord = ""
    for w in word:
        newWord += getComplementLetter(w)
    return encrypt(text, newWord)
