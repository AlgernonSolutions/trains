from alg_objs.conductor import Conductor, TrackCircuit


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


if __name__ == '__main__':
    conductor = Conductor()
    track_circuits = conductor.get_track_circuits()
    results = find_longest_track()
    print(results)
