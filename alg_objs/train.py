class Train:
    def __init__(self, train_id, train_number):
        self._train_id = train_id
        self._train_number = train_number

    @property
    def train_id(self):
        return self._train_id

    @property
    def train_number(self):
        return self._train_number

    @classmethod
    def parse_from_api_call(cls, api_response):
        train_id = api_response['TrainId']
        train_number = api_response['TrainNumber']
        return cls(train_id, train_number)


class TrackCircuit:
    def __init__(self, circuit_id):
        self._circuit_id = circuit_id

    @classmethod
    def parse_from_api_response(cls, api_response):
        return cls(api_response['CircuitId'])

    @property
    def circuit_id(self):
        return self._circuit_id


class TrainPosition:
    def __init__(self, time_stamp, train, track_circuit):
        """
            object representing the positional relationship between a train and a track circuit
        :param time_stamp:
        :param train: Train object
        :param track_circuit: TrackCircuit object
        """
        self._time_stamp = time_stamp
        self._train = train
        self._track_circuit = track_circuit

    @classmethod
    def parse_from_api_call(cls, utc_timestamp, api_response):
        train = Train.parse_from_api_call(api_response)
        track_circuit = TrackCircuit.parse_from_api_response(api_response)
        return cls(utc_timestamp, train, track_circuit)

    @property
    def time_stamp(self):
        return self._time_stamp

    @property
    def train(self):
        return self._train

    @property
    def track_circuit(self):
        return self._track_circuit


class SystemSnapshot:
    def __init__(self, utc_timestamp, train_positions):
        self._utc_timestamp = utc_timestamp
        self._train_positions = train_positions

    @classmethod
    def parse_from_api_response(cls, utc_timestamp, api_response):
        train_positions = []
        for entry in api_response:
            train_position = TrainPosition.parse_from_api_call(utc_timestamp, entry)
            train_positions.append(train_position)
        return cls(utc_timestamp, train_positions)

    @property
    def utc_timestamp(self):
        return self._utc_timestamp

    @property
    def train_positions(self):
        return self._train_positions

    def __iter__(self):
        return iter(self._train_positions)

