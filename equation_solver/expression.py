from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator

class Expression(ABC):
  @abstractmethod
  def _raw_get_subexpressions(self) -> Iterator[Expression]:
    yield from ()

  def get_subexpressions(self) -> Iterator[Expression]:
    for subexpression in self._raw_get_subexpressions():
      yield subexpression
      for recursive_subexpression in subexpression.get_subexpressions():
        yield recursive_subexpression

class Multiply(Expression):
  def __init__(self, left : Expression, right : Expression):
    self._left = left
    self._right = right

  def _raw_get_subexpressions(self) -> Iterator[Expression]:
    yield self._left
    yield self._right

  @property
  def left(self) -> Expression:
    return self._left

  @property
  def right(self) -> Expression:
    return self._right

  def __str__(self) -> str:
    return str(self._left) + ' * ' + str(self._right)

class Term(Expression):
  def __init__(self, identifier : str):
    self._identifier = identifier

  def _raw_get_subexpressions(self) -> Iterator[Expression]:
    return super()._raw_get_subexpressions()

  @property
  def identifier(self) -> str:
    return self._identifier

  def __str__(self) -> str:
    return self._identifier

class Exponent(Expression):
  def __init__(self, base : Expression, exponent : float):
    self._base = base
    self._exponent = exponent

  def _raw_get_subexpressions(self) -> Iterator[Expression]:
    yield self._base

  @property
  def base(self) -> Expression:
    return self._base

  @property
  def exponent(self) -> float:
    return self._exponent

  def __str__(self) -> str:
    return str(self._base) + '^' + str(self._exponent)