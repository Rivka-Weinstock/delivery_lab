from typing import Optional
from fastapi import FastAPI, Body, Request, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()



@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc.detail)}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid request body or query parameters"}
    )


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/deliveries")
def get_deliveries(status: Optional[str] = None):
    return []

@app.get("/deliveries/{delivery_id}")
def get_delivery(delivery_id: int):
    return {"id": delivery_id}

@app.post("/deliveries", status_code=201)
def create_delivery(data: dict = Body(...)):
    return {"status": "created"}

@app.patch("/deliveries/{delivery_id}")
def update_delivery(delivery_id: int, data: dict = Body(...)):
    return {"status": "updated"}

@app.delete("/deliveries/{delivery_id}")
def delete_delivery(delivery_id: int):
    return Response(status_code=204)