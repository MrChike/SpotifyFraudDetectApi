from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from .service import service_calculation
from .model import K3Score

class EventDetectionController:
    def get_event_detection(self, request: Request) -> Response:
        k3_score = K3Score()  # Create an instance of K1Score
        calc = service_calculation(k3_score)
        return JSONResponse(content=f"Your Response got to the event_detection Controller {calc}", status_code=status.HTTP_200_OK)

    def update_event_detection(self, request: Request) -> Response:
        return JSONResponse(content="Your Response Updated the event_detection Controller", status_code=status.HTTP_200_OK)

