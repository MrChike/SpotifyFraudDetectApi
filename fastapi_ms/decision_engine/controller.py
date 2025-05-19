from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from .service import *
from .model import K2Score

class DecisionEngineController:
    def get_decisions(self, request: Request) -> Response:
        k2_score = K2Score()  # Create an instance of K2Score
        calc = service_calculation(k2_score)
        return JSONResponse(content=f"Your Response got to the Decision Engine Controller {calc}", status_code=status.HTTP_200_OK)

    def update_decisions(self, request: Request) -> Response:
        return JSONResponse(content="Your Response Updated the Decision Engine Controller", status_code=status.HTTP_200_OK)

