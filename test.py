#Test additioonner deux nombres

#Test additionner chaines de caracteres
from main import add, divide

from unittest import TestCase
import pytest



def test_add_two_numbers():
    assert add(5,10)==15

def test_add_two_string():
    assert add('a','b')=='ab'

def test_add_boolean():
    assert add(True,True)==2
    assert add(False,False)==0
    assert add(True,False)==1
    assert add(False,True)==1

def test_with_none():
    with pytest.raises(TypeError):
        add(None, None)


def test_devide_obtain_virgule():
    assert divide(5,2)==2.5

def test_cas_critic():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)


