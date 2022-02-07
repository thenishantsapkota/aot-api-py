from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from aot_quotes.core.quote.service import GetService
from aot_quotes.mixins.database import DBMixin

router = InferringRouter()


@cbv(router)
class GetCBV(DBMixin):
    get_service: GetService = Depends(GetService)

    @router.get("/")
    def random(self):
        result = self.get_service.get_quote(self.session, self.engine)
        return result
