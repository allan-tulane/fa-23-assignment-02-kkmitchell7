from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply_help(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply_help(BinaryNumber(14), BinaryNumber(5)) == 5*14
