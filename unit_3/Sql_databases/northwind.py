'''
###############################
Part 2 - The Northwind Database
###############################
'''
import sqlite3
# Create connection to `northwind.sqlite3` database
CONN = sqlite3.connect('northwind_small.sqlite3')

### THERE ARE MANY WAYS OF DOING THIS:

def run_queries():
    """Run and print output from queries"""
    # Part 2
    # What are the ten most expensive items (per unit price) in the database?
    expensive_items = 'SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
    # What is the average age of an employee at the time of their hiring?
    avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'
    # How does the average age of employee at hire vary by city?
    age_by_city = ('SELECT City, AVG(HireDate - BirthDate) FROM Employee '
                   'GROUP BY City;')

    # Part 3
    # THERE ARE MANY WAYS OF DOING THIS:

    # What are the ten most expensive items (per unit price) in the database *and*
    # their suppliers?

    # METHOD 1
    # item_suppliers = ('SELECT p.ProductName, p.UnitPrice, s.CompanyName '
    #                  'FROM Products p, Suppliers s WHERE p.SupplierId = s.Id '
    #                  'ORDER BY p.UnitPrice DESC LIMIT 10;')

    # METHOD 2
    item_suppliers = ("""SELECT ProductName, UnitPrice, CompanyName
                          FROM Product
                          JOIN Supplier
                          ON Product.SupplierId = Supplier.Id
                          ORDER BY UnitPrice DESC
                          LIMIT 10;""")

    # What is the largest category (by number of unique products in it)?

    # METHOD 1
    #largest_category = ('SELECT c.CategoryName, COUNT(DISTINCT p.Id) '
    #                    'FROM Category c, Product p WHERE c.Id = p.CategoryId '
    #                    'GROUP BY 1 ORDER BY 2 DESC LIMIT 1;')

    # METHOD 2
    largest_category = ( """SELECT CategoryName, COUNT(DISTINCT ProductName) AS Count
                            FROM Category
                            JOIN Product
                            ON Category.Id = Product.CategoryId
                            GROUP BY CategoryName
                            ORDER BY Count DESC
                            LIMIT 1;""")

    # Who's the employee with the most territories?

    # METHOD 1
    #employee = ('SELECT e.Id, e.FirstName, e.LastName, COUNT(DISTINCT t.Id) '
    #            'FROM Territory t, Employee e, EmployeeTerritory et '
    #            'WHERE e.Id = et.EmployeeId AND t.id = et.TerritoryId '
    #            'GROUP BY 1, 2, 3 ORDER BY 4 DESC LIMIT 1;')

    # METHOD 2

    employee =  ("""SELECT E.FirstName, E.LastName, COUNT(ET.TerritoryId) AS TerritoryCount 
                    FROM Employee AS E
                    JOIN EmployeeTerritory AS ET
                    ON E.Id = ET.EmployeeId
                    GROUP BY E.Id
                    ORDER BY TerritoryCount DESC
                    LIMIT 1;""")
    # Get and print results
    queries = (expensive_items, avg_hire_age, age_by_city, item_suppliers,
               largest_category, employee)
    curs = CONN.cursor()
    for query in queries:
        print(curs.execute(query).fetchall())

if __name__ == "__main__":
    run_queries()



"""
WARNING!!!
TABLE NAMES ARE SINGULAR NOT PLURAL!!!!

"""

# OUTPUT:
"""
[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0), (29, 'Thüringer Rostbratwurst', 12, 6, '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1), (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1), (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0), (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0), (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0), (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0), (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0), (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0), (28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]
[(37.22222222222222,)]
[('Kirkland', 29.0), ('London', 32.5), ('Redmond', 56.0), ('Seattle', 40.0), ('Tacoma', 40.0)]
[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), ('Mishi Kobe Niku', 97, 'Tokyo Traders'), ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), ('Raclette Courdavault', 55, 'Gai pâturage'), ('Manjimup Dried Apples', 53, "G'day, Mate"), ('Tarte au sucre', 49.3, "Forêts d'érables"), ('Ipoh Coffee', 46, 'Leka Trading'), ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
[('Confections', 13)]
[(7, 'Robert', 'King', 10)]
"""
