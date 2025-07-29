from fastapi import APIRouter, Query, Body, File, UploadFile
from fastapi.exceptions import ResponseValidationError, HTTPException

from src.api.v1.data.schemes import Data, DataResponse

from typing import Optional

router = APIRouter(prefix="/endpoints")


@router.post("/send_data_query")
async def send_data_query(data: str = Query(...)):
    return {"data": data}

@router.post("/send_data_body")
async def send_data_body(data: str = Body(...)):
    return {"data": data}


@router.post("/send_data_schema", response_model=DataResponse)
async def send_data_body(data: Data):
    data.data += " this is new data"
    return {"new_data": data}
