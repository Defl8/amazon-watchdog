import sqlite3
from sqlite3 import Connection, Cursor


def connect_to_db(db_name: str) -> Connection:
    return sqlite3.connect(db_name)


def make_table(table_name: str, db_name: str, *args: str):
    column_names: tuple[str, ...] = args
    connection: Connection = connect_to_db(db_name)
    cursor: Cursor = connection.cursor()
    column_string: str = ", ".join(column_names)
    _ = cursor.execute(f"CREATE TABLE {table_name}({column_string})")


def check_if_exists_table(table_name: str, db_name: str) -> bool:
    connection: Connection = connect_to_db(db_name) 
    cursor: Cursor = connection.cursor()
    table_list: Cursor = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return table_name in table_list.fetchall()
