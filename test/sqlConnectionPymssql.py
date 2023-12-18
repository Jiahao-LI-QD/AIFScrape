import pymssql
conn = pymssql.connect(host=r'localhost:port', user=r'sa', password=r'password', database=r'test1')
cur = conn.cursor()
cur.execute(r'SELECT * FROM newtable')
row = cur.fetchone()
print(row)
cur.close()
conn.close()