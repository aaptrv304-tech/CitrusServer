from fastapi import FastAPI
from database.session import engine
from database.base import Base
from api.admin.routers import router as admin_router
from api.business_owner.routers import router as business_owner_router
from api.cashier.routers import router as cashier_router
from api.frontend.routers import router as frontend_router

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loyalty Program API", version="1.0.0")

# Подключение роутеров
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(business_owner_router, prefix="/business_owner", tags=["business_owner"])
app.include_router(cashier_router, prefix="/cashier", tags=["cashier"])
app.include_router(frontend_router, prefix="/frontend", tags=["frontend"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)