import sqlite3
import psycopg2

#Task 5 - Support Postgres db

def connect_to_db(config, db_type):
    #Assuming config is a dictionary with access credentials as such
    # config = {
    #     "database": "mydb",
    #     "user": "postgres",
    #     "password": "",
    #     "host": "127.0.0.1",
    #     "port": "5432"
    # }
    if db_type == 'postgres':
        return psycopg2.connect(database=config["database"], user=config["user"], password=config["password"], host=config["host"], port=config["port"])
    elif db_type == 'sqlite':
        connection = sqlite3.connect('db/transactions.db')
        return connection