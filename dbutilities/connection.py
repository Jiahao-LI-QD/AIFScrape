import pyodbc
# windows authentication
cnxn = pyodbc.connect(r'Driver=SQL Server;'
                      r'Server=.\AIF;'
                      r'Database=test1;'
                      r'Trusted_Connection=yes;')

# username & password
# cnxn = pyodbc.connect('DRIVER={SQL Server};'
#                       r'Server=.\AIF;'
#                       'Database=test1;'
#                       'Port=port#;'
#                       'User ID=sa;'
#                       'Password=password')


