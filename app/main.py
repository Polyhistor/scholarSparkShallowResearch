from fastapi import FastAPI
from app.api.routes.router import router

app = FastAPI(
    title="shallowresearchscholarspark",
    description="A FastAPI microservice",
    version="0.2.0"
)

app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}