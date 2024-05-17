from http import HTTPStatus

from src.app import app

@app.get("/health", status_code=HTTPStatus.OK)
async def health():
    return {"status": "health_check"}, HTTPStatus.OK
