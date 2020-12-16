import time

dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = '''0,3,6'''
TESTSTRING1 = '''1,3,2'''
TESTSTRING2 = '''2,1,3'''
TESTSTRING3 = '''3,1,2'''
STRING = '''0,14,6,20,1,4'''

class Spoken:
    def __init__(self,num,spoken):
        self.num=num
        self.spoken=spoken
        self.previous_spoken=None

    def is_repeat(self):
        return True if self.previous_spoken else False

    def age(self):
        return self.spoken-self.previous_spoken

    def update(self, turn):
        self.previous_spoken = self.spoken
        self.spoken = turn

def parse_input():
    f = STRING.split(',')
    inputs =[int(i) for i in f]


    return inputs

def run1(data,turns):
    spoken = {i:Spoken(i,j) for j,i in enumerate(data,1)}
    previous = data[-1]
    for i in range(len(data)+1,turns+1):
        s= spoken[previous]
        if s.is_repeat():
            previous= s.age()
        else:
            previous = 0

        if previous in spoken.keys():
            spoken[previous].update(i)
        else:
            spoken[previous] = Spoken(previous,i)
    return previous

def run2(data):
    pass


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs,2020)
    g = run1(inputs,30_000_000)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
