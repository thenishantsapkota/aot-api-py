from aot_quotes.core.quote.service import GetService
from aot_quotes.mixins.database import DBMixin
from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class GetCBV(DBMixin):
    get_service: GetService = Depends(GetService)

    @router.get("/")
    def random(self):
        result = self.get_service.get_quote(self.session, self.engine)
        return {"quote": result}

    @router.get("/{query}")
    def random_list(self, query: int):
        if query < 1:
            raise HTTPException(status_code=404, detail="Heh? Why?")
        result = self.get_service.get_random_quotes(query, self.session, self.engine)
        return result
