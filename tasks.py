

# Task 1
# Write a Python script to find out which visitor created the most revenue.
# Note: a simple print of the result to the console is sufficient

def find_max_revenue(cursor):
    cursor.execute("SELECT id FROM Transactions ORDER BY revenue DESC")
    return cursor.fetchone()[0]


# Task 2
# Write a Python script to find out on which day most revenue for users who ordered via a mobile phone was created.
# Note: a simple print of the result to the console is sufficient

def max_revenue_mobile(cursor):
    cursor.execute("SELECT datetime FROM Transactions WHERE device_type=3 ORDER BY revenue DESC")
    return cursor.fetchone()[0]