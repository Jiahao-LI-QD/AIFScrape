import pyodbc

# windows authentication
# cnxn = pyodbc.connect(r'Driver=SQL Server;'
#                       r'Server=.\AIF;'
#                       r'Database=test1;'
#                       r'Trusted_Connection=yes;')


# username & password
# cnxn = pyodbc.connect('DRIVER={SQL Server};'
#                       r'Server=.\AIF;'
#                       'Database=test1;'
#                       'Port=port#;'
#                       'User ID=sa;'
#                       'Password=password')


def connect_str(server, database, port=None, user=None, password=None):
    if user is None:
        return (f'Driver={{SQL Server}}; '
                f'Server=.\\{server}; '
                f'Database={database}; '
                f'Trusted_Connection=yes;')
    else:
        return (f'Driver={{SQL Server}}; '
                f'Server=.\\{server}; '
                f'Database={database}; '
                f'port={port}; '
                f'User ID={user}; '
                f'Password={password};')


def connect_db(server, database, port=None, user=None, password=None):
    return pyodbc.connect(connect_str(server, database, port, user, password))


