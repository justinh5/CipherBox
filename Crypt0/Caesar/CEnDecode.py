

def encode(plaintext, shift):
    """Encode plaintext
    Encode the message with a given shift key. Offset each character
    in the message by 'shift' number of letters in the alphabet
    """

    ciphertext = ""

    # shift each character
    for x in plaintext:
        if 97 <= ord(x) <= 122:       # if character is alphabetic lowercase
            ciphertext += chr((ord(x) - 97 + shift) % 26 + 97)
        elif 65 <= ord(x) <= 90:      # if character is alphabetic uppercase
            ciphertext += chr((ord(x) - 65 + shift) % 26 + 65)
        else:                         # non-alphabetic characters do not change
            ciphertext += x
    return ciphertext


def decode(ciphertext, shift, known):
    """Decode ciphertext
    Decode the message in either of the cases where
    the shift key is or is not known. A shift key that isn't known
    will call the decode_all function to test all possible shifts.
    """

    if not known:
        return decode_all(ciphertext)  # decode with all possibilities if shift key is unknown

    plaintext = ""

    for x in ciphertext:
        if 97 <= ord(x) <= 122:    # character is alphabetic lowercase
            plaintext += chr((ord(x) - 97 - shift) % 26 + 97)
        elif 65 <= ord(x) <= 90:   # character is alphabetic uppercase
            plaintext += chr((ord(x) - 65 - shift) % 26 + 65)
        else:                      # non-alphabetic characters do not change
            plaintext += x

    return plaintext


def decode_all(ciphertext):
    """Decode ciphertext when shift key is unknown
    All possible 25 shifts are attempted, each with a
    different offset in the alphabet.
    """

    plaintext = ""

    for i in range(1, 26):

        temp = ""

        for x in ciphertext:
            if 97 <= ord(x) <= 122:    # character is alphabetic lowercase
                temp += chr((ord(x) - 97 - i) % 26 + 97)
            elif 65 <= ord(x) <= 90:   # character is alphabetic uppercase
                temp += chr((ord(x) - 65 - i) % 26 + 65)
            else:                      # non-alphabetic characters do not change
                temp += x

        plaintext += "Shift " + str(i) + ": " + "\n" + temp + "\n\n"

    return plaintext
