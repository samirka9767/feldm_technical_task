

To be able to run the project install python >= 3.5 on your machine.

The task contains 5 subtasks. There is a separate function for each task has been created. 
For 1st 4 tasks, functions have been created in the tasks.py file, and the 5th tasks is implemented in choose_db.py file. 

In main.py file, all 5 functions have been called. 

For task #3 - When running store_data_into_file function, all_transactions.txt file will be created in the current project folder, as it was required in the Task #3. 


As it was required in Task #4, the curency conversion will happen to all the transactions from Transactions table. For transactions which happened at a certain time which is not in eurofxref-hist-90d.xml file, there is a default rate, equal to 0.88 (which is today's euro-to-usd currency) and the convertion happens based on that rate. 




The following command will run all tasks at the same time and will print accordingly: (Run the command in the project folder)

python3 main.py

Run tests in /tests folder:

    python3 -m unittest tests/tes