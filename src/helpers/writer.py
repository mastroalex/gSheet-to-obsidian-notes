from datetime import datetime, timedelta
import src.helpers.check as ch
import src.helpers.template as tmp
import os
from pathlib import Path

myos = ch.checkOS() #check file system
servicePath=ch.giveServicePath(myos) #path for account_service.json
# import paths
paths=tmp.myPath(myos)
obsidianPath=paths[3] #see template.py
exercisePath=paths[4] #see template.py

def writeFiles(inputdate,data):
 # format date
        filterdate= datetime.strptime(inputdate, '%d/%m/%Y').date()     
        # check every row of the sheet   
        for i in range(len(data)):
            # check if the first column contain a date
            if ch.validateDate(data[i][0]):
                for j in range(len(data[i])):
                    # clean empty cells substituing with a NaN
                    if data[i][j]=='':
                        # it is important to avoid empty cell for mean, std and charts
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
                        # set index to zero when new day starts
                        # index represents the exercise inside the same training day
                        index=0
                    if i>0:
                        if data[i][0]==data[i-1][0]:
                            # if the date is the same of the previous cell
                            # we are in the same training day, so we need to
                            # increment the exercise index
                            # check for new exercise and increment index
                            index=index+1
                        else:
                            # enter in a new day --> reset index --> fill the template
                            index=0
                            # file name and path with the following structure:
                            # workout/date/workout_data .md
                            WorkoutCurrentFilePath=Path(exercisePath+"/"+str(dateValue)+"/workout_"+str(dateValue)+".md")
                            # create daily directory in Obsidan/Workout/new_day
                            os.makedirs(os.path.dirname(WorkoutCurrentFilePath), exist_ok=True)
                            # fill the template
                            workoutText=tmp.createWorkout(dateValue,dayType,exerciseType,SxR,reps,weigth)
                            # write daily file
                            with open(WorkoutCurrentFilePath,'w') as f:
                                f.write(workoutText)
                    
                    # file name and path with the following structure:
                    # /date/date_index .md
                    currentFilePath=Path(exercisePath+"/"+str(dateValue)+"/"+str(dateValue)+"_"+str(index)+".md")
                    os.makedirs(os.path.dirname(currentFilePath), exist_ok=True)
                    # write exercise
                    with open(currentFilePath,'w') as f:
                        f.write(head+"\n"+"# workout - "+str(dateValue)+"_"+str(index)+"\n")
