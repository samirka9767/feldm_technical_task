

To be able to run the project install python >= 3.5 on your machine.

The task contains 5 subtasks. For each task there is a separate function created. 

For 1st 4 tasks, functions have been created in the tasks.py file, and the 5th tasks is implemented in choose_db.py file. 

In main.py file, all 5 functions have been called. 

For task #3 - When running store_data_into_file function, all_transactions.txt file will be created in the current project folder, as it was required in the Task #3. 


As it was required in Task #4, the curency conversion will happen to all the transactions from Transactions table. For transactions which happened at a certain time which is not in eurofxref-hist-90d.xml file, there is a default rate, equal to 0.88 (which is today's euro-to-usd currency) and the convertion happens based on that rate. 


For Task #5

sqlite is built-in python, for this you just need to import sqlite

For postgres support follow below:


Run the following comman in your cli:

pip3 install psycopg2 

OR

Download postgres app from here: https://postgresapp.com/downloads.html
Follow the installation stesp specified in the link. 


Check out your default settings for the following values:

host = hostname
user = username
passwd = yourpassword
database = yourdatabase
port: 5432

Change those values in config/db.ini file, set according to your own credentials


Note: choose_db.py function when called with postgres argument e.g connect_to_db('postgres') will return the connection to postgres db, but I did not import transactions.db into postgres to run the queries and see if it works. In my project I can locally connect to postgres db and I assume this is what was expected from the Task #5. 


RUN THE PROJECT:

The following command will run all tasks at the same time and will print accordingly: (Run the command in the project folder)

python3 main.py

I have implemented 3 test cases for 1st 3 tasks:

Run tests in /tests folder:

    python3 -m unittest tests/tes