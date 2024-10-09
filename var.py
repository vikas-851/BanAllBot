import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "28122413"))
    API_HASH = os.getenv("API_HASH", "750432c8e1b221f91fd2c93a92710093")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7531600807:AAFpMRajhL-S_7TCWxAOELpvqLuWRhEzaaQ")
    sudo = os.getenv("SUDO", 5610811504 7453770651)
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
