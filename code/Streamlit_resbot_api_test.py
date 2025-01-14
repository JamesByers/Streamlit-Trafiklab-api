# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:17:04 2025

@author: BYERJ023
"""

import requests
#import ast
import datetime;
#from pytz import timezone
from dateutil.relativedelta import relativedelta
import streamlit as st


def get_values_from_nested_dict(response_dict):
    values = []
    for key, value in response_dict.items():
        if isinstance(value, dict):
            for inner_key, inner_value in value.items():
                values.append(inner_value)
        else:
            values.append(value)
    return values
st.title("Jess' departure board POC")

# Define the API endpoint
url = 'https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=10&duratoin-60&accessId=46f02d63-48e6-4529-8c2c-4b01befec633&duration=120&id=740021655'
#url = 'https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=20&accessId=46f02d63-48e6-4529-8c2c-4b01befec633&duration=60&id=740021655'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data_skanstull = response.json()
    # Convert dictionary to string
    #print(data_skanstull)
    data_skanstull_str = str(data_skanstull)
    # Replace single quotes with double quotes
    data_skanstull_str = data_skanstull_str.replace("'", '"')
    print(data_skanstull)

else:
    print("Failed to fetch data. Status code: {response.status_code}")
    

values = get_values_from_nested_dict(data_skanstull)

ct = datetime.datetime.now()
subHoursNumber = 9;
stockholm_time = ct + relativedelta(hours=subHoursNumber)
fmt = "%Y-%m-%d %H:%M %p"
print("Stockholm time: ", stockholm_time.strftime(fmt))
#st.write("Last updated: ", stockholm_time.strftime(fmt), "(Stockholm time)")
#st.markdown("*Refresh browser to update*")
#print("Current Stockholm time:   ", ct)

update_time_string = "Last updated: " + stockholm_time.strftime(fmt) + "      (Stockholm time)"
html_str = f"""
    <style>
    p.a {{
      font-weight: bold;
      color:green;
      margin-left: 15px;
    }}
    p.b {{
      margin-left: 30px;
    }} 
    p.c {{
      font-style: italic;
      margin-left: 30px;
    }}                          
    </style>
    <p class="b">{update_time_string}</p>
    <p class="c">Refresh browser to update</p>
    """
st.markdown(html_str, unsafe_allow_html=True)

data = data_skanstull
#print(data)


i=0
num_trains = 0
print(data['Departure'][i]['stop'])
st.subheader(data['Departure'][i]['stop'])
print("")
print('To city center')
st.markdown("##### To city center")


for x in data:
    try:
        if data['Departure'][i]['directionFlag'].strip() == '1':
            if "Tunnelbana" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    cleaned_tunnelbana_markdown = "**Foo**"
                    print(cleaned_tunnelbana, ', ', data['Departure'][i]['date'], cleaned_time)
                  
                    print("  ", "directionFlag: ", data['Departure'][i]['directionFlag'].strip())
                    print("  ", "Direction: ", data['Departure'][i]['direction'])
                    print("")

                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction']
                    font_size = 14  #st.slider("Enter a font size", 1, 300, value=30)
                    html_str = f"""
                        <style>
                        p.a {{
                          font-weight: bold;
                          color:green;
                          margin-left: 15px;
                        }}
                        p.b {{
                          margin-left: 30px;
                        }}                          
                        </style>
                        <p class="a">{variable_output}</p>
                        """
                    st.markdown(html_str, unsafe_allow_html=True)
                    #st.write("")
                    num_trains = num_trains + 1
    except:
        ""
    i = i + 1
    
if num_trains < 1:
    st.write("No trains at this time")    
    
    
    
    
print("")
print(data['Departure'][i]['stop'])
print('From city center)')
st.markdown("##### From city center")
i=0
num_trains = 0
for x in data:
    try:
        if data['Departure'][i]['directionFlag'].strip() == '2':
            if "Tunnelbana" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    cleaned_tunnelbana_markdown = "**Foo**"
                    print(cleaned_tunnelbana, ', ', data['Departure'][i]['date'], cleaned_time)
                  
                    print("  ", "directionFlag: ", data['Departure'][i]['directionFlag'].strip())
                    print("  ", "Direction: ", data['Departure'][i]['direction'])
                    print("")

                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction']
                    font_size = 14  #st.slider("Enter a font size", 1, 300, value=30)
                    html_str = f"""
                        <style>
                        p.a {{
                          font-weight: bold;
                          margin-left: 15px;
                        }}
                        p.b {{
                          margin-left: 30px;
                        }}                          
                        </style>
                        <p class="a">{variable_output}</p>
                        """
                    st.markdown(html_str, unsafe_allow_html=True)
                    #st.write("")
                    num_trains = num_trains + 1
    except:
        ""
    i = i + 1

if num_trains < 1:
    st.write("No trains at this time")    


# Define the API endpoint
url = 'https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=10&id=740046211&duration=60&accessId=46f02d63-48e6-4529-8c2c-4b01befec633'
#url = 'https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=20&accessId=46f02d63-48e6-4529-8c2c-4b01befec633&duration=60&id=740021655'

# Define the API endpoint
#url = 'https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=10&duratoin-60&accessId=46f02d63-48e6-4529-8c2c-4b01befec633&duration=60&id=740021655'
#url = 'https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=20&accessId=46f02d63-48e6-4529-8c2c-4b01befec633&duration=60&id=740021655'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data_skanstull = response.json()
    # Convert dictionary to string
    #print(data_skanstull)
    data_skanstull_str = str(data_skanstull)
    # Replace single quotes with double quotes
    data_skanstull_str = data_skanstull_str.replace("'", '"')
    print(data_skanstull)

else:
    print("Failed to fetch data. Status code: {response.status_code}")
    

values = get_values_from_nested_dict(data_skanstull)

data = data_skanstull
#print(data)


i=0
num_trains = 0
try:
    #print(data['Departure'][i]['stop'])
    #st.subheader(data['Departure'][i]['stop'])
    print("Nätgränd (Stockholm kn)")
    st.subheader("Nätgränd (Stockholm kn)")
    #print("")
    print('Direction 1')
    st.markdown("##### to Stockholm Tengdahisgatan")
except:
    ""
    #print("No bus stop data)avaialble")

for x in data:
    try:
        if data['Departure'][i]['directionFlag'].strip() == '1':
            if "Buss" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    cleaned_tunnelbana_markdown = "**Foo**"
                    print(cleaned_tunnelbana, ', ', data['Departure'][i]['date'], cleaned_time)
                    print("  ", "directionFlag: ", data['Departure'][i]['directionFlag'].strip())
                    print("  ", "Direction: ", data['Departure'][i]['direction'])
                    print("")

                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction']
                    html_str = f"""
                        <style>
                        p.a {{
                          font-weight: bold;
                          color:green;
                          margin-left: 15px;
                        }}
                        p.b {{
                          margin-left: 30px;
                        }}                          
                        </style>
                        <p class="a">{variable_output}</p>
                        """
                    st.markdown(html_str, unsafe_allow_html=True)
                    #st.write("")
                    num_trains = num_trains + 1
    except:
        ""
    i = i + 1
    
if num_trains < 1:
    st.write("No buss data available")    
    
    
     
print("Nätgränd (Stockholm kn)")
print("")
print('Direction 2')
st.markdown("##### to Motalavägen")
#try:
#    print(data['Departure'][i]['stop'])
#except:
#    print("No buss data availalble")
i=0
num_trains = 0
for x in data:
    try:
        if data['Departure'][i]['directionFlag'].strip() == '2':
            if "Buss" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    cleaned_tunnelbana_markdown = "**Foo**"
                    print(cleaned_tunnelbana, ', ', data['Departure'][i]['date'], cleaned_time)
                  
                    print("  ", "directionFlag: ", data['Departure'][i]['directionFlag'].strip())
                    print("  ", "Direction: ", data['Departure'][i]['direction'])
                    print("")

                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction']
                    font_size = 14  #st.slider("Enter a font size", 1, 300, value=30)
                    html_str = f"""
                        <style>
                        p.a {{
                          font-weight: bold;
                          margin-left: 15px;
                        }}
                        p.b {{
                          margin-left: 30px;
                        }}                          
                        </style>
                        <p class="a">{variable_output}</p>
                        """
                    st.markdown(html_str, unsafe_allow_html=True)
                    #st.write("")
                    num_trains = num_trains + 1
    except:
        ""
    i = i + 1

if num_trains < 1:
    st.write("No Buss data available")    
