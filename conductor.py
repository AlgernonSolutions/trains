import json
from time import sleep

import requests


class Conductor:
    def __init__(self, api_key=None):
        if not api_key:
            api_key = '1ea53d88753446d4b266fc065b1bd241'
        self._api_key = api_key
        self._headers = {'api_key': api_key}
        self._session = requests.session()

    def get_track_circuits(self):
        url = 'https://api.wmata.com/TrainPositions/TrackCircuits/'
        response = self._session.get(url, headers=self._headers, params={'contentType': 'json'})
        results = json.loads(response.content)
        tracks = {}
        track_circuits = results['TrackCircuits']
        for circuit in track_circuits:
            track_number = circuit['Track']
            circuit_id = circuit['CircuitId']
            if track_number not in tracks:
                tracks[track_number] = {}
            tracks[track_number][circuit_id] = circuit
        return tracks

    def get_lines(self):
        url = 'https://api.wmata.com/Rail.svc/json/jLines'
        google_homepage = requests.get(url, headers=self._headers)
        results = (json.loads(google_homepage.content))
        return results['Lines']

    def get_stations(self, line_code):
        url = 'https://api.wmata.com/Rail.svc/json/jStations'
        results = requests.get(url, params={'LineCode': line_code}, headers=self._headers)
        return json.loads(results.content)['Stations']

    def get_station_parking_information(self, station_code):
        url = 'https://api.wmata.com/Rail.svc/json/jStationParking'
        results = requests.get(url, params={'StationCode': station_code}, headers=self._headers)
        return json.loads(results.content)['StationsParking']

    def get_station_lat_lon(self):
        pacer = 0
        station_locations = {}
        lines = self.get_lines()
        for line in lines:
            line_code = line['LineCode']
            stations = self.get_stations(line_code)
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

    def get_train_positions(self):
        url = 'https://api.wmata.com/TrainPositions/TrainPositions/'
        google_homepage = requests.get(url, headers=self._headers, params={'contentType': 'json'})
        results = (json.loads(google_homepage.content))
        train_positions = {}
        for entry in results['TrainPositions']:
            circuit_id = entry['CircuitId']
            train_id = entry['TrainId']
            train_positions[train_id] = entry
        return train_positions
