from fastapi import APIRouter
from . import users, businesses, rewards, visits

router = APIRouter()

# Подключение роутеров для админ панели
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(businesses.router, prefix="/businesses", tags=["businesses"])
router.include_router(rewards.router, prefix="/rewards", tags=["rewards"])
router.include_router(visits.router, prefix="/visits", tags=["visits"])