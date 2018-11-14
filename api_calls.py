import json
from time import sleep

import requests

#this is a change comment, to demonstrate how to break things

def get_train_position():
    pass


def add(number_one, number_two):
    results = int(number_one) + int(number_two)
    return results


def generate_greeting(username):
    results = 'Hello ' + str(username)
    return results


def get_station_locations(api_key=None):
    if not api_key:
        api_key = '1ea53d88753446d4b266fc065b1bd241'


def get_train_positions(api_key=None):
    if not api_key:
        api_key = '1ea53d88753446d4b266fc065b1bd241'
    url = 'https://api.wmata.com/TrainPositions/TrainPositions/'
    google_homepage = requests.get(url, headers={'api_key': api_key}, params={'contentType': 'json'})
    results = (json.loads(google_homepage.content))
    train_positions = {}
    for entry in results['TrainPositions']:
        circuit_id = entry['CircuitId']
        train_id = entry['TrainId']
        train_positions[train_id] = entry
    return train_positions


def get_track_circuits(api_key=None):
    if not api_key:
        api_key = '1ea53d88753446d4b266fc065b1bd241'
    url = 'https://api.wmata.com/TrainPositions/TrackCircuits/'
    google_homepage = requests.get(url, headers={'api_key': api_key}, params={'contentType': 'json'})
    results = (json.loads(google_homepage.content))
    tracks = {}
    track_circuits = results['TrackCircuits']
    for circuit in track_circuits:
        track_number = circuit['Track']
        circuit_id = circuit['CircuitId']
        if track_number not in tracks:
            tracks[track_number] = {}
        tracks[track_number][circuit_id] = circuit
    return tracks


def get_lines(api_key=None):
    if not api_key:
        api_key = '1ea53d88753446d4b266fc065b1bd241'
    url = 'https://api.wmata.com/Rail.svc/json/jLines'
    google_homepage = requests.get(url, headers={'api_key': api_key})
    results = (json.loads(google_homepage.content))
    return results['Lines']


def get_stations(line_code, api_key=None):
    if not api_key:
        api_key = '1ea53d88753446d4b266fc065b1bd241'
    url = 'https://api.wmata.com/Rail.svc/json/jStations'
    results = requests.get(url, params={'LineCode': line_code}, headers={'api_key': api_key})
    return json.loads(results.content)['Stations']


def get_station_parking_information(station_code, api_key=None):
    if not api_key:
        api_key = '1ea53d88753446d4b266fc065b1bd241'
    url = 'https://api.wmata.com/Rail.svc/json/jStationParking'
    results = requests.get(url, params={'StationCode': station_code}, headers={'api_key': api_key})
    return json.loads(results.content)['StationsParking']


def get_station_lat_lon(api_key=None):
    pacer = 0
    station_locations = {}
    lines = get_lines(api_key)
    for line in lines:
        line_code = line['LineCode']
        stations = get_stations(line_code)
        for station in stations:
            if pacer > 5:
                sleep(1)
                pacer = 0
            station_locations[station['Name']] = {
                'lat': station['Lat'],
                'lon': station['Lon']
            }
            pacer += 1
    return station_locations


lat_lon = get_station_lat_lon()
lines = get_lines()
all_stations = {}
for line in lines:
    if line['DisplayName'] != 'Red':
        continue
    line_code = line['LineCode']
    stations = get_stations(line_code)
    for station in stations:
        station_name = station['Name']
        all_stations[station_name] = station['Address']
        sleep(1)
        parking = get_station_parking_information(station['Code'])
        if not parking:
            print('station with code %s, on line code %s has no parking' % (line_code, station['Code']))
            continue
        print('the station with code %s, on line code %s has parking' % (line_code, station['Code']))
print(all_stations)

