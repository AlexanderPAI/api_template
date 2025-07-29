from fastapi import APIRouter

from src.api.v1.data import endpoints

router = APIRouter(prefix="/v1")

router.include_router(endpoints.router)
