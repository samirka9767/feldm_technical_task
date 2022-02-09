from choose_db import connect_to_db
from tasks import find_max_revenue


conn = connect_to_db('', 'sqlite')
cursor = conn.cursor()



def main():
    #Task 1
    print(find_max_revenue(cursor))





if __name__ == "__main__":
    main()