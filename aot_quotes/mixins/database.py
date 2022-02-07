from starlette.requests import Request
from sqlmodel import Session
from aot_quotes.common.db import engine

class DBMixin:
    def __init__(self, request: Request) -> None:
        self.request = request
        self.session = Session
        self.engine = engine