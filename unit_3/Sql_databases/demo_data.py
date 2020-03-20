'''
#########################################
Part 1 - Making and populating a Database
#########################################
'''
import sqlite3


# Open a connection to a new (blank) database file demo_data.sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
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
    curs = conn.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS demo (s char(1), x int, y int);')
    for i in DATA:
        curs.execute('INSERT INTO demo (s, x, y) VALUES ' + str(i))
    curs.close()
    conn.commit()

'''
WARNING! `CREATE TABLE IF NOT EXISTS` APPENDS TO THE SAME DATABASE
THUS DUPLICATING YOUR RESULTS:
How many rows are there are?
[(6,)]
How many rows are there where both x and y are at least 5?
[(4,)]
How many unique values of y are there
[(2,)]

- delete `demo_data.sqlite3` to get correct results if running your script again
'''

# - Count how many rows you have - it should be 3!
# - How many rows are there where both x and y are at least 5?
# - How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
def run_queries():
    curs = conn.cursor()
    print("How many rows are there are?")
    print(curs.execute('SELECT COUNT(*) FROM demo;').fetchall())
    print("How many rows are there where both x and y are at least 5?")
    print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5;').fetchall())
    print("How many unique values of y are there ")
    print(curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall())

'''
How many rows are there are?
[(3,)]
How many rows are there where both x and y are at least 5?
[(2,)]
How many unique values of y are there
[(2,)]
'''

if __name__ == "__main__":
    make_db()
    run_queries()
