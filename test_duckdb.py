# import sys
# sys.path.append('c:\\users\\timmer\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\\localcache\\local-packages\\python310\\site-packages')

pip install duckdb

import duckdb
cursor = duckdb.connect()
print(cursor.execute('SELECT 42').fetchall())

print(cursor.execute('INSTALL httpfs').fetchall())
