from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from .service import *

class MLOpsController:
    def predict_mlops(self, request: Request) -> Response:
        calc = service_calculation()
        return JSONResponse(content=f"Your Response got to the MLOps Controller {calc}", status_code=status.HTTP_200_OK)

