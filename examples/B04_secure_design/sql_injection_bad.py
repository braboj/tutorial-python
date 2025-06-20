# SQL Injection - Bad Example
# ------------------------------------------------------------------------------
# Directly formatting user input into an SQL query can allow injection attacks.
# NEVER build queries using string concatenation with untrusted data.

import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT)')

username = input('Enter username to lookup: ')

# BAD: user input is concatenated directly into the query
query = f"SELECT * FROM users WHERE username = '{username}'"
print('Executing:', query)
for row in cursor.execute(query):
    print(row)
