from fastapi import APIRouter

IngestionRouter = APIRouter()

# Define your routes here
@IngestionRouter.get("/")
async def get_ingestion():
    return {"message": "Ingestion endpoint"}