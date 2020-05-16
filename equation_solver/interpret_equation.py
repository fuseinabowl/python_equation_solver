from typing import Tuple, Type

from .expression import Expression, Multiply, Term

operation_characters = ['*', '^']
separating_characters = [' ']

non_term_characters = operation_characters + separating_characters

def interpret(input_string : str) -> Expression:
  first_term, remainder = _interpret_first_term(input_string)

  next_non_whitespace_index = _find_first_character_not_in_collection_index(remainder, separating_characters)
  remainder = remainder[next_non_whitespace_index:]

  operator_type, remainder = _interpret_first_operator(remainder)

  next_non_whitespace_index = _find_first_character_not_in_collection_index(remainder, separating_characters)
  remainder = remainder[next_non_whitespace_index:]

  if operator_type is None:
    return first_term
  else:
    sub_operator = interpret(remainder)
    return operator_type(first_term, sub_operator)

def _find_first_non_term_character_index(input_string : str) -> int:
  return _find_first_character_in_collection_index(input_string, non_term_characters)

def _find_first_character_in_collection_index(input_string : str, characters) -> int:
  for i in range(0, len(input_string)):
    if input_string[i] in characters:
      return i
  return len(input_string)

def _find_first_non_operation_character_index(input_string : str) -> int:
  return _find_first_character_not_in_collection_index(input_string, operation_characters)

def _find_first_character_not_in_collection_index(input_string : str, characters) -> int:
  for i in range(0, len(input_string)):
    if input_string[i] not in characters:
      return i
  return len(input_string)

def _interpret_first_term(input_string : str) -> Tuple[Term, str]:
  first_non_term_character_index = _find_first_non_term_character_index(input_string)
  return (Term(input_string[:first_non_term_character_index]), input_string[first_non_term_character_index:])

def _interpret_first_operator(input_string : str) -> Tuple[Type[Expression], str]:
  first_non_equation_character_index = _find_first_non_operation_character_index(input_string)
  equation_type = _get_type_from_string(input_string[:first_non_equation_character_index])
  return (equation_type, input_string[first_non_equation_character_index:])

def _get_type_from_string(input_string : str) -> Type[Expression]:
  if input_string == '*':
    return Multiply
  else:
    return None