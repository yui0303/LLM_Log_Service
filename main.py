from fastapi import FastAPI

from app.routers.setup_router import setup_router



app = FastAPI(
    title="Backend API",
    description="待補....",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

setup_router(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}