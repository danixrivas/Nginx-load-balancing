from fastapi import FastAPI

app = FastAPI()

@app.get('/{client}')
async def home(client: str):
    print(client)
    return {"message": "This is server C"}