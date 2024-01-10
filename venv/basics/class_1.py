from fastapi import FastAPI

#creating basic fastapi app

app = FastAPI()

@app.get("/")
async def first_app():
    return {"message": "we are ready to go with Fast API"}

