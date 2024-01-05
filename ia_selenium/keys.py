import sys
import os

def ia_account():
    with open(os.path.join(sys.path[0], r"confs\ia_conf")) as f:
        l = [line.split("=") for line in f.readlines()]
        d = {key.strip(): value.strip() for key, value in l}
    if "username" not in d or "password" not in d:
        raise Exception("IA account info not found. Please provide it in confs/ia_conf")
    if "web_url" not in d:
        raise Exception("Web url not found. Please provide it in confs/ia_conf")
    if "csv_path" not in d:
        raise Exception("File path for csv files not found. Please provide it in confs/ia_conf")
    return d
