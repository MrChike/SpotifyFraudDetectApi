from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from .service import *

class PreProcessingController:
    def get_preprocessing(self, request: Request) -> Response:
        calc = service_calculation()
        return JSONResponse(content=f"Your Response got to the PreProcessing Controller {calc}", status_code=status.HTTP_200_OK)

    def update_preprocessing(self, request: Request) -> Response:
        return JSONResponse(content="Your Response Updated the PreProcessing Controller", status_code=status.HTTP_200_OK)

