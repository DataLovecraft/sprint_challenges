'''
###############################
Part 2 - The Northwind Database
###############################
'''
import sqlite3
CONN = sqlite3.connect('northwind_small_plural.sqlite3')


def run_queries():
    """Run and print output from queries for sprint challenge questions."""
    # Part 2
    expensive_items = 'SELECT * FROM Products ORDER BY UnitPrice DESC LIMIT 10;'
    avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM Employees;'
    age_by_city = ('SELECT City, AVG(HireDate - BirthDate) FROM Employees '
                   'GROUP BY City;')
    # Part 3
    item_suppliers = ('SELECT p.ProductName, p.UnitPrice, s.CompanyName '
                      'FROM Products p, Suppliers s WHERE p.SupplierId = s.Id '
                      'ORDER BY p.UnitPrice DESC LIMIT 10;')
    largest_category = ('SELECT c.CategoryName, COUNT(DISTINCT p.Id) '
                        'FROM Category c, Product p WHERE c.Id = p.CategoryId '
                        'GROUP BY 1 ORDER BY 2 DESC LIMIT 1;')
    employee = ('SELECT e.Id, e.FirstName, e.LastName, COUNT(DISTINCT t.Id) '
                'FROM Territory t, Employees e, EmployeeTerritory et '
                'WHERE e.Id = et.EmployeeId AND t.id = et.TerritoryId '
                'GROUP BY 1, 2, 3 ORDER BY 4 DESC LIMIT 1;')
    # Get and print results
    queries = (expensive_items, avg_hire_age, age_by_city, item_suppliers,
               largest_category, employee)
    curs = CONN.cursor()
    for query in queries:
        print(curs.execute(query).fetchall())

if __name__ == "__main__":
    run_queries()

'''
OUTPUT:
What are the ten most expensive items (per unit price) in the database?
(38, 'Côte de Blaye', 263.5)
(29, 'Thüringer Rostbratwurst', 123.79)
(9, 'Mishi Kobe Niku', 97)
(20, "Sir Rodney's Marmalade", 81)
(18, 'Carnarvon Tigers', 62.5)
(59, 'Raclette Courdavault', 55)
(51, 'Manjimup Dried Apples', 53)
(62, 'Tarte au sucre', 49.3)
(43, 'Ipoh Coffee', 46)
(28, 'Rössle Sauerkraut', 45.6)
================================================================================
What is the average age of an employee at the time of their hiring?
[(37.28344360787892,)]
================================================================================
How does the average age of employee at hire vary by city?
('Kirkland', 28.588637919233403)
('London', 32.82819986310746)
('Redmond', 55.619438740588635)
('Seattle', 39.77275838466804)
('Tacoma', 40.48459958932238)
================================================================================
What are the ten most expensive items (per unit price) in the database and their suppliers?
(18, 'Aux joyeux ecclésiastiques', 38, 'Côte de Blaye', 263.5)
(12, 'Plutzer Lebensmittelgroßmärkte AG', 29, 'Thüringer Rostbratwurst', 123.79)
(4, 'Tokyo Traders', 9, 'Mishi Kobe Niku', 97)
(8, 'Specialty Biscuits, Ltd.', 20, "Sir Rodney's Marmalade", 81)
(7, 'Pavlova, Ltd.', 18, 'Carnarvon Tigers', 62.5)
(28, 'Gai pâturage', 59, 'Raclette Courdavault', 55)
(24, "G'day, Mate", 51, 'Manjimup Dried Apples', 53)
(29, "Forêts d'érables", 62, 'Tarte au sucre', 49.3)
(20, 'Leka Trading', 43, 'Ipoh Coffee', 46)
(12, 'Plutzer Lebensmittelgroßmärkte AG', 28, 'Rössle Sauerkraut', 45.6)
================================================================================
What is the largest category (by number of unique products in it)?
[(3, 'Confections', 13)]
================================================================================
Who's the employee with the most territories?
[(7, 'Sales Representative', 'Robert', 'King', 10)]
'''
