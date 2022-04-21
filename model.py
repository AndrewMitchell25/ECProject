import requests
import json
import csv

stateNames = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "D.C.", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",  "Michigan", "Minnesota", "Mississippi", "Missouri",  "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",  "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

stateData = {}

stateIDs = []
state = 0
for i in range(1,57):
    x = "%02d" % (i,)
    if(i == 7 or i==3 or i == 52 or i == 43 or i==14 or i==11):
        continue
    stateIDs.append("LASST" + x + "0000000000003")
    

startYear = 2003
endYear = 2021
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": stateIDs,"startyear":str(startYear), "endyear":str(endYear), "annualaverage":"true","registrationkey":"345a69db035449398aa0dfb79dbe47f2"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

for i in range(50):
    #get the current state in the data
    currentState = json_data["Results"]["series"][i]["data"]
    stateData[stateNames[i]] = list(range(endYear-startYear+1))
    #for each year
    for k in range(endYear-startYear+1):
        #add up each month and divide by 12 to get average
        yearlyAverage = 0
        for j in range(12):
            yearlyAverage += float(currentState[k*12+j]["value"])
        yearlyAverage = yearlyAverage/12
        yA = round(yearlyAverage, 3)
        stateData[stateNames[i]][k] = yA
print(stateData)

