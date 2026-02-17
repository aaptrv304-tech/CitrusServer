from fastapi import APIRouter
from . import businesses, rewards, statistics

router = APIRouter()

# Подключение роутеров для панели владельца бизнеса
router.include_router(businesses.router, prefix="/businesses", tags=["businesses"])
router.include_router(rewards.router, prefix="/rewards", tags=["rewards"])
router.include_router(statistics.router, prefix="/statistics", tags=["statistics"])