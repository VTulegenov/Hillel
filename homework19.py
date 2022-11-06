import os
import sqlite3


db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

invoice_items = '''
    SELECT UnitPrice, Quantity
        FROM invoice_items;
'''
result = cur.execute(invoice_items).fetchall()
b = 0
for i,j in result:
    result[b] = i*j
    b += 1
print(sum(result))


customers = '''
    SELECT DISTINCT FirstName
        FROM customers;
'''
result_2 = cur.execute(customers).fetchall()
first_mane = set()

for sadf in result_2:
    first_mane.add(sadf[0])

print(f'all names quantity: {len(result_2)}, unique names quantity: {len(first_mane)}')
print(*first_mane)


connection.close()
