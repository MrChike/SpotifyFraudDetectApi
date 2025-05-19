from fastapi import APIRouter, Request
from .controller import PreProcessingController


class PreProcessingRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.controller = PreProcessingController()
        self.add_api_route(path="/", endpoint=self.get_preprocessing, methods=["GET"])
        self.add_api_route(path="/update", endpoint=self.update_preprocessing, methods=["GET"])

    def get_preprocessing(self, request: Request):
        return self.controller.get_preprocessing(request)

    def update_preprocessing(self, request: Request):
        return self.controller.update_preprocessing(request)


preprocessing_router = PreProcessingRouter()