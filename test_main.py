# test_main.py — 🧑‍✈️ Kapitan yozadi, 🧠 Mantiqchi kodini tekshiradi
import unittest, os
from main import Royxat

class RoyxatTest(unittest.TestCase):
    def setUp(self):
        self.r = Royxat()
        self.r.qosh("Dars qilish")

    def test_qosh(self):
        self.r.qosh("Non olish")
        self.assertEqual(len(self.r), 2)

    def test_bajar(self):
        self.assertTrue(self.r.bajar(0))
        self.assertFalse(self.r.bajar(0))

    def test_saqla_yukla(self):
        self.r.saqla("test_tmp.json")
        r2 = Royxat.yukla("test_tmp.json")
        self.assertEqual(len(r2), 1)

    def tearDown(self):
        if os.path.exists("test_tmp.json"):
            os.remove("test_tmp.json")