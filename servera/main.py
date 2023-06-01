from fastapi import FastAPI

app = FastAPI()

@app.get('/{client}')
async def home(client):
    print(client)
    return {"message": "This is server A"}