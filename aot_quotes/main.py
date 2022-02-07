from fastapi import FastAPI

from aot_quotes.core.quote.views import router as get
from starlette.responses import RedirectResponse

app = FastAPI(title="Attack on Titan - Quotes API")

app.include_router(get, prefix="/random")

@app.get("/")
async def redirect():
    return RedirectResponse(url="/docs")