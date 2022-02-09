import unittest
from choose_db import connect_to_db
# from tasks import
from tasks import find_max_revenue, max_revenue_mobile

conn = connect_to_db('', 'sqlite')
cursor = conn.cursor()


class TestTasks(unittest.TestCase):

    def test_find_max_revenue(self):
        actual_value = find_max_revenue(cursor)
        expected_value = cursor.execute("select id from (SELECT id, max(revenue) FROM Transactions)").fetchone()[0]
        assert actual_value == expected_value

    def test_max_revenue_mobile(self):
        actual_value = max_revenue_mobile(cursor)
        expected_value = cursor.execute("SELECT datetime, max(revenue) FROM Transactions WHERE device_type=3").fetchone()[0]
        assert actual_value == expected_value


