from fastapi import APIRouter, Request
from .controller import AnalyticsController


class AnalyticsRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self.controller = AnalyticsController()
        self.add_api_route(path="/", summary="Retrieve Analysis", endpoint=self.get_analytics, methods=["GET"])
        self.add_api_route(path="/update", summary="Update Analytics", endpoint=self.update_analytics, methods=["POST"])

    def get_analytics(self, request: Request):
        return self.controller.get_analytics(request)

    def update_analytics(self, request: Request):
        return self.controller.update_analytics(request)


analytics_router = AnalyticsRouter()