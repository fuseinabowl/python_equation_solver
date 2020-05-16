from .simplification_rule import SimplificationRule

from ..expression import Multiply, Term, Exponent, Expression

class MultiplySameToPower(SimplificationRule):
  def can_be_applied(self, expression : Expression) -> bool:
    if type(expression) is Multiply:
      if type(expression.left) is Term and type(expression.right) is Term:
        return expression.left.identifier == expression.right.identifier

  def apply(self, expression : Expression) -> Expression:
    return Exponent(expression.left.identifier, 2)