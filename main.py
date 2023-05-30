import src.helpers.check as ch
import src.helpers.template as tmp
import src.helpers.writer as wr
import gspread
from datetime import datetime, timedelta
import os
import sys 

myos = ch.checkOS() #check file system
servicePath=ch.giveServicePath(myos) #path for account_service.json

# open google sheet into data
sa=gspread.service_account(filename=servicePath)
sh=sa.open("Gym")
wks=sh.worksheet("Foglio1")
data=wks.get_all_values()


def main(argv):
    if len(argv) < 1:
        # subtract one day from today
        inputdate = datetime.today() - timedelta(days=1)
        inputdate=inputdate.strftime('%d/%m/%Y')
    elif len(argv)==1:
        # read date
        inputdate=argv[0]
    else:
        exit(1)        
    #print(inputdate) 
    if ch.validateDate(inputdate): #check the input
        wr.writeFiles(inputdate,data)
    else:
        print(f"Wrong input (needs dd/mm/yyyy format). You insert: \"{inputdate}\"")


if __name__ == "__main__":
   main(sys.argv[1:])