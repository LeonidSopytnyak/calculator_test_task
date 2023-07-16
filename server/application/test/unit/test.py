from server.application.const import (
    ADDING_OPERAND,
    SQUARE_OPERAND,
    SUBTRACT_OPERAND,
    MULTIPLY_OPERAND,
    DIVIDE_OPERAND
)
from server.application.controller import CalculatorController
from server.application.test.base import calculator_controller


def test_01_calculate_add(calculator_controller: CalculatorController):
    result = calculator_controller.calculate_according_to_strategy(
        operator=ADDING_OPERAND, first_operand=2, second_operand=3, number=0
    )
    assert result == 5


def test_02_calculate_subtract(calculator_controller: CalculatorController):
    result = calculator_controller.calculate_according_to_strategy(
        operator=SUBTRACT_OPERAND, first_operand=5, second_operand=3, number=0
    )
    assert result == 2


def test_03_calculate_multiply(calculator_controller: CalculatorController):
    result = calculator_controller.calculate_according_to_strategy(
        operator=MULTIPLY_OPERAND, first_operand=4, second_operand=2, number=0
    )
    assert result == 8


def test_04_calculate_divide(calculator_controller: CalculatorController):
    result = calculator_controller.calculate_according_to_strategy(
        operator=DIVIDE_OPERAND, first_operand=10, second_operand=2, number=0
    )
    assert result == 5


def test_05_calculate_square(calculator_controller: CalculatorController):
    result = calculator_controller.calculate_according_to_strategy(
        operator=SQUARE_OPERAND, number=4, first_operand=0, second_operand=0
    )
    assert result == 16
