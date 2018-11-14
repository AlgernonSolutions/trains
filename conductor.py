import json

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
