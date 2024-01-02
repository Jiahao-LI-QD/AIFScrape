import sys
import os

def ia_account():
    with open(os.path.join(sys.path[1], r"keys\ia_account")) as f:
        l = [line.split("=") for line in f.readlines()]
        d = {key.strip(): value.strip() for key, value in l}
    if "user" not in d or "pwd" not in d:
        raise Exception("IA account file not found. Please provide it in keys/ia_account")
    return d
