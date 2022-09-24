from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/health_check")
async def root():
    return {"message": "OK"}
