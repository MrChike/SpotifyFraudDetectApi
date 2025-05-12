from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from analytics.routers.router import AnalyticsRouter
from detection.routers.router import DetectionRouter
from ingestion.routers.router import IngestionRouter 

app = FastAPI()

# Include routers from different modules
app.include_router(AnalyticsRouter, prefix="/analytics", tags=["analytics"])
app.include_router(DetectionRouter, prefix="/detection", tags=["detection"])
app.include_router(IngestionRouter, prefix="/ingestion", tags=["ingestion"])

# Optional: Add CORS, error handling, etc.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or a more restricted list of origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Error handling (optional)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": "Validation error occurred", "errors": exc.errors()},
    )

if __name__ == "__main__":
    # Run the application (if running directly for local dev purposes)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
