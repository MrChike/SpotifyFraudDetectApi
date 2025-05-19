from fastapi import APIRouter, Request
from .controller import DecisionEngineController


class DecisionEngineRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.controller = DecisionEngineController()
        self.add_api_route(path="/", endpoint=self.get_decisions, methods=["GET"])
        self.add_api_route(path="/update", endpoint=self.update_decisions, methods=["GET"])

    def get_decisions(self, request: Request):
        return self.controller.get_decisions(request)

    def update_decisions(self, request: Request):
        return self.controller.update_decisions(request)


decisions_router = DecisionEngineRouter()