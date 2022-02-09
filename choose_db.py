import sqlite3
import psycopg2
import configparser


#Task 5 - Support Postgres db

def connect_to_db(db_type):
    if db_type == 'postgres':
        config = configparser.ConfigParser()
        config.read('db/db.ini')
        config = config['postgresql']
        return psycopg2.connect(database=config["database"], user=config["user"], password=config["password"],
                                host=config["host"], port=config["port"])
    elif db_type == 'sqlite':
        connection = sqlite3.connect('db/transactions.db')
        return connection