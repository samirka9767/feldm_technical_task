from utilities.write_into_file import write_into_file
from utilities.parse_available_currencies import find_usd_rate


# Task 1
# Write a Python script to find out which visitor created the most revenue.
# Note: a simple print of the result to the console is sufficient

def find_max_revenue(cursor):
    cursor.execute("SELECT id FROM Transactions ORDER BY revenue DESC")
    return cursor.fetchone()[0]


# Task 2
# Write a Python script to find out on which day most revenue for users who ordered via a mobile phone was created.
# Note: a simple print of the result to the console is sufficient

def find_max_revenue_mobile(cursor):
    cursor.execute("SELECT datetime FROM Transactions WHERE device_type=3 ORDER BY revenue DESC")
    return cursor.fetchone()[0]


# Task 3
# Write a Python script that combines the contents of Devices and Transactions
# and store it as a single flat file including the column names.

def store_data_into_file(cursor):
    query = cursor.execute(
        "SELECT T.id AS ID, T.visitor_id AS VISITORID, T.revenue AS REVENUE, strftime('%Y-%m-%d',T.datetime) AS DATE, "
        "T.tax as TAX, D.device_name AS DEVICE "
        "FROM Transactions AS T INNER JOIN Devices AS D")
    names = list(map(lambda x: x[0], query.description))
    all_records = cursor.fetchall()
    write_into_file(all_records, names)
    return "All Transactions along with devices are writen into a file"


# Task 4
# As stated in the SQL comments the created revenue is currently stored in USD.
# Update the data stored in the database to have the created revenue in EUR.
def convert_revenue_to_euro(cursor, rate=0.88):
    cursor.execute("SELECT * FROM Transactions")
    transactions = cursor.fetchall()
    for transaction in transactions:
        id = transaction[0]
        revenue = transaction[4]
        date = transaction[1].split()[0]
        current_rate = find_usd_rate(date)
        if current_rate != -1:
            revenue = revenue / float(current_rate)
        else:
            revenue = revenue / float(rate)
        data = (revenue, id)
        cursor.execute("""Update Transactions set revenue = ?  where id = ?""", data)
    return "Converted revenue values into EU"

