import pytest
import re

from ..expand_equation import expand_equation
from .. import interpret_equation
from ..expression import Multiply, Term

@pytest.mark.parametrize("input_string", [("a"), ("b"), ("c")])
def test_with_single_character_single_term_unchanged(input_string : str):
  assert expand_equation(input_string) == input_string

@pytest.mark.parametrize("input_string", [("ab"), ("bc"), ("cd")])
def test_with_multiple_character_single_term_unchanged(input_string : str):
  assert expand_equation(input_string) == input_string

@pytest.mark.parametrize("first_term,second_term", [("a","b",), ("b","c",), ("c","ab",)])
def test_with_two_different_terms_multiplied_with_spaces_effectively_unchanged(first_term : str, second_term : str):
  input_string = first_term + ' * ' + second_term
  output_string = expand_equation(input_string)
  assert re.match(first_term + r'\s*\*\s*' + second_term, output_string) is not None, output_string

@pytest.mark.parametrize("first_term,second_term", [("a","b",), ("b","c",), ("c","ab",)])
def test_with_two_different_terms_multiplied_with_spaces_interpreted_as_multiply(first_term : str, second_term : str):
  input_string = first_term + ' * ' + second_term
  interpreted_equation = interpret_equation.interpret(input_string)
  assert type(interpreted_equation) is Multiply
  assert type(interpreted_equation.left) is Term
  assert interpreted_equation.left.identifier == first_term
  assert type(interpreted_equation.right) is Term
  assert interpreted_equation.right.identifier == second_term

def test_interpret_single_multiply_sign_as_multiply():
  assert interpret_equation._interpret_first_operator('*')[0] is Multiply

@pytest.mark.parametrize("trailing_contents", [("a"), ("b"), ("c"), (" c"), ("    alsk a")])
def test_interpret_multiply_sign_with_trailing_contents_as_multiply(trailing_contents : str):
  assert interpret_equation._interpret_first_operator('*' + trailing_contents)[0] is Multiply

@pytest.mark.parametrize("trailing_contents", [("a"), ("b"), ("c"), (" c"), ("    alsk a")])
def test_interpret_multiply_sign_with_trailing_contents_remainder_is_trailing_contents(trailing_contents : str):
  assert interpret_equation._interpret_first_operator('*' + trailing_contents)[1] == trailing_contents

@pytest.mark.parametrize("term", [("a"), ("b"), ("ca")])
def test_with_two_same_terms_multiplied_with_spaces_changed_to_term_power_two(term : str):
  input_string = term + ' * ' + term
  output_string = expand_equation(input_string)
  assert output_string == term + '^2'