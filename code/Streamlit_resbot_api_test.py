# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:17:04 2025

@author: BYERJ023
"""

import requests
#import datetime;
from datetime import datetime
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

st.title("Jess' departure board")

# Define the API endpoint
url = 'https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=10&duration=60&accessId=46f02d63-48e6-4529-8c2c-4b01befec633&duration=120&id=740021655'
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
    #print(data_skanstull)

else:
    print("Failed to fetch data. Status code: {response.status_code}")

values = get_values_from_nested_dict(data_skanstull)

ct = datetime.now()
print("burf..................")
#stockholm_time = ct + relativedelta(hours=1)
stockholm_time = ct + timedelta(hours=1)
fmt = "%Y-%m-%d %H:%M"
print("Stockholm time: ", stockholm_time.strftime(fmt))

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
st.subheader(data['Departure'][i]['stop'].replace(" (Stockholm kn)",""))
print("")
print('to T-Centralen')
st.markdown("##### to T-Centralen")

for x in data:
    try:
        if data['Departure'][i]['directionFlag'].strip() == '1':
            if "Tunnelbana" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction'].replace(" (Stockholm kn)", "")
                    variable_output_2 = data['Departure'][i]['Product'][0]['operator'] + ' ' + data['Departure'][i]['Product'][0]['operatorCode']
                    print(variable_output, end="   ")                   
                    print(variable_output_2)
                    print("")
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
        pass
    i = i + 1
    
if num_trains < 1:
    #st.write("No trains at this time")
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
        }}
        p.c {{
          margin-left: 15px;
        }}                    
        </style>
        <p class="c">No trains at this time</p>
    """
    st.markdown(html_str, unsafe_allow_html=True)       
    
i=0
num_trains = 0
print("")
print('from city')
st.markdown("##### from city")

for x in data:
    try:
        if data['Departure'][i]['directionFlag'].strip() == '2':
            if "Tunnelbana" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction'].replace(" (Stockholm kn)", "")
                    variable_output_2 = data['Departure'][i]['Product'][0]['operator'] + ' ' + data['Departure'][i]['Product'][0]['operatorCode']
                    print(variable_output, end="   ")                   
                    print(variable_output_2)
                    print("")
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
        pass
    i = i + 1
    
if num_trains < 1:
    #st.write("No trains at this time")
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
        }}
        p.c {{
          margin-left: 15px;
        }}                    
        </style>
        <p class="c">No trains at this time</p>
    """
    st.markdown(html_str, unsafe_allow_html=True)         


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
    #print(data_skanstull)

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
    st.subheader("Nätgränd busshållplats")
    #print("")
    print('Direction 1')
    st.markdown("##### österutto to Tengdahisgatan")
except:
    ""

for x in data:
    try:
        if data['Departure'][i]['directionFlag'] == '1':
            if "Buss" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction'].replace(" (Stockholm kn)", "").replace('Stockholm Tengdahlsgatan','österut').replace('Motalavägen','väster')
                    variable_output_2 = data['Departure'][i]['Product'][0]['operator'] + ' ' + data['Departure'][i]['Product'][0]['operatorCode']
                    print(variable_output, end="   ")                   
                    print(variable_output_2)
                    print("")
                    #font_size = 14  #st.slider("Enter a font size", 1, 300, value=30)
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
        pass
    i = i + 1
    
if num_trains < 1:
    #st.write("No Buss data available")   
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
        }}
        p.c {{
          margin-left: 15px;
        }}                    
        </style>
        <p class="c">No Buss data available</p>
    """
    st.markdown(html_str, unsafe_allow_html=True)
    
     
print("Nätgränd")
print("")
print('Direction 2')
st.markdown("##### väster to Motalavägen")
i=0
num_trains = 0
for x in data:
    try:
        if data['Departure'][i]['directionFlag'].strip() == '2':
            if "Buss" in data['Departure'][i]['name']:
                    cleaned_tunnelbana = data['Departure'][i]['name'].replace('Länstrafik -', '')
                    cleaned_time = data['Departure'][i]['time'].removesuffix(':00')
                    temp_direction_flag = data['Departure'][i]['directionFlag'].strip()
                    temp_direction = data['Departure'][i]['direction']
                    variable_output = cleaned_time + '    ' + cleaned_tunnelbana + ' - ' + data['Departure'][i]['direction'].replace(" (Stockholm kn)", "").replace('Stockholm Tengdahlsgatan','österut').replace('Motalavägen','väster')
                    variable_output_2 = data['Departure'][i]['Product'][0]['operator'] + ' ' + data['Departure'][i]['Product'][0]['operatorCode']
                    print(variable_output, end="   ")                   
                    print(variable_output_2)
                    print("")
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
        pass
    i = i + 1
    
if num_trains < 1:
    #st.write("No Buss data available")    
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
        }}
        p.c {{
          margin-left: 15px;
        }}                    
        </style>
        <p class="c">No Buss data available</p>
     """
    st.markdown(html_str, unsafe_allow_html=True)

    















