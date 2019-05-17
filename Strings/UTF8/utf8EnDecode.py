'''
UTF-8 Encoding

1 byte:  0xxxxxxx
2 bytes: 110xxxxx 10xxxxxx
3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

example:
€ -> code point:         U+20AC
  -> binary:             0010 0000 1010 1100
  -> binary utf-8:       11100010 10000010 10101100
  -> hexadecimal utf-8:  \xE2\x82\xAC
'''


def encode(string):

    result = ""

    for x in string:

        value = ord(x)

        if value.bit_length() < 8:                                          # 1 byte (ASCII character)
            result += '\\x' + str(hex(value)[2:]).zfill(2)
        elif 7 < value.bit_length() < 12:                                   # 2 bytes
            result += '\\x' + str(hex(192 + ((value >> 6) & 31))[2:]) + \
                      '\\x' + str(hex(128 + (value & 63))[-2:])
        elif 11 < value.bit_length() < 17:                                  # 3 bytes
            result += '\\x' + str(hex(224 + ((value >> 12) & 15))[2:]) + \
                      '\\x' + str(hex(128 + ((value >> 6) & 63))[2:]) + \
                      '\\x' + str(hex(128 + (value & 63))[-2:])
        else:                                                               # 4 bytes
            result += '\\x' + str(hex(240 + ((value >> 18) & 7))[2:]) + \
                      '\\x' + str(hex(128 + ((value >> 12) & 63))[2:]) + \
                      '\\x' + str(hex(128 + ((value >> 6) & 63))[-2:]) + \
                      '\\x' + str(hex(128 + (value & 63))[-2:])

    return result


# This function decodes a utf-8 hex encoding to a utf-8 decoded string.
# Unfortunately, there is a limit to how many characters Python can display,
# and therefore the maximum amount of utf-8 characters it can detect is 1,114,111.
def decode(string):

    string = string.replace('\\x', '')   # remove all '\x'

    result = ""

    i = 0

    while i < len(string):
        if string[i].isdecimal():                     # character is 1 byte
            newi = i + 2
            temp = string[i:newi]
        elif string[i].lower() in ['c', 'd']:         # character is 2 bytes
            newi = i + 4
            temp = string[i:newi]
        elif string[i].lower() == 'e':                # character is 3 bytes
            newi = i + 6
            temp = string[i:newi]
        elif string[i].lower() == 'f':                # character is 4 bytes
            newi = i + 8
            temp = string[i:newi]
        else:                                         # encoding is not utf-8
            return

        result += chr(int(temp, 16))  # change hex value to string char
        i = newi

    return result

