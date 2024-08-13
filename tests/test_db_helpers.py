from sqlite3.dbapi2 import connect
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
import sqlite3
import os

from watchdog.db.db import make_table, check_if_exists_table

class TestDBHelpers(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        connection = sqlite3.connect("test.db")
        connection.close()

    def setUp(self) -> None:
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
        _ = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='test'")
        tables = cursor.fetchall()
        if "test" in list(map(lambda x: x[0], tables)):
            _ = cursor.execute("DROP TABLE test;")
        connection.close()

    @classmethod
    def tearDownClass(cls) -> None:
        if "test.db" in os.listdir():
            os.remove("test.db")


    def test_create_table(self):
        db_name: str = "test.db"
        table_name: str = "test"
        make_table(table_name, db_name, "col1", "col2")

        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        _ = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        table_exists = cursor.fetchone()
        connection.close()

        self.assertIsNotNone(table_exists, msg="Table was not found in db")


    def test_check_if_table_exists(self):
        db_name: str = "test.db"
        table_name: str = "test"
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        _ = cursor.execute(f"CREATE TABLE {table_name}(col1, col2, col3)")
        connection.close()

        table_exists_true: bool = check_if_exists_table(table_name, db_name)
        table_exists_false: bool = check_if_exists_table("fake", db_name)

        self.assertTrue(table_exists_true, "Function did not return True, existence of table cannot be confirmed")
        self.assertFalse(table_exists_false, "Function did not return False, state of table cannot be confirmed")


if __name__ == "__main__":
    _ = unittest.main()
