from sqlmodel import create_engine, SQLModel

from aot_quotes.common.db.quotes import Quotes

engine = create_engine("sqlite:///database.db", echo=True)

def migrate():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    migrate()

__all__ = ["Quotes"]