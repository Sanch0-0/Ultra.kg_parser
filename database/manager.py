from sqlalchemy import Engine, Row, exc, text
from .connection import engine, TABLES

class TablesManager:
    engine: Engine = engine

    @classmethod
    def create_tables(cls: "TablesManager", *args, **kwargs) -> None:

        with cls.engine.connect() as connection:
            for table, request in TABLES.items():

                try:
                    connection.execute(text(request))
                    connection.commit()
                except exc.OperationalError:
                    request_ = request.split()
                    request_.insert(2, "IF NOT EXISTS")
                    request = " ".join(request_)
                    print(f"""Table {table} already exist! Change yoyr request \n{request}\n""")


class Manager(TablesManager):


    @classmethod
    def select_many(cls: "Manager", request: str, *args, **kwargs) -> list[Row]:

        with cls.engine.connect() as connection:
            response = connection.execute(text(request))

        return response.all()


    @classmethod
    def select_one(cls: "Manager", request: str, *args, **kwargs) -> Row | None:

        with cls.engine.connect() as connection:
            response = connection.execute(text(request))

        try:
            return response.one()
        except exc.NoResultFound:
            return None


    @classmethod
    def insert(cls: "Manager", request: str, check_unique: bool = False, *args, **kwargs) -> None:

        with cls.engine.connect() as connection:
            if check_unique:
                try:
                    connection.execute(text(request))
                    connection.commit()
                except exc.IntegrityError as error:
                    print("Dublicate")
            else:
                connection.execute(text(request))
                connection.commit()

    @classmethod
    def update(cls: "Manager", request: str, *args, **kwargs) -> None:

        with cls.engine.connect() as connection:
            connection.execute(text(request))
            connection.commit()


    @classmethod
    def delete(cls: "Manager", request: str, *args, **kwargs) -> None:

        with cls.engine.connect() as connection:
            connection.execute(text(request))
            connection.commit()
