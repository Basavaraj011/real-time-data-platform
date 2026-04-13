from fastapi import FastAPI

app = FastAPI(
    title="Real-Time Data Platform",
    description="Ingestion service for event streaming",
    version="0.1.0"
)

@app.get("/health")
async def health():
    return {"status": "healthy"}