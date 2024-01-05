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
        return (r'Driver={SQL Server}; '
                f'Server=.\\{server}; '
                f'Database={database}; '
                f'Trusted_Connection=yes;')
    else:
        return (r'DRIVER={SQL Server};'
                f'SERVER={server},{port};'  # Note the comma before the port number
                f'DATABASE={database};'  # Replace with your actual database name
                f'UID={user};'  # Your username
                f'PWD={password}') # password


def connect_db(port=None, user=None, password=None):
    try:
        with open(os.path.join(os.path.dirname(__file__), 'dbProperties.properties')) as properties:
            l = [line.split("=") for line in properties.readlines()]
            d = {key.strip(): value.strip() for key, value in l}
        if "server" not in d or "database" not in d:
            raise Exception("Property server or database not found")
        if "port" not in d or "user" not in d or "password" not in d:
            d["port"] = None
            d["user"] = None
            d["password"] = None
    except Exception as e:
        print(e)
        exit()
    else:
        print("Property file load successful!")
    connection_string = connect_str(d["server"], d["database"], d["port"], d["user"], d["password"])
    print(connection_string)
    # connection_string = (
    #     "DRIVER={ODBC Driver 17 for SQL Server};"
    #     "SERVER=192.168.2.63,51433;"  # Note the comma separating the IP and the port
    #     "DATABASE=WebInformation;"  # Replace with your actual database name if it's not the default
    #     "UID=Scraper;"
    #     "PWD=123456;"  # Replace with your actual password
    # )
    # print(connection_string)
    return pyodbc.connect(connection_string)
