from fastapi import APIRouter, Request
from .controller import IngestionController


class IngestionRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.controller = IngestionController()
        self.add_api_route(path="/", endpoint=self.get_ingestion, methods=["GET"])
        self.add_api_route(path="/update", endpoint=self.update_ingestion, methods=["GET"])

    def get_ingestion(self, request: Request):
        return self.controller.get_ingestion(request)

    def update_ingestion(self, request: Request):
        return self.controller.update_ingestion(request)


ingestion_router = IngestionRouter()