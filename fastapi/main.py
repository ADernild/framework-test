import asyncio
import time

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/api/ping/")
async def ping():
    return JSONResponse(status_code=200, content={"message": "pong"})


@app.get("/api/sleep-sync/")
def sleep_sync():
    time.sleep(1)
    return JSONResponse(
        status_code=200, content={"message": "Synchronous sleep complete"}
    )


@app.get("/api/sleep-async/")
async def sleep_async():
    await asyncio.sleep(1)
    return JSONResponse(
        status_code=200, content={"message": "Asynchronous sleep complete"}
    )
