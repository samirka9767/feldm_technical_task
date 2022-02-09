from choose_db import connect_to_db
from tasks import find_max_revenue, find_max_revenue_mobile, store_data_into_file, convert_revenue_to_euro



def main():

    #Connect to db
    conn = connect_to_db('sqlite')
    cursor = conn.cursor()

    #Task 1
    print(find_max_revenue(cursor))

    #Task 2
    print(find_max_revenue_mobile(cursor))

    #Task 3
    print(store_data_into_file(cursor))

    # Task #4
    print(convert_revenue_to_euro(cursor, 0.88))

    #Commit and close the connection
    conn.commit()
    conn.close()






if __name__ == "__main__":
    main()