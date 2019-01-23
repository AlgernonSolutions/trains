from alg_objs.conductor import Conductor

if __name__ == '__main__':
    conductor = Conductor()
    track_circuits = conductor.get_lines(raw=True)
    print(track_circuits)
