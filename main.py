import csv
import random

def Menu():
    menuInput=input("1:Station Pick")
    if menuInput=="1":
        data_list=csvRead()
        StationPick(data_list)
    else:
        print("invalid option")
        Menu()

def csvRead(): 
    print("csv")
    with open('NATIONAL_RAIL_STATION_LOG_-_FEB_2025_update.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)  # Create DictReader

        data_list = []  # List to store dictionaries
        for row in csv_reader:
            data_list.append(row)
        return data_list
        
def StationPick(data_list): 
    county=input("Enter a County")
    print("county")
    global stationsPickList
    stationsPickList=[]
    for data in data_list:
        if data['County']==county and data['Visited']=="No":
            stationsPickList.append(data['Station'])
    print(stationsPickList)
    
    stationRandPick()
def stationRandPick():
    global stationsPickList
    numberOfStations=input("5how many staions do you want to vist")
    try:
        numberOfStations=int(numberOfStations)
    except:
        print("not a number")
        stationRandPick(55)
    if numberOfStations>len(stationsPickList):
        print("too many stations")
        stationRandPick()
    else:    
        for i in range(int(numberOfStations)):
        
            num=random.randint(0,(len(stationsPickList)-1))
            station=stationsPickList[num]
            #print(num)
            print(station)
            stationsPickList.remove(station)
            menuInput=input("continue\n Y=Yes\nN=No (return to menu)")
Menu()

        


