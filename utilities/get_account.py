import sys
import os


def account(filename):
    """
    reads a configuration file named ia_conf and extracts the account information, web URL, and file path for CSV files.
    :return: a dictionary containing the IA account information, web URL, and file path for CSV files.

    workflow:
    1. Open the ia_conf file using open and os.path.join.
    2. Read lines and create key-value pairs.
    3. Convert the list to a dictionary, removing whitespaces.
    4. Ensure the dictionary contains “username” and “password”.
    5. Verify the presence of “web_url” and “csv_path”.
    6. Return the dictionary if all keys are present.
    """

    with open(os.path.join(sys.path[1], "confs", filename)) as f:
        lines = [line.rstrip('\n').split("=", 1) for line in f.readlines()]
        d = {key.strip(): value.strip() for key, value in lines}
    if "username" not in d or "password" not in d:
        raise Exception("IA account info not found. Please provide it in confs/ia_conf")
    if "web_url" not in d:
        raise Exception("Web url not found. Please provide it in confs/ia_conf")
    if "csv_path" not in d:
        raise Exception("File path for csv files not found. Please provide it in confs/ia_conf")
    return d
