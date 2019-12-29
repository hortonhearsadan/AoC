import time
from utils import open_file

day = 14
year = 2015

TESTSTRING = ''''''
STRING = ''''''


class Reindeer:
    def __init__(self, speed, duration, rest):
        self.speed = speed
        self.duration = duration
        self.rest = rest

    @property
    def flight_distance(self):
        return self.speed * self.duration

    @property
    def cycle_length(self):
        return self.rest + self.duration


def get_reindeers(string):
    rd = {}
    for s in string:
        s = list(filter(None, s.replace('.\n', '').split(' ')))
        name = s[0]
        speed = float(s[3])
        duration = float(s[6])
        rest = float(s[13])
        rd[name] = Reindeer(speed, duration, rest)

    return rd


def get_distance_after_seconds(r, seconds):
    cycles, remainder = divmod(seconds, r.cycle_length)
    remainder = min(remainder, r.duration)
    partial_cycle_distance = remainder * r.speed

    return cycles * r.flight_distance + partial_cycle_distance


def run1():
    string = open_file(14, 2015)
    reindeers = get_reindeers(string)
    max_distance = 0
    seconds = 2503
    for name, r in reindeers.items():
        distance = get_distance_after_seconds(r, seconds)
        if distance > max_distance:
            lead_reindeer = name
            max_distance = distance

    return max_distance, lead_reindeer


def run2():
    string = open_file(14, 2015)
    reindeers = get_reindeers(string)
    points = {r: 0 for r in reindeers.keys()}
    seconds = 2503
    distances = {r:0 for r in reindeers.keys()}
    for x in range(1, seconds + 1):
        max_distance = 0
        lead_reindeer = ''
        for name, r in reindeers.items():
            distances[name] = get_distance_after_seconds(r, x)
        max_dist = max(d for d in distances.values())
        leaders = [r for r in reindeers.keys() if distances[r] == max_dist]
        for l in leaders:
            points[l] += 1

    return max(v for v in points.values())


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
