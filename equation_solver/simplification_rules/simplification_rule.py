from abc import ABC, abstractmethod

from ..expression import Expression

class SimplificationRule(ABC):
  @abstractmethod
  def can_be_applied(self, expression : Expression) -> bool:
    return False

  @abstractmethod
  def apply(self, expression : Expression) -> Expression:
    return expression