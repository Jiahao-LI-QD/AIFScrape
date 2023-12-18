from dbutilities import connection
import pyodbc

selectAll = r"select * from newtable"
insertion = r"insert into newtable values (?, ?)"
deleteGreater2 = r"delete from newtable where id > 2"

#with open("dbutilities\dbProperties.properties") as f:
#db = connection.connect_db()

# Connect MSSQL database with windows authentication
cnxn = pyodbc.connect(r'Driver=SQL Server;'
                      r'Server=.\AIF;'
                      r'Database=test1;'
                      r'Trusted_Connection=yes;')
cursor = cnxn.cursor()

print("clean database for testing: deleting id > 2")
cursor.execute(deleteGreater2)
cursor.commit()
print(cursor.rowcount, cursor.messages)

def checkAllInNewTable(c):
    c.execute(selectAll)
    while 1:
        row = c.fetchone()
        if not row:
            break
        print(row)

print("")
print("check rows in newTable")
checkAllInNewTable(cursor)

value = (3, "info 3")
values = [(4, "info 4"), (5, "info 5")]

print("")
print("insert one row into newTable")

cursor.execute(insertion, value)
cursor.commit()
print(cursor.rowcount, cursor.description, cursor.messages)


print("")
print("insert multiple rows into newTable")
cursor.executemany(insertion, values)
cursor.commit()

checkAllInNewTable(cursor)

# If autocommit is true <-- be careful <-- handle them one by one
# try:
#     cnxn.autocommit = False
#     params = [ ('A', 1), ('B', 2) ]
#     cursor.executemany("insert into newtable values (?, ?)", params)
# except pyodbc.DatabaseError as err:
#     cnxn.rollback()
# else:
#     cnxn.commit()
# finally:
#     cnxn.autocommit = True


cursor.close()
cnxn.close()