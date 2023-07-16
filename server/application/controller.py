from typing import Dict, Union

from server.application.strategy.calculate_strategy import \
    StrategyContext as CalculateStrategyContext


class CalculatorController:

    def __init__(self, strategies: Dict[str, Union[CalculateStrategyContext]]):
        self.strategies = strategies

    def calculate_according_to_strategy(
            self,
            operator: str,
            first_operand: float,
            second_operand: float,
            number: float,
    ) -> float:
        """
        Calculate the result based on the provided operator and operands.

        Args:
            operator (str): The arithmetic operator to use in the calculation.
            first_operand (float): The first operand.
            second_operand (float): The second operand.
            number (float): The number for the square operation.

        Returns:
            float: The calculated result.

        Raises:
            ValueError: If the operator is not supported.

        The calculate_according_to_strategy method selects the appropriate
        calculation strategy based on the provided operator and performs the
        calculation using the operands and number.

        If the operator is found in the available strategies,
        the method delegates the calculation to the corresponding strategy
        and returns the result. If the operator is not supported,
        a ValueError is raised.

        Note: The calculate_according_to_strategy method assumes
        that all operands are provided, even if they are not relevant for a
        specific operator. For example, the square operator only uses the
        number parameter and ignores the operands.
        """
        strategy = self.strategies.get(operator)
        if strategy:
            return strategy.calculate(
                first_operand=first_operand,
                second_operand=second_operand,
                number=number
            )
        else:
            raise ValueError('This operation not include')
