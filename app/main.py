from fastapi import FastAPI, Request

from .routes.v1 import user

app = FastAPI(
    title="Cloud Run API Demo", description="", version="0.1.0", redoc_url=None
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    import time

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def hello():
    return {"hello": "world"}


app.include_router(user.router, prefix="/api/v1/users", tags=["User"])
