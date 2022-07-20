from .Database import Database

class SGBDConfig: 
    def __init__(self, path: str) -> None:
        self.path = path

defaulConfig = SGBDConfig(
    path='./YourSGBD'
)

class SGBD:

    def __init__(self, config: SGBDConfig = defaulConfig) -> None:
        self.databases = []
        self.config = config

    def create_database(self, name: str) -> Database: 
        new_database = Database(
            name=name, 
            path=self.config.path
        )

        new_database.persist()

        self.databases.append(new_database)

        return new_database

    def get_databases(self) -> list:

        return self.databases

    def get_databases_names(self) -> list:

        def get_name(database: Database) -> str:
            return database.get_name()

        return list(map(get_name, self.get_databases()))
