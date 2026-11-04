# SQL Injection Attack Demonstration

import sqlite3

# Step 1: Create Database
con = sqlite3.connect(":memory:")
cur = con.cursor()

# Step 2: Create Table
cur.execute("CREATE TABLE users (username TEXT, password TEXT)")

cur.execute("INSERT INTO users VALUES ('admin', '1234')")
cur.execute("INSERT INTO users VALUES ('user', 'abcd')")

print("Database Created Successfully!")

# Step 3: Accept User Input
username = input("\nEnter Username: ")
password = input("Enter Password: ")

# Step 4: Vulnerable SQL Query
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

print("\nGenerated SQL Query:")
print(query)

# Step 5: Execute Query
try:
    cur.execute(query)
    result = cur.fetchone()

    if result:
        print("\nLogin Successful!")
        print("Welcome:", result[0])
    else:
        print("\nInvalid Username or Password!")

except sqlite3.Error as e:
    print("SQL Error:", e)

# Step 6: Secure Login using Parameterized Query
print("\n--- Secure Login ---")

username = input("Enter Username: ")
password = input("Enter Password: ")

cur.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, password)
)

result = cur.fetchone()

if result:
    print("Secure Login Successful!")
else:
    print("Secure Login Failed!")

con.close()