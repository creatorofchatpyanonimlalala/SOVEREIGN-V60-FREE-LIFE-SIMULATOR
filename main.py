from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
app = FastAPI()
@app.get("/api/world")
def world(): return {"status":"SOVEREIGN LIVE"}
app.mount("/", StaticFiles(directory=".", html=True), name="static")
