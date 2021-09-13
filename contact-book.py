import sqlite3


def init(db):
    global connection
    global cursor
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    create_table()


# Function to create a database table for storing contacts
def create_table():
    # SQL command to create a table in the database
    sql_command = '''CREATE TABLE IF NOT EXISTS contacts
         (number INT PRIMARY KEY     NOT NULL,
         fname           VARCHAR(20)    NOT NULL,
         lname         VARCHAR(10));'''
    cursor.execute(sql_command)
    connection.commit()


# Function to insert contact details into database
def insert_values(number, fname, lname):
    # SQL command to insert the data in the table
    sql_command = '''INSERT INTO contacts (number, fname, lname) VALUES (?,?,?);'''
    # tuple to insert at placeholder
    tuple = (number, fname, lname)
    cursor.execute(sql_command, tuple)
    connection.commit()


# Function to display values
def display_values():
    # SQL command to insert the data in the table
    sql_command = '''SELECT * FROM contacts;'''
    cursor.execute(sql_command)
    records = cursor.fetchall()
    print("Printing list of Contacts: \n")
    for row in records:
        print("Mobile Number: ", row[0])
        print("First Name: ", row[1])
        print("Last Name: ", row[2])
        print("\n")
    connection.commit()


# Function to clear database
def clear_database():
    print("Erasing database... \n")
    sql_command = '''drop table contacts;'''
    cursor.execute(sql_command)
    connection.commit()


init("contacts.db")
number = int(input("Enter Mobile Number: "))
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
insert_values(number, fname, lname)
display_values()
clear_database() # call this function to clear database
connection.close()
