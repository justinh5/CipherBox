

def convert_numbers(value, x, y):
    """Convert integer representations
    Convert a value from representation x to representation y, where
    value is any integer representation and x and y can range from base 2-36.
    """

    # attempt to convert the value to a decimal integer
    temp = int(value, x)
    return str(base10toN(temp, y))


def convert_binary(value, x, y):
    """Convert binary representations
    Convert values between different types of binary representations.
    Value comes in as x and is returned as y.
    """

    if x == "Unsigned":
        temp = int(value, 2)
    elif x == "Sign and Magnitude":
        temp = sign_and_mag_to_int(value)
    elif x == "One's Complement":
        temp = ones_to_int(int(value, 2), len(value))
    elif x == "Two's Complement":
        temp = twos_to_int(int(value, 2), len(value))
    else:              # the value is already in decimal
        temp = int(value)

    if y == "Unsigned":
        return "{0:b}".format(temp)
    elif y == "Sign and Magnitude":
        return int_to_sign_and_mag(temp)
    elif y == "One's Complement":
        return int_to_ones(temp)
    elif y == "Two's Complement":
        return int_to_twos(temp)
    else:              # the value is already in decimal
        return temp


def convert_dunits(value, x, y):
    """Convert digital storage units
    Convert a digital storage value from units x to units y. Value can be any
    decimal value and x and y are strings that represent the units.
    """

    prefix = {'bit': 1, 'byt': 1, 'kil': 1000, 'kib': 1024, 'meg': 10**6, 'meb': 2**20, 'gig': 10**9,
              'gib': 2**30, 'ter': 10**12, 'teb': 2**40, 'pet': 10**15, 'peb': 2**50}

    xprefix, xsuffix = x[:3], x[-1]
    yprefix, ysuffix = y[:3], y[-1]

    if xsuffix == 'e' and ysuffix == 'e':          # bytes -> bytes
        xbytes = prefix[xprefix] * value
        return xbytes / prefix[yprefix]
    elif xsuffix == 'e' and ysuffix == 't':        # bytes -> bits
        xbits = (prefix[xprefix] * value) * 8
        return xbits / prefix[yprefix]
    elif xsuffix == 't' and ysuffix == 'e':        # bits -> bytes
        xbytes = (prefix[xprefix] * value) / 8
        return xbytes / prefix[yprefix]
    else:                                          # bits -> bits
        xbits = prefix[xprefix] * value
        return xbits / prefix[yprefix]


def base10toN(num, base):
    """Convert a decimal number (base-10) to a number of any base/radix from 2-36."""

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    if num == 0:
        return '0'

    if num < 0:
        return '-' + base10toN((-1) * num, base)

    left = num // base
    if left == 0:
        return digits[num % base]
    else:
        return base10toN(left, base) + digits[num % base]


def sign_and_mag_to_int(value):
    if value[0] == "1":
        return int(value[1:], 2) * -1
    return int(value, 2)


def ones_to_int(value, bits):
    if value >> (bits - 1) != 0:    # if sign bit is negative
        value -= (1 << bits) - 1    # invert bits
    return value


def twos_to_int(value, bits):
    if value >> (bits - 1) != 0:    # if sign bit is negative
        value -= 1 << bits
    return value


def int_to_sign_and_mag(value):
    if value < 0:
        return "1" + "{0:b}".format(abs(value))
    else:
        temp = "{0:b}".format(value)
        if temp[0] != "0":
            temp = "0" + temp
        return temp


def int_to_ones(value):
    if value < 0:  # flip bits if negative
        return "{0:b}".format(abs(abs(value) - ((1 << value.bit_length() + 1) - 1)))
    else:
        temp = "{0:b}".format(value)
        if temp[0] != "0":
            temp = "0" + temp
        return temp


def int_to_twos(value):
    if value < 0:
        return "{0:b}".format(abs(abs(value) - (1 << value.bit_length() + 1)))
    else:
        temp = "{0:b}".format(value)
        if temp[0] != "0":
            temp = "0" + temp
        return temp
