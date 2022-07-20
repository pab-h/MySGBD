from .Database import Database

class SGBD:

    def __init__(self) -> None:
        
        self.databases = []

    def create_database(self, name: str) -> Database: 
        new_database = Database(name=name)

        self.databases.append(new_database)

        return new_database

    def get_databases(self) -> list:

        return self.databases