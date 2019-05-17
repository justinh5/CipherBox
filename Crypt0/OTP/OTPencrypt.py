# One-time pad encryption/decryption


def encrypt(plaintext, key):

    ciphertext = ""
    i, j = 0, 0      # key, plaintext indices

    # strip all non-alpha characters from key
    key2 = ""
    for x in key: key2 += x if x.isalpha() else ""

    # shift each character
    for x in plaintext:
        if 97 <= ord(x) <= 122:             # if character is alphabetic lowercase
            ciphertext += chr(((ord(x) - 97) + (ord(key2[i].lower()) - 97)) % 26 + 97)
            i += 1
        elif 65 <= ord(x) <= 90:            # if character is alphabetic uppercase
            ciphertext += chr(((ord(x) - 65) + (ord(key2[i].upper()) - 65)) % 26 + 65)
            i += 1
        else:                               # non-alphabetic characters do not change
            ciphertext += x
        j += 1

        if i == len(key2):
            return ciphertext + plaintext[j:]

    return ciphertext


def decrypt(ciphertext, key):

    plaintext = ""
    i, j = 0, 0       # key, ciphertext indices

    # strip all non-alpha characters from key
    key2 = ""
    for x in key: key2 += x if x.isalpha() else ""

    # shift each character
    for x in ciphertext:
        if 97 <= ord(x) <= 122:  # if character is alphabetic lowercase
            plaintext += chr(((ord(x) - 97) - (ord(key2[i].lower()) - 97)) % 26 + 97)
            i += 1
        elif 65 <= ord(x) <= 90:  # if character is alphabetic uppercase
            plaintext += chr(((ord(x) - 65) - (ord(key2[i].upper()) - 65)) % 26 + 65)
            i += 1
        else:  # non-alphabetic characters do not change
            plaintext += x
        j += 1

        if i == len(key2):
            return plaintext + ciphertext[j:]

    return plaintext
