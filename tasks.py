from datetime import datetime

from alg_objs.conductor import Conductor, TrackCircuit
from alg_objs.train import SystemSnapshot


def find_longest_track():
    conductor = Conductor()
    api_key = conductor.api_key
    circuits = conductor.get_track_circuits()
    new_circuits = []
    for line in circuits.values():
        for circuit_id, circuit in line.items():
            neighbors = circuit['Neighbors']
            right_neighbors = []
            left_neighbors = []
            for neighbor in neighbors:
                neighbor_type = neighbor['NeighborType']
                if neighbor_type == 'Left':
                    left_neighbors.extend(neighbor['CircuitIds'])
                if neighbor_type == 'Right':
                    right_neighbors.extend(neighbor['CircuitIds'])
            new_circuit = TrackCircuit(circuit['Track'], circuit['CircuitId'], left_neighbors, right_neighbors)
            new_circuits.append(new_circuit)
    print(new_circuits)


def draw():
    import networkx as nx
    import matplotlib.pyplot as plt

    options = {
        'node_size': 200,
        'width': 3,
    }
    G = nx.Graph()
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold', **options)

    plt.show()


def take_snapshort():
    api_response = Conductor().get_train_positions()
    utc_timestamp = datetime.now()
    snap_short = SystemSnapshot.parse_from_api_response(utc_timestamp, api_response.values())
    return snap_short


if __name__ == '__main__':
    short_shorts = take_snapshort()
    for train_position in short_shorts:
        print(train_position)
    print(short_shorts)
