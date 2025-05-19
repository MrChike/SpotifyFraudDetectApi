from fastapi import APIRouter, Request
from .controller import MLOpsController


class MLOpsRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.controller = MLOpsController()
        self.add_api_route(path="/", endpoint=self.predict_mlops, methods=["GET"])

    def predict_mlops(self, request: Request):
        return self.controller.predict_mlops(request)



mlops_router = MLOpsRouter()