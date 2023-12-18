import os
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


def connect_db(port=None, user=None, password=None):
    try :
        with open(os.path.join(os.path.dirname(__file__), 'dbProperties.properties')) as properties:
            l = [line.split("=") for line in properties.readlines()]
            d = {key.strip(): value.strip() for key, value in l}
        if "server" not in d or "database" not in d:
            raise Exception("Property server or database not found")
    except Exception as e:
        print(e)
        exit()
    else:
        print("Property file load successful!")

    return pyodbc.connect(connect_str(d["server"], d["database"]))

