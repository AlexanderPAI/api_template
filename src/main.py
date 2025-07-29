import uvicorn
from fastapi import FastAPI

from src.api.v1.router import router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "OK"}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)