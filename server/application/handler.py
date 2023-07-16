from aiohttp import web
from aiohttp.web import Request
from aiohttp.web_response import Response
from server.application.controller import CalculatorController
from server.application.view import CalculatorView


class CalculatorHandler:
    def __init__(
            self,
            controller: CalculatorController
    ):
        self.controller = controller
        self.view = CalculatorView()

    async def calculate(self, request: Request) -> Response:
        """
        Calculate the result based on the provided query parameters.
        Args:
            request (Request): The HTTP request object.
        Returns:
            Response: The HTTP response object.
        Raises:
            ValueError: If there is an error in the calculation or
            invalid input.

        The `calculate` method extracts the query parameters from the request
        and performs the calculation based on the provided operands and
        operator.
        The available query parameters are:
        - operator: The arithmetic operator to use in
          the calculation (default: '+').
        - first_operand: The first operand (default: 0).
        - second_operand: The second operand (default: 0).
        - number: The number to be squared (default: 0).

        The method delegates the calculation to the controller, according to
        provided strategies handles any potential errors, and returns an HTTP
        response with the calculated result or an error message.
        """
        operator = request.query.get('operator').strip() or '+'
        first_operand = float(request.query.get('first_operand', 0))
        second_operand = float(request.query.get('second_operand', 0))
        number = float(request.query.get('number', 0))

        try:
            result = self.controller.calculate_according_to_strategy(
                operator=operator,
                first_operand=first_operand,
                second_operand=second_operand,
                number=number
            )
            response = self.view.render_result(result)
            return web.json_response(response)
        except ValueError as e:
            return web.Response(status=400, text=str(e))

