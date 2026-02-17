from fastapi import FastAPI

app = FastAPI(title="Loyalty Program API", version="1.0.0")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)