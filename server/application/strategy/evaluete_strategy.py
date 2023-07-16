from abc import (
    ABC,
    abstractmethod
)
from typing import Optional


class EvaluateStrategy(ABC):

    @abstractmethod
    def calculate(
            self,
            expression: str
    ):
        pass


class StrategyContext:
    def __init__(self, strategy: EvaluateStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> EvaluateStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: EvaluateStrategy) -> None:
        self._strategy = strategy

    def evaluate(
            self,
            expression: str
    ):
        return self._strategy.calculate(
            expression=expression
        )


class ExpressionEvaluateStrategy(EvaluateStrategy):
    def calculate(
            self,
            expression: str
    ):
        expression = expression.replace('s', '**')
        result = eval(expression)
        return result
