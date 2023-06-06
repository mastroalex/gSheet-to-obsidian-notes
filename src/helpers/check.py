from sys import platform
from datetime import datetime



def checkOS():
    if platform == "linux" or platform == "linux2":
    # linux
        # not implemented
        return
    elif platform == "darwin":
    # OS X
        os="M"
    elif platform == "win32":
    # Windows...
        os="W"
    return os

def giveServicePath(os):
    if os=="W":
        servicePath="C:/Users/bigba/%APPDATA%/gspread/service_account.json"    
    elif os=="M":
        servicePath="/Users/alessandromastrofini/Documents/jsonUsefullForObsidian/service_account.json"
    else:
        return
    return servicePath

def validateDate(date_text):
    try:
        datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False


        