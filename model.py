import requests
import json
import csv

state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "D.C.", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",  "Michigan", "Minnesota", "Mississippi", "Missouri",  "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",  "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
headers = {'Content-type': 'application/json'}

stateData = {}

stateID = ""
for i in range(1,10):
    stateID = ("LASST0" + str(i) + "0000000000003")
    data = json.dumps({"seriesid": stateID,"startyear":"2011", "endyear":"2014"})
    p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
    
    stateData[state_names[i-1]] = "placeholder"

for i in range(10,57):
    stateID = ("LASST" + str(i) + "0000000000003")
    data = json.dumps({"seriesid": stateID,"startyear":"2011", "endyear":"2014"})
    p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
    
    stateData[state_names[i-1]] = "placeholder"



json_data = json.loads(p.text)
print(json_data)
