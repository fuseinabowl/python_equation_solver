import pytest

from ..expression import Multiply, Term

def test_term_expression_iterate_over_subexpressions_is_empty():
  term = Term('id')
  subexpressions = list(term.get_subexpressions())
  assert len(subexpressions) == 0
  
def test_multiply_expression_iterate_over_subexpressions_is_the_two_terms():
  left = Term('left')
  right = Term('right')
  multiply = Multiply(left, right)
  subexpressions = list(multiply.get_subexpressions())
  assert len(subexpressions) == 2
  assert subexpressions[0] is left
  assert subexpressions[1] is right