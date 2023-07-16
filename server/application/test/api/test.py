import pytest
from aiohttp import web

from server.application.const import (
    BASE_CALCULATION_URL,
    SQUARE_CALCULATION_URL,
    ADDING_OPERAND,
    SQUARE_OPERAND
)
from server.application.controller import CalculatorController
from server.application.handler import CalculatorHandler
from server.application.test.base import calculator_controller


@pytest.fixture()
def client(loop, aiohttp_client, calculator_controller: CalculatorController):
    app = web.Application()
    calculator_handler = CalculatorHandler(controller=calculator_controller)

    app.router.add_get(
        path=BASE_CALCULATION_URL,
        handler=calculator_handler.calculate
    )
    app.router.add_get(
        path=SQUARE_CALCULATION_URL,
        handler=calculator_handler.calculate
    )
    return loop.run_until_complete(aiohttp_client(app))


@pytest.mark.asyncio
async def test_calculate_endpoint(client):
    params = {
        'first_operand': '2',
        'second_operand': '3',
        'operator': ADDING_OPERAND
    }
    response = await client.get(BASE_CALCULATION_URL, params=params)
    assert response.status == 200
    data = await response.json()
    assert 'result' in data
    assert data['result'] == 5


@pytest.mark.asyncio
async def test_calculate_square_endpoint(client):
    params = {'number': '4', 'operator': SQUARE_OPERAND}
    response = await client.get(SQUARE_CALCULATION_URL, params=params)
    assert response.status == 200
    data = await response.json()
    assert 'result' in data
    assert data['result'] == 16
