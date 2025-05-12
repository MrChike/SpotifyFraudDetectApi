from fastapi import APIRouter

DetectionRouter = APIRouter()

# Define your routes here
@DetectionRouter.get("/")
async def get_detection():
    return {"message": "Detection endpoint"}