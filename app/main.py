from fastapi import FastAPI
from app.api.routes.router import router

app = FastAPI(
    title="shallowresearchscholarspark",
    description="This is the service that handles the shallow research aspect of the scholar spark",
    version="0.1.2"
)

app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}