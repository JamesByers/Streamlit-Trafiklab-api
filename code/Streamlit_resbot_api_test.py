# -*- coding: utf-8 -*-
"""
@author: BYERJ023
"""

import requests
from datetime import datetime
import pytz
import streamlit as st

# --- NEW: Dynamic ID Lookup Function ---
@st.cache_data
def get_station_id(api_key, search_term):
    """Automatically finds the Reserobot extId for a given station name."""
    url = "https://api.resrobot.se/v2.1/location.name"
    params = {
        "input": search_term,
        "format": "json",
        "accessId": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for item in data.get("stopLocationOrCoordLocation", []):
            if "StopLocation" in item and "extId" in item["StopLocation"]:
                return item["StopLocation"]["extId"]
    return None

st.title("Jess' departure board")

API_KEY = "46f02d63-48e6-4529-8c2c-4b01befec633"

# Automatically find the ID for Midsommarkransen (Streamlit caches this so it only runs once!)
tunnelbana_id = get_station_id(API_KEY, "Midsommarkransen")
bus_id = "740051247" # We know this one is correct for Svandammsplan!

if not tunnelbana_id:
    st.error("Could not dynamically find the Midsommarkransen ID. Check API status.")
    st.stop()


# ==========================================
# TIME AND HEADER
# ==========================================
stockholm_tz = pytz.timezone('Europe/Stockholm')
now_in_stockholm = datetime.now(stockholm_tz)
fmt = "%Y-%m-%d %H:%M"

update_time_string = f"Last updated: {now_in_stockholm.strftime(fmt)}      (Stockholm time)"
html_str = f"""
    <style>
    p.b {{ margin-left: 30px; }} 
    p.c {{ font-style: italic; margin-left: 30px; }}                          
    </style>
    <p class="b">{update_time_string}</p>
    <p class="c">Refresh browser to update</p>
"""
st.markdown(html_str, unsafe_allow_html=True)


# ==========================================
# TUNNELBANA SECTION (MIDSOMMARKRANSEN)
# ==========================================
url_tunnelbana = f"https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=10&duration=60&accessId={API_KEY}&id={tunnelbana_id}"
response_tb = requests.get(url_tunnelbana)

if response_tb.status_code == 200:
    data_tb = response_tb.json()
else:
    st.error(f"Failed to fetch Tunnelbana data. Status code: {response_tb.status_code}")
    st.stop()

# Header
if data_tb.get('Departure'):
    station_name = data_tb['Departure'][0]['stop'].replace(" (Stockholm kn)", "")
    st.subheader(station_name)

# --- Tunnelbana Direction 1 ---
st.markdown("##### Mot Mörby centrum / Ropsten")
num_trains = 0
for train in data_tb.get('Departure', []):
    name = train.get('name', '')
    direction = train.get('direction', '')
    direction_flag = str(train.get('directionFlag', '')).strip()

    if "Tunnelbana" in name and direction_flag == '1':
        cleaned_tunnelbana = name.replace('Länstrafik -', '')
        cleaned_time = train.get('time', '').removesuffix(':00')
        clean_dir = direction.replace(" (Stockholm kn)", "")
        
        variable_output = f"{cleaned_time}    {cleaned_tunnelbana} - {clean_dir}"
        
        html_str = f'<p style="font-weight: bold; color:green; margin-left: 15px;">{variable_output}</p>'
        st.markdown(html_str, unsafe_allow_html=True)
        num_trains += 1
        
if num_trains < 1:
    st.markdown('<p style="margin-left: 15px; font-style: italic;">No trains at this time</p>', unsafe_allow_html=True)


# --- Tunnelbana Direction 2 ---
st.markdown("##### Mot Fruängen")
num_trains_2 = 0
for train in data_tb.get('Departure', []):
    name = train.get('name', '')
    direction = train.get('direction', '')
    direction_flag = str(train.get('directionFlag', '')).strip()

    if "Tunnelbana" in name and direction_flag == '2':
        cleaned_tunnelbana = name.replace('Länstrafik -', '')
        cleaned_time = train.get('time', '').removesuffix(':00')
        clean_dir = direction.replace(" (Stockholm kn)", "")
        
        variable_output = f"{cleaned_time}    {cleaned_tunnelbana} - {clean_dir}"
        
        html_str = f'<p style="font-weight: bold; color:green; margin-left: 15px;">{variable_output}</p>'
        st.markdown(html_str, unsafe_allow_html=True)
        num_trains_2 += 1
        
if num_trains_2 < 1:
    st.markdown('<p style="margin-left: 15px; font-style: italic;">No trains at this time</p>', unsafe_allow_html=True)


# ==========================================
# BUS SECTION (SVANDAMMSPLAN)
# ==========================================
url_bus = f"https://api.resrobot.se/v2.1/departureBoard?format=json&maxJourneys=10&duration=120&accessId={API_KEY}&id={bus_id}"
response_bus = requests.get(url_bus)

if response_bus.status_code == 200:
    data_bus = response_bus.json()
else:
    st.error(f"Failed to fetch Bus data. Status code: {response_bus.status_code}")
    st.stop()

st.subheader("Svandammsplan busshållplats")

# --- Bus Direction 1 ---
st.markdown("##### Mot Liljeholmen")
num_buses_1 = 0
for bus in data_bus.get('Departure', []):
    name = bus.get('name', '')
    direction = bus.get('direction', '')
    direction_flag = str(bus.get('directionFlag', '')).strip()

    if "Buss" in name and direction_flag == '1':
        cleaned_buss = name.replace('Länstrafik -', '')
        cleaned_time = bus.get('time', '').removesuffix(':00')
        clean_dir = direction.replace(" (Stockholm kn)", "")
        
        variable_output = f"{cleaned_time}    {cleaned_buss} - {clean_dir}"
        
        html_str = f'<p style="font-weight: bold; color:green; margin-left: 15px;">{variable_output}</p>'
        st.markdown(html_str, unsafe_allow_html=True)
        num_buses_1 += 1
        
if num_buses_1 < 1:
    st.markdown('<p style="margin-left: 15px; font-style: italic;">No Buss data available</p>', unsafe_allow_html=True)


# --- Bus Direction 2 ---
st.markdown("##### Mot Hökmossen / Älvsjö")
num_buses_2 = 0
for bus in data_bus.get('Departure', []):
    name = bus.get('name', '')
    direction = bus.get('direction', '')
    direction_flag = str(bus.get('directionFlag', '')).strip()

    if "Buss" in name and direction_flag == '2':
        cleaned_buss = name.replace('Länstrafik -', '')
        cleaned_time = bus.get('time', '').removesuffix(':00')
        clean_dir = direction.replace(" (Stockholm kn)", "")
        
        variable_output = f"{cleaned_time}    {cleaned_buss} - {clean_dir}"
        
        html_str = f'<p style="font-weight: bold; color:green; margin-left: 15px;">{variable_output}</p>'
        st.markdown(html_str, unsafe_allow_html=True)
        num_buses_2 += 1
        
if num_buses_2 < 1:
    st.markdown('<p style="margin-left: 15px; font-style: italic;">No Buss data available</p>', unsafe_allow_html=True)

    

























