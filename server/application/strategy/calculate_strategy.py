from abc import (
    ABC,
    abstractmethod
)
from typing import Optional


class CalculateStrategy(ABC):

    @abstractmethod
    def calculate(
            self,
            first_operand: float,
            second_operand: float,
            number: Optional[float] = None
    ):
        pass


class StrategyContext:
    def __init__(self, strategy: CalculateStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> CalculateStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: CalculateStrategy) -> None:
        self._strategy = strategy

    def calculate(
            self,
            first_operand: float,
            second_operand: float,
            number: Optional[float] = None
    ):
        return self._strategy.calculate(
            first_operand=first_operand,
            second_operand=second_operand,
            number=number
        )


class OperandsAddingStrategy(CalculateStrategy):
    def calculate(
            self,
            first_operand: float,
            second_operand: float,
            number: Optional[float] = None
    ):
        return first_operand + second_operand


class OperandsSubtractStrategy(CalculateStrategy):
    def calculate(
            self,
            first_operand: float,
            second_operand: float,
            number: Optional[float] = None
    ):
        return first_operand - second_operand


class OperandsMultiplyStrategy(CalculateStrategy):
    def calculate(
            self,
            first_operand: float,
            second_operand: float,
            number: Optional[float] = None
    ):
        return first_operand * second_operand


class OperandsDivideStrategy(CalculateStrategy):
    def calculate(
            self,
            first_operand: float,
            second_operand: float,
            number: Optional[float] = None
    ):
        if not second_operand:
            raise ValueError('Division by zero is not allowed')
        return first_operand / second_operand


class OperandsSquareStrategy(CalculateStrategy):
    def calculate(
            self,
            first_operand: float,
            second_operand: float,
            number: Optional[float] = None
    ):
        return number ** 2
