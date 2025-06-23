import requests
import time
import json
from geopy.distance import distance

def get_data(url, response, data, my_location):
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)
    return response.json()

def get_route(icao24, begin, end):
    url = "https://opensky-network.org/api/flights/aircraft"
    parameters = {
        'icao24': icao24,
        'begin': begin,
        'end': end
    }
    if response.status_code == 200:
        return response2.json()
    else:
        print(f"error: {response.status_code}")
        return None

def file_writer(data, filename):
    try:
        with open(data, "w") as json_file:
        json.dump(data, json_file, indent=4)
        print(f"JSON data successfully written to {data}")
    except IOError as e:
        print(f"error writing to file: {e}") 

def main()
    my_location = (42.2710, 71.8099) #wpi latitude & longitude
    data = get_data()

    file_writer(data, "planes_data.json")

    for state in data['states']:
        callsign = state[1]
        lat = state[6]
        lon = state[5]
        alt = state[7]
    
    if lat is not None and lon is not None:
        plane_location = (lat, lon)
        dist = distance(my_location, plane_location).km
    
        if dist < 5 and alt and alt < 2000
            print(f"Plane {callsign} overhead!! Go take a look!")