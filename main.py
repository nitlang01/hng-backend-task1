from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

CATFACT_URL = "https://catfact.ninja/fact"
CATFACT_TIMEOUT = float(os.getenv("CATFACT_TIMEOUT", "5"))
FALLBACK_FACT = os.getenv("FALLBACK_FACT", "No cat facts available right now. Try again later.")

USER_EMAIL = os.getenv("USER_EMAIL", "your-email@example.com")
USER_NAME = os.getenv("USER_NAME", "Your Full Name")
USER_STACK = os.getenv("USER_STACK", "Python/FastAPI")

@app.get("/me")
async def me():
    cat_fact = FALLBACK_FACT
    try:
        async with httpx.AsyncClient(timeout = CATFACT_TIMEOUT) as client:
            response = await client.get(CATFACT_URL)
            response.raise_for_status()
            cat_fact = response.json().get("fact", FALLBACK_FACT)
    except Exception:
        cat_fact = FALLBACK_FACT

    data = {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }            
    return JSONResponse(content=data)