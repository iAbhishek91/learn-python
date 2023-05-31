from fastapi import FastAPI

app = FastAPI() # app  is fastapi instance and FastAPI is a class


@app.get("/")
async def root():
    return {"message": "Hello World"}