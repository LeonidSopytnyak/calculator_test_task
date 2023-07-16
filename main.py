import os
from typing import Dict

from aiohttp import web

from server.application.const import (
    ADDING_OPERAND,
    SUBTRACT_OPERAND,
    MULTIPLY_OPERAND,
    DIVIDE_OPERAND,
    SQUARE_OPERAND
)
from server.application.controller import CalculatorController
from server.application.handler import CalculatorHandler
from aiohttp_swagger import setup_swagger
from server.application.strategy.calculate_strategy import (
    StrategyContext as CalculateStrategyContext,
    OperandsAddingStrategy, OperandsSubtractStrategy,
    OperandsMultiplyStrategy, OperandsDivideStrategy,
    OperandsSquareStrategy,
)


def create_app():
    application = web.Application()
    strategies = create_strategies()
    calculator_controller = CalculatorController(strategies=strategies)
    calculator_handler = CalculatorHandler(controller=calculator_controller)
    application.router.add_get(
        '/api/v1/calculate',
        calculator_handler.calculate
    )
    application.router.add_get(
        '/api/v1/calculate_square',
        calculator_handler.calculate
    )

    static_dir = os.path.join(os.path.dirname(__file__), 'client')
    application.router.add_static('/client', path=static_dir)

    setup_swagger(
        application,
        swagger_from_file='swagger.yaml',
        swagger_url='/api/v1/doc',
        api_base_url="/api/v1"
    )

    return application


def create_strategies() -> Dict[str, CalculateStrategyContext]:
    strategies = {
        ADDING_OPERAND: CalculateStrategyContext(OperandsAddingStrategy()),
        SUBTRACT_OPERAND: CalculateStrategyContext(OperandsSubtractStrategy()),
        MULTIPLY_OPERAND: CalculateStrategyContext(OperandsMultiplyStrategy()),
        DIVIDE_OPERAND: CalculateStrategyContext(OperandsDivideStrategy()),
        SQUARE_OPERAND: CalculateStrategyContext(OperandsSquareStrategy()),
    }
    return strategies


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)
