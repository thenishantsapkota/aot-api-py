import typing as t

from sqlmodel import Field, SQLModel


class Quotes(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    quote: str
