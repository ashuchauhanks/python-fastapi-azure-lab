from fastapi import FastAPI
from datetime import datetime, timezone
app = FastAPI(title="Azure App Service Lab")
@app.get("/")
def home():
    return {"message": "Hello from Azure App Service Lab", "status": "running"}
@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}
