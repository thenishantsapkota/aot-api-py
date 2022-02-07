from fastapi import FastAPI

from aot_quotes.core.quote.views import router as get

app = FastAPI(
    title="Attack on Titan - Quotes API", docs_url="/", redoc_url=None, version="2.0.0"
)

app.include_router(get, prefix="/v2/random")
