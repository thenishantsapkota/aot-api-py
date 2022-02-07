from sqlmodel import Field, SQLModel
import typing as t

class Quotes(SQLModel, table=True):
    id: t.Optional[int] = Field(default=None, primary_key=True)
    quote: str