from fastapi import APIRouter, Request
from .controller import EventDetectionController


class EventDetectionRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.controller = EventDetectionController()
        self.add_api_route(path="/", endpoint=self.get_event_detection, methods=["GET"])
        self.add_api_route(path="/update", endpoint=self.update_event_detection, methods=["GET"])

    def get_event_detection(self, request: Request):
        return self.controller.get_event_detection(request)

    def update_event_detection(self, request: Request):
        return self.controller.update_event_detection(request)


event_detection_router = EventDetectionRouter()