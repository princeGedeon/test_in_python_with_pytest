#Test additioonner deux nombres

#Test additionner chaines de caracteres
from main import add

from unittest import TestCase


class TestCalculatrice(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(5,10),15)

    def test_add_two_string(self):
        self.assertEqual(add('a','b'),'ab')

    def test_add_boolean(self):
        self.assertEqual(add(True,True),2)
        self.assertEqual(add(False,False),0)
        self.assertEqual(add(True,False),1)
        self.assertEqual(add(False,True),1)


