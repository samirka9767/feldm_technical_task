import unittest
from choose_db import connect_to_db
import os
from tasks import find_max_revenue, find_max_revenue_mobile

conn = connect_to_db('sqlite')
cursor = conn.cursor()


class TestTasks(unittest.TestCase):

    def test_find_max_revenue(self):
        actual_value = find_max_revenue(cursor)
        expected_value = cursor.execute("select id from (SELECT id, max(revenue) FROM Transactions)").fetchone()[0]
        assert actual_value == expected_value

    def test_find_max_revenue_mobile(self):
        actual_value = find_max_revenue_mobile(cursor)
        expected_value = cursor.execute("SELECT datetime, max(revenue) FROM Transactions WHERE device_type=3").fetchone()[0]
        assert actual_value == expected_value

    def test_store_data_into_file(self):
        is_created = os.path.isfile('./all_transactions.txt')
        assert is_created


