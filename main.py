from fastapi import FastAPI, Response
import requests

app = FastAPI()

BASE_URL = "http://161.132.41.249:3001/api/reniec"
TOKEN = "1596bd13-65ff-458e-8105-daadb93417e9"

@app.get("/api/reniec/{dni}")
def bridge(dni: str):
    target_url = f"{BASE_URL}/{dni}?token={TOKEN}"
    try:
        response = requests.get(target_url)
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="application/json"
        )
    except Exception as e:
        return {"error": "Connection error", "detail": str(e)}

@app.get("/")
def health():
    return {"status": "online"}

