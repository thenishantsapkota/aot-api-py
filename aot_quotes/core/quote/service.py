import random
import typing as t
from email.quoprimime import quote

from aot_quotes.common.db import Quotes
from sqlmodel import Session, select


class GetService:
    def get_quote(self, session: t.Type[Session], engine) -> t.Optional[dict]:
        with session(engine) as s:
            statement = select(Quotes)
            result = s.execute(statement).fetchall()

            if result:
                quote_obj = random.choice(result)
                return (quote_obj[0]).quote

    def get_random_quotes(
        self, query: int, session: t.Type[Session], engine
    ) -> t.Optional[dict]:
        with session(engine) as s:
            statement = select(Quotes)
            result = s.execute(statement).fetchall()

            if result:
                data = list()
                items = random.sample(result, query)
                for item in items:
                    data.append({"id": item[0].id, "quote": item[0].quote})
                return data
