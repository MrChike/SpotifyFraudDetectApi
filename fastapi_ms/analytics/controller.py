from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from .service import *
from .model import K1Score

class AnalyticsController:
    def get_analytics(self, request: Request) -> Response:
        k1_score = K1Score()  # Create an instance of K1Score
        calc = service_calculation(k1_score)
        return JSONResponse(content=f"Your Response got to the Analytics Controller {calc}", status_code=status.HTTP_200_OK)

    def update_analytics(self, request: Request) -> Response:
        return JSONResponse(content="Your Response Updated the Analytics Controller", status_code=status.HTTP_200_OK)

