# SQL Injection - Good Example
# ------------------------------------------------------------------------------
# Parameterized queries separate data from code, preventing SQL injection.
# Use parameter placeholders and pass parameters as a tuple.

import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT)')

username = input('Enter username to lookup: ')

# GOOD: query uses ? placeholders and parameters tuple
query = 'SELECT * FROM users WHERE username = ?'
print('Executing:', query, 'with params', username)
for row in cursor.execute(query, (username,)):
    print(row)
