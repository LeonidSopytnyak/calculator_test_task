from typing import Dict


class CalculatorView:
    @staticmethod
    def render_result(result) -> Dict[str, float]:
        return {'result': result}
