from .expression import Expression
from .simplification_rules.multiply_same_to_power import MultiplySameToPower

rules = [MultiplySameToPower()]

def simplify_expression(expression : Expression) -> Expression:
  for rule in rules:
    if rule.can_be_applied(expression):
      expression = rule.apply(expression)
  
  return expression