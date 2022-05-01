import numpy as np
import requests
import json
import plotly.express as px
import pandas as pd

stateNames = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",  "Michigan", "Minnesota", "Mississippi", "Missouri",  "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",  "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
stateCodes = [ 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME','MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX','UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

stateData = []

stateIDs = []
state = 0
for i in range(1,57):
    x = "%02d" % (i,)
    if(i == 7 or i==3 or i == 52 or i == 43 or i==14 or i==11):
        continue
    stateIDs.append("LASST" + x + "0000000000003")
    

startYear = 2003
endYear = 2021
years = np.linspace(startYear, endYear, endYear-startYear+1)
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": stateIDs,"startyear":str(startYear), "endyear":str(endYear), "annualaverage":"true","registrationkey":"345a69db035449398aa0dfb79dbe47f2"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

for i in range(50):
    #get the current state in the data
    currentState = json_data["Results"]["series"][i]["data"]
    #for each year
    for k in range(endYear-startYear+1):
        #add up each month and divide by 12 to get average
        yearlyAverage = 0
        for j in range(12):
            yearlyAverage += float(currentState[k*12+j]["value"])
        yearlyAverage = yearlyAverage/12
        yA = round(yearlyAverage, 3)
        stateData.append([stateNames[i], k+startYear, yA, stateCodes[i]])
print(stateData)

df = pd.DataFrame(stateData, columns=["state", "year", "value", "code"])


print(df)

#fig = px.scatter(df, x='state', y='value', animation_frame='year', range_y=[0,15], labels="Unemployment Rate")

fig = px.choropleth(df, locationmode="USA-states", 
                        locations='code',
                        color='value',
                        color_continuous_scale="Blues",
                        range_color=(0, 15),
                        scope="usa",
                        animation_frame='year',
                        title = 'Unemployment in the US from 2003 to 2021',
                        labels={'value':'Unemployment Rate (%)', 'year':'Year'}
                        )

fig.write_html('first_figure.html', auto_open=True)