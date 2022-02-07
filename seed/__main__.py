from sqlmodel import Session

from aot_quotes.common.db import Quotes, engine


def seed_data(filename):
    with Session(engine) as session:
        with open(filename, "r") as fp:
            for line in fp.readlines():
                quote_obj = Quotes(quote=line.strip())
                session.add(quote_obj)
            session.commit()


if __name__ == "__main__":
    seed_data("./seed/data.txt")
