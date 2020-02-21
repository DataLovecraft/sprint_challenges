# Part 1

import sqlite3


# Open a connection to a new (blank) database file demo_data.sqlite3
CONN = sqlite3.connect('demo_data.sqlite3')
DATA = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

# - Make a cursor, and execute an appropriate CREATE TABLE statement to accept
#   the above data (name the table demo)
#
# - Write and execute appropriate INSERT INTO statements to add the data
#   (as shown above) to the database
def make_db():
    curs = CONN.cursor()
    curs.execute('CREATE TABLE demo (s char(1), x int, y int);')
    for datum in DATA:
        curs.execute('INSERT INTO demo (s, x, y) VALUES ' + str(datum))
    curs.close()
    CONN.commit()


# - Count how many rows you have - it should be 3!
# - How many rows are there where both x and y are at least 5?
# - How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
def run_queries():
    curs = CONN.cursor()
    print(curs.execute('SELECT COUNT(*) FROM demo;').fetchall())
    print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5;').fetchall())
    print(curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall())

if __name__ == "__main__":
    make_db()
    run_queries

'''
OUTPUT:
Count how many rows you have
There are 3 rows in the table.
================================================================================
How many rows are there where both x and y are at least 5?
There are 2 rows where both x and y are at least 5.
================================================================================
How many unique values of y are there?
There are 2 unique values of y.
================================================================================
'''
