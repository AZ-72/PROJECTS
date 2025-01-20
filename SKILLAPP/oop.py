#                                       DATABASES
# - connect
# - execute
# - close
# - cursor => all operation in sql dne by cursor not the connection itself
# - commit => save alle changes
# - fetchone => returns a single record or none if no more rows are available
# - fetchall => fetches all the rows of a query result it returns all the rows
#               as a list of tuples an empty list is returned if there is no record to fetch
# - fetchmany(size)=> to fetch a number of rows that you choose
#-----------------------------------------------------------------------------------

#import sqlite3 module

import sqlite3

# Connect to the database (or create it if it doesn't exist)
db = sqlite3.connect("app.db")
cr = db.cursor()

# Creating tables and fields
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Inserting data into the users table
#cr.execute("INSERT INTO users (user_id, name) VALUES (1, 'ahmed')")
#cr.execute("INSERT INTO users (user_id, name) VALUES (2, 'ali')")
#cr.execute("INSERT INTO users (user_id, name) VALUES (3, 'mohammed')")
my_list = ["AHMED","sayed","mahmoud","ali","kamal","kamel","sameh","enas"]


for key ,user in enumerate (my_list) :
    cr.execute(f"INSERT INTO users (user_id, name) VALUES ({key + 1}, '{user}' ) ")


#updating data replacing names
cr.execute("UPDATE users SET name = 'marmosh' WHERE user_id = 8")

#deletong data

#cr.execute("DELETE from users where user_id =number ")



#                     FETCH                              DATA

cr.execute("select * from users")
print(cr.fetchall())


# Save (commit) changes
db.commit()

# Closing the database
db.close()


# ------------------------------------------------------------------------------------
#                              training on evrything
#import sqlite3
#
#
#def get_all_data():
#    try:
#        # connect to database
#        db = sqlite3.connect("app.db")
#
#        print("connected to database ")
#
#
#        #setting up the cursor
#        cr = db.cursor()
#
#        #fetch data from database
#        cr.execute("select * from users")
#
#
#        # assign data to variable
#        results = cr.fetchall()
#
#        #print number of rows
#        print(f"Database Has {len(results)} ==> Rows")
#        #loop on results
#        #printingmessage
#        print("showing data ....||||")
#        for row in results:
#            print(f"UserID => {row[0]}  |  ", end=" ")
#            print(f"Username => {row[1]}")
#
#
#
#
#    except sqlite3.Error as er:
#        print(f"error Reading Data {er}")
#
#    finally:
#        if (db):
#
#            #Close Database connection
#            db.close()
#
#            print("connection to database is closed  ||||.....  /")
#
#
#get_all_data()

#test git hub





