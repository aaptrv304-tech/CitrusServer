from fastapi import APIRouter
from . import shifts, nfc, visits

router = APIRouter()

# Подключение роутеров для приложения кассира
router.include_router(shifts.router, prefix="/shifts", tags=["shifts"])
router.include_router(nfc.router, prefix="/nfc", tags=["nfc"])
router.include_router(visits.router, prefix="/visits", tags=["visits"])