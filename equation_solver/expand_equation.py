from typing import Tuple, Type

from .interpret_equation import interpret
from .simplify_expression import simplify_expression

def expand_equation(equation_string : str) -> str:
  interpreted_equation = interpret(equation_string)
  simplified_expression = simplify_expression(interpreted_equation)
  return str(simplified_expression)