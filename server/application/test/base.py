import pytest
from server.application.const import (
    ADDING_OPERAND,
    SQUARE_OPERAND,
    SUBTRACT_OPERAND,
    MULTIPLY_OPERAND,
    DIVIDE_OPERAND
)
from server.application.controller import CalculatorController
from server.application.strategy.calculate_strategy import (
    StrategyContext as CalculateStrategyContext,
    OperandsAddingStrategy,
    OperandsSubtractStrategy,
    OperandsDivideStrategy,
    OperandsMultiplyStrategy,
    OperandsSquareStrategy,
)


@pytest.fixture(scope='session')
def calculator_controller():
    strategies = {
        ADDING_OPERAND: CalculateStrategyContext(OperandsAddingStrategy()),
        SUBTRACT_OPERAND: CalculateStrategyContext(
            OperandsSubtractStrategy()),
        MULTIPLY_OPERAND: CalculateStrategyContext(
            OperandsMultiplyStrategy()),
        DIVIDE_OPERAND: CalculateStrategyContext(OperandsDivideStrategy()),
        SQUARE_OPERAND: CalculateStrategyContext(OperandsSquareStrategy()),
    }
    fixture_calculator_controller = CalculatorController(strategies=strategies)
    return fixture_calculator_controller


__all__ = ['calculator_controller']
