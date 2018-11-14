from conductor import Conductor


def find_longest_track():
    conductor = Conductor()
    return conductor.get_track_circuits()


if __name__ == '__main__':
    results = find_longest_track()
    print(results)
