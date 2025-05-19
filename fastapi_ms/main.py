from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analytics.router import analytics_router as AnalyticsRouter
from decision_engine.router import decisions_router as DecisionEngineRouter
from event_detection.router import event_detection_router as EventDetectionRouter
from ingestion.router import ingestion_router as IngestionRouter
from mlops.router import mlops_router as MLOpsRouter
from preprocessing.router import preprocessing_router as PreProcessingRouter
from shared.configs.settings import app_settings as AppSettings


app = FastAPI(
    title="Spotify Fraud Detect API",
    description="""A modular and scalable system designed to detect and 
    respond to fraudulent activities on streaming 
    platforms in real-time created by""",
    docs_url="/",
    version="0.0.1",
    contact={
        "name": AppSettings.contact_name,
        "url": AppSettings.contact_info,
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

app.include_router(AnalyticsRouter, prefix="/analyze", tags=["analytics"])
app.include_router(DecisionEngineRouter, prefix="/decide", tags=["decision-engine"])
app.include_router(EventDetectionRouter, prefix="/detect", tags=["event-detection"])
app.include_router(IngestionRouter, prefix="/ingest", tags=["ingestion"])
app.include_router(MLOpsRouter, prefix="/predict", tags=["prediction"])
app.include_router(PreProcessingRouter, prefix="/preprocess", tags=["preprocessing"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
