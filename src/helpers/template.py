import os
import numpy as np

def myPath(myos):
    myfile='mymarkdown.md'
    
    if myos=="W": #windows
        filename=os.path.basename(__file__)
        path=os.path.abspath(__file__)
        mainfolderPath=path.replace(filename,"")
        obsidianPath='C:/Users/bigba/OneDrive/Documenti/Ale'
    
    elif myos=="M": #macos
        filename=os.path.basename(__file__)
        path=os.path.abspath(__file__)
        mainfolderPath=path.replace(filename,"")
        obsidianPath='/Users/alessandromastrofini/Obsidian/Ale'
    exercisePath=obsidianPath+'/Workout'
    
    return filename,path,mainfolderPath,obsidianPath,exercisePath
    
## template for chart with chartjs

def chartText(exType,color,date):
    textForChart=(" \n \n "
    "```dataviewjs  \n"
    f"let EX=\"{exType}\"; \n"
    "dv.header(3,EX);"
    f"const maxvalue=dv.array(dv.pages('\"Workout\"').where(p=>p.exercisename && p.exerciseName.path==EX && p.dateNoLink<dv.date(\"{date}\")+1 && p.dateNoLink>dv.date(\"2022-12-30\")+1  ).max );  \n"
    f"const meanvalue=dv.array(dv.pages('\"Workout\"').where(p=>p.exercisename && p.exerciseName.path==EX && p.dateNoLink<dv.date(\"{date}\")+1 && p.dateNoLink>dv.date(\"2022-12-30\")+1 ).mean );  \n"
    f"const mylabel=dv.array(dv.pages('\"Workout\"').where(p=>p.exercisename && p.exerciseName.path==EX && p.dateNoLink<dv.date(\"{date}\")+1 && p.dateNoLink>dv.date(\"2022-12-30\")+1 ).dateNoLink);  \n"
    "const chartData = {    \n"
    "type: 'line',    \n"
    "data: {    \n"
    "labels: mylabel.map(t => t.toLocaleString([], { month: '2-digit', day: '2-digit', year: '4-digit', hour: '2-digit', minute: '2-digit' })),   \n" 
    "datasets: [{    \n"
    "label: \"Max\",    \n"
    "data: maxvalue.values,  \n"
    f"backgroundColor: ['#{color}'],  \n"
    "borderWidth:  1  \n"
    "},{    \n"
    "label: \"Mean\",    \n"
    "data: meanvalue.values,      \n"
    "backgroundColor: ['#a0ada3'],  \n"
    "borderWidth:  1  \n"
    "}]    \n"
    "}    \n"
    "}  \n"
    "window.renderChart(chartData, this.container);  \n"
    "```   \n" 
    "\n \n")
    return textForChart

# template for the markdown header with YAML syntax

def fileHeader(date,exerciseType,SxR,reps,weigth):
    header=("---\n"
    "type:: gymExercise \n")
    datestring="date:: [["+str(date)+"]] \n dateNoLink::"+str(date)+" \n"
    exerciseName="exerciseName:: [["+str(exerciseType)+"]] \n"
    SxR_string="SxR:: "+str(SxR)+" \n"
    S1="S1:: "+str(reps[0])+" \n"
    W1="W1:: "+str(weigth[0])+" \n"
    S2="S2:: "+str(reps[1])+" \n"
    W2="W2:: "+str(weigth[1])+" \n"
    S3="S3:: "+str(reps[2])+" \n"
    W3="W3:: "+str(weigth[2])+" \n"
    S4="S4:: "+str(reps[3])+" \n"
    W4="W4:: "+str(weigth[3])+" \n"
    S5="S5:: "+str(reps[4])+" \n"
    W5="W5:: "+str(weigth[4])+"\n"
    weigthNum=[float(x.replace(',', '.')) for x in weigth]
    std="std:: "+str(np.nanstd(weigthNum).round(decimals=2))+"\n"
    maxWeigth="max:: "+str(np.nanmax(weigthNum))+"\n"
    minWeigth="min:: "+str(np.nanmin(weigthNum))+"\n"
    meanWeigth="mean:: "+str(np.nanmean(weigthNum).round(decimals=2))+"\n"
    header=header+datestring+exerciseName+SxR_string+S1+W1+S2+W2+S3+W3+S4+W4+S5+W5+maxWeigth+minWeigth+meanWeigth+std
    header=header+'---\n'
    return header

# workout template

def createWorkout(date,dayType,exerciseType,SxR,reps,weigth):
    header=("---\n"
    "type:: workout \n")
    datestring="date:: [["+str(date)+"]] \ndateNoLink::"+str(date)+" \n"
    dayTypeString="dayType:: "+str(dayType)+" \n"
    header=header+datestring+dayTypeString+"cal:: \n"
    header=header+'---\n'
    text=(
       "# Workout -" + str(date) +"\n"
       "[["+str(date)+"]] \n"
       "```dataview \n"
       "TABLE WITHOUT ID \n" 
       'exerciseName as "Name",\n'
        'SxR as "SxR",\n'
        'max as "Max",\n'
        'mean as "Mean",\n'
        'std as "Std"\n'
        'FROM "Workout" \n'
        'where contains(type,"gymExercise") and contains(string(date),"'+str(date)+'")\n'
        "```\n"
    )
    exType=["Stacco", "Bench press", "Pull up","Squat S","Military"]
    color=["ba342b","ba342b","58ba2b","ba6e34","bf2e91"]
    mychart=""
    for i in range(len(exType)):
        mychart=mychart+chartText(exType[i],color[i],str(date))
    return header+text+"\n"+mychart+"\n"