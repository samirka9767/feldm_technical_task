from choose_db import connect_to_db
from tasks import find_max_revenue, max_revenue_mobile


conn = connect_to_db('', 'sqlite')
cursor = conn.cursor()



def main():
    #Task 1
    print(find_max_revenue(cursor))

    #Task 2
    print(max_revenue_mobile(cursor))





if __name__ == "__main__":
    main()