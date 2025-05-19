from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from .service import service_calculation
from .model import K4Score

class IngestionController:
    def get_ingestion(self, request: Request) -> Response:
        k1_score = K4Score()  # Create an instance of K4Score
        calc = service_calculation(k1_score)
        return JSONResponse(content=f"Your Response got to the Ingestion Controller {calc}", status_code=status.HTTP_200_OK)

    def update_ingestion(self, request: Request) -> Response:
        return JSONResponse(content="Your Response Updated the Ingestion Controller", status_code=status.HTTP_200_OK)

