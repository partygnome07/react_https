from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

# This lets us verify /docs is up before adding any parser logic.
