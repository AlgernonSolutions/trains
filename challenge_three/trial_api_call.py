from alg_objs.conductor import Conductor

if __name__ == '__main__':
    conductor = Conductor(secondary=True, random_arg=True)
    track_circuits = conductor.get_lines(raw=True)
    print(track_circuits)
