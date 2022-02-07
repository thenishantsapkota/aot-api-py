from sqlmodel import Session
from starlette.requests import Request

from aot_quotes.common.db import engine


class DBMixin:
    def __init__(self, request: Request) -> None:
        self.request = request
        self.session = Session
        self.engine = engine
