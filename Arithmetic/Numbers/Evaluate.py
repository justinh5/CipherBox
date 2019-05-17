from Convert.Numbers.Convert import *
import operator


OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/ (will round)": operator.floordiv}

def evaluate(op1, op2, op, kind):
    """Evaluates an expression
    First convert both operands to decimal integers, then perform
    the selected operation and return the expected value.
    """

    if kind == "Unsigned Binary":
        temp = OPS[op](int(op1, 2), int(op2, 2))
        result = "{0:b}".format(temp)          # format result to binary string

    elif kind == "Sign and Magnitude":
        left = sign_and_mag_to_int(op1)
        right = sign_and_mag_to_int(op2)
        temp = OPS[op](left, right)
        result = int_to_sign_and_mag(temp)

    elif kind == "One's Complement":
        left = ones_to_int(int(op1, 2), len(op1))
        right = ones_to_int(int(op2, 2), len(op2))
        temp = OPS[op](left, right)
        result = int_to_ones(temp)

    elif kind == "Two's Complement":
        left = twos_to_int(int(op1, 2), len(op1))
        right = twos_to_int(int(op2, 2), len(op2))
        temp = OPS[op](left, right)
        result = int_to_twos(temp)

    else:
        temp = OPS[op](int(op1, 16), int(op2, 16))
        result = hex(temp)

    return result
