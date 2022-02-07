import random
import typing as t

from aot_quotes.common.db import Quotes
from sqlmodel import Session, select

class GetService:
    def get_quote(self, session: t.Type[Session], engine) -> t.Optional[dict]:
        with session(engine) as s:
            statement = select(Quotes)
            result = s.execute(statement).fetchall()

            if result:
                return random.choice(result)