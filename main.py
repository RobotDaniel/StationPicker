import csv
import random
county=input("Enter a County")
print("county")

def csvRead(): 
    with open('NATIONAL_RAIL_STATION_LOG_-_FEB_2025_update.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)  # Create DictReader

        data_list = []  # List to store dictionaries
        for row in csv_reader:
            data_list.append(row)
        return data_list
        
def StationPick(): 
    stations=[]
    for data in data_list:
    if data['County']==county and data['Visited']=="No":
        stations.append(data['Station'])
    print(stations)
    numberOfStations=input("how many staions do you want to vist")

    for i in range(int(numberOfStations)):
    
        print(stations[random.randint(0,(len(stations)-1))])



        


