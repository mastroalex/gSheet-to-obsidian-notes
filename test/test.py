import src.helpers.check as ch
import src.helpers.template as tmp
import gspread
from datetime import datetime
import os
from pathlib import Path


myos = ch.checkOS() #check file system
servicePath=ch.giveServicePath(myos) #path for account_service.json
# import paths
paths=tmp.myPath(myos)
obsidianPath=paths[3] #see template.py
exercisePath=paths[4] #see template.py

# open google sheet into data
sa=gspread.service_account(filename=servicePath)
sh=sa.open("Gym")
wks=sh.worksheet("Foglio1")
data=wks.get_all_values()

# to avoid rewriting all the file, ask a starting date
inputdate=input("Enter date (dd/mm/yyyy): ")

if ch.validateDate(inputdate): #check the input
    # format date
    filterdate= datetime.strptime(inputdate, '%d/%m/%Y').date()     
    # check every row of the sheet   
    for i in range(len(data)):
        # check if the first column contain a date
        if ch.validateDate(data[i][0]):
            for j in range(len(data[i])):
                # clean empty cells substituing with a NaN
                if data[i][j]=='':
                    data[i][j]='nan'
            # convert date format        
            dateValue=datetime.strptime(data[i][0], '%d/%m/%Y').date()
            
            # consider only value afte the input date
            if dateValue>filterdate:    
                # convert the row, each row contain:
                # date | day tipe (char) | series X reps | weight (x5) | reps (x5) |
                dayType=data[i][1]
                exerciseType=data[i][2]
                SxR=data[i][3]
                weigth=[data[i][4], data[i][5], data[i][6], data[i][7], data[i][8]]
                reps=[data[i][12], data[i][13], data[i][14], data[i][15], data[i][16]]               
                
                # create header for the makrdown to inlucde YAML tags
                head=tmp.fileHeader(dateValue,exerciseType,SxR,reps,weigth)
                #print(head)
                if i==0:
                    index=0
                if i>0:
                    if data[i][0]==data[i-1][0]:
                    # check for new training day and increment index
                        index=index+1
                    else:
                        # enter in a new day --> reset index --> fill the template
                        index=0
                        # file name and path
                        WorkoutCurrentFilePath=Path(exercisePath+"/"+str(dateValue)+"/workout_"+str(dateValue)+".md")
                        # create daily directory in Obsidan/Workout/new_day
                        os.makedirs(os.path.dirname(WorkoutCurrentFilePath), exist_ok=True)
                        # fill the template
                        workoutText=tmp.createWorkout(dateValue,dayType,exerciseType,SxR,reps,weigth)
                        # write daily file
                        with open(WorkoutCurrentFilePath,'w') as f:
                            f.write(workoutText)
                
                currentFilePath=Path(exercisePath+"/"+str(dateValue)+"/"+str(dateValue)+"_"+str(index)+".md")
                #print(currentFilePath)
                os.makedirs(os.path.dirname(currentFilePath), exist_ok=True)
                # write exercise
                with open(currentFilePath,'w') as f:
                    f.write(head+"\n"+"# workout - "+str(dateValue)+"_"+str(index)+"\n")

else:
    print(f"Wrong input. You insert \"{inputdate}\"")

