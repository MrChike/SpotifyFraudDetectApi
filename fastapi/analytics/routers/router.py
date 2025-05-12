from fastapi import APIRouter

AnalyticsRouter = APIRouter()

# Define your routes here
@AnalyticsRouter.get("/")
async def get_analytics():
    return {"message": "Analytics endpoint"}


