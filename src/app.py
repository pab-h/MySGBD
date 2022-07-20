from classes.Database import Database
from classes.SGBD import SGBD

sgbd = SGBD()

sgbd.create_database("Database 1")
sgbd.create_database("Database 1")

print(sgbd.get_databases_names())

