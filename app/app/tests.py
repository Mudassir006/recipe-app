from django.test import SimpleTestCase

from app import calc

class calcTest(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5,6)

        self.assertEqual(res,11) 

    def test_subtract_numbers(self):
        res = calc.subtract(8,19)

        self.assertEqual(res,11)
