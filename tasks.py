

# Task 1
# Write a Python script to find out which visitor created the most revenue.
# Note: a simple print of the result to the console is sufficient

def find_max_revenue(cursor):
    cursor.execute("SELECT id FROM Transactions ORDER BY revenue DESC")
    return cursor.fetchone()[0]