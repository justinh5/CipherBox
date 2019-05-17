import unittest
from Crypt0.Caesar import CEnDecode
from Crypt0.Vigenere import VEnDecode
from Crypt0.OTP import OTPencrypt
from Convert.Numbers.Convert import convert_dunits
from Arithmetic.Numbers.Primality.Primality import is_prime, next_prime

# python3 -m unittest tests/test_basic.py


class TestArithmetic(unittest.TestCase):

    def test(self):
        self.assertEqual(is_prime(79), True)
        self.assertEqual(is_prime(80), False)
        self.assertEqual(is_prime(76756756756744646753673045994395940569596680657), True)
        self.assertEqual(is_prime(45365546356567576573567657567635756753676574560), False)
        self.assertEqual(next_prime(4), 5)
        self.assertEqual(next_prime(5), 7)
        self.assertEqual(next_prime(5645645645645645645), 5645645645645645663)
        self.assertEqual(next_prime(90969709979690198342), 90969709979690198351)


class TestConverters(unittest.TestCase):

    def test_dunits(self):
        self.assertEqual(convert_dunits(50, 'bit', 'byte'), 6.25)
        self.assertEqual(convert_dunits(50, 'bit', 'pebibyte'), 5.551115123125783e-15)
        self.assertEqual(convert_dunits(50, 'megabit', 'bit'), 5e7)
        self.assertEqual(convert_dunits(50, 'byte', 'bit'), 400)
        self.assertEqual(convert_dunits(50, 'byte', 'gibibyte'), 4.6566128730773926e-08)


class TestCrypto(unittest.TestCase):

    def test_caesar(self):
        self.assertEqual(CEnDecode.encode("", 5), "")
        self.assertEqual(CEnDecode.encode("Jupiter", 5), "Ozunyjw")
        self.assertEqual(CEnDecode.encode("Jupiter1234", 5), "Ozunyjw1234")
        self.assertEqual(CEnDecode.encode("Jupiter Saturn", 5), "Ozunyjw Xfyzws")
        self.assertEqual(CEnDecode.decode("", 5, True), "")
        self.assertEqual(CEnDecode.decode("Ozunyjw", 5, True), "Jupiter")
        self.assertEqual(CEnDecode.decode("Ozunyjw1234", 5, True), "Jupiter1234")
        self.assertEqual(CEnDecode.decode("Ozunyjw Xfyzws", 5, True), "Jupiter Saturn")

    def test_vigenere(self):
        self.assertEqual(VEnDecode.encode("", "A"), "")
        self.assertEqual(VEnDecode.encode("Lemons", "monkey"), "Xszyrq")
        self.assertEqual(VEnDecode.encode("Lemons1234", "monkey"), "Xszyrq1234")
        self.assertEqual(VEnDecode.encode("Lemon's juice", "monkey"),"Xszyr'q vivmi")
        with self.assertRaises(IndexError):
            VEnDecode.encode("Lemon", "")
        self.assertEqual(VEnDecode.decode("", "A"), "")
        self.assertEqual(VEnDecode.decode("Xszyrq", "monkey"), "Lemons")
        self.assertEqual(VEnDecode.decode("Xszyrq1234", "monkey"), "Lemons1234")
        self.assertEqual(VEnDecode.decode("Xszyr'q vivmi", "monkey"), "Lemon's juice")

    def test_otp(self):
        self.assertEqual(OTPencrypt.encrypt("", "keykeykey"), "")
        self.assertEqual(OTPencrypt.encrypt("PineTrees", "keykeykey"), "ZmloXpoiq")
        self.assertEqual(OTPencrypt.encrypt("PineTrees####", "keykeykey"), "ZmloXpoiq####")
        self.assertEqual(OTPencrypt.encrypt("Pine Trees", "key"), "Zmle Trees")
        with self.assertRaises(IndexError):
            OTPencrypt.encrypt("PineTrees", "")
        self.assertEqual(OTPencrypt.decrypt("", "keykeykey"), "")
        self.assertEqual(OTPencrypt.decrypt("ZmloXpoiq", "keykeykey"), "PineTrees")
        self.assertEqual(OTPencrypt.decrypt("ZmloXpoiq####", "keykeykey"), "PineTrees####")
        self.assertEqual(OTPencrypt.decrypt("Zmle Trees", "key"), "Pine Trees")


class TestStrings(unittest.TestCase):

    def test_utf8(self):
        return
