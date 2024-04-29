import mysql.connector

try:
    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(host='localhost' , password='Naani@123' , user='root',database='project')

    if conn.is_connected():
        print('Connected to MySQL database')

#TRANSACTION1

    # Start a transaction
    conn.start_transaction(isolation_level='READ COMMITTED')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        
        

        # Update 'product' table
        update_query1 = "UPDATE product SET prod_id = 'pp1' WHERE prod_id = 'p1'"
        cursor.execute(update_query1)
        print("prodid updated in 'product' and 'stock' table")
        
        # Commit the transaction
        conn.commit()
        print("Transaction1 committed successfully")

    except mysql.connector.Error as e:
        print(f'Error executing SQL query: {e}')
        # Rollback the transaction in case of error
        conn.rollback()
        print("Transaction1 rolled back")
#TRANSACTION1 ENDED

#TRANSACTION2
# Start a transaction
    conn.start_transaction(isolation_level='READ COMMITTED')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        
      

        # Update 'depot' table
        update_query2 = "UPDATE depot SET dep_id = 'dd1' WHERE dep_id = 'd1'"
        cursor.execute(update_query2)
        print("depid updated in 'depot' and 'stock' table")

    
        # Commit the transaction
        conn.commit()
        print("Transaction2 committed successfully")

    except mysql.connector.Error as e:
        print(f'Error executing SQL query: {e}')
        # Rollback the transaction in case of error
        conn.rollback()
        print("Transaction2 rolled back")
#TRANSACTION2 ENDED


except mysql.connector.Error as e:
    print(f'Error connecting to MySQL: {e}')

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print('MySQL connection closed')
