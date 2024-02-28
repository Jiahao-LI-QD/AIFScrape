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
    """
    This method returns a connection string for connecting to a SQL Server database.
    :param server: (string) The name of the SQL Server instance.
    :param database: (string) The name of the database to connect to.
    :param port: (int) The port number of the SQL Server instance. Defaults to None
    :param user: (string) The username for authentication. Defaults to None.
    :param password: (string) The password for authentication. Defaults to None
    :return: A string that can be used to connect to a SQL Server database.

    Workflow:
    1.If user is None, the function returns a connection string with Windows authentication.
    2.If user is not None, the function returns a connection string with SQL Server authentication.
    3.The connection string includes the server name, database name, optional port number, optional
      username, and optional password.
    """
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
    """
    This method reads a properties file to get the server, database, port, user, and password information.
    It then calls the connect_str function to generate a connection string and uses it to establish a
    connection to a SQL Server database using the pyodbc library.
    :param port: The port number of the SQL Server instance. Defaults to None.
    :param user: The username for authentication. Defaults to None.
    :param password:  The password for authentication. Defaults to None.
    :return: A connection object that can be used to interact with the SQL Server database.

    Workflow:
    1.The function tries to open the properties file and reads its contents.
    2.It splits each line of the file by the "=" character and creates a dictionary with the key-value pairs.
    3.It checks if the "server" and "database" keys exist in the dictionary. If not, it raises an exception.
    4.If the "port", "user", and "password" keys do not exist in the dictionary, it sets them to None.
    5.If the properties file is successfully loaded, it prints a success message.
    6.The function calls the connect_str function with the server, database, port, user, and password
      information from the dictionary.
    7.It uses the generated connection string to establish a connection to the SQL Server database using
      the pyodbc library.
    8.The established connection is returned.
    """
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
