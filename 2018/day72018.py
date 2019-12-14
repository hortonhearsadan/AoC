import fileinput
import re
import time
import networkx as nx

TESTSTRING = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
'''
STRING = '''Step U must be finished before step A can begin.
Step F must be finished before step Z can begin.
Step B must be finished before step J can begin.
Step O must be finished before step R can begin.
Step H must be finished before step S can begin.
Step T must be finished before step R can begin.
Step L must be finished before step W can begin.
Step M must be finished before step I can begin.
Step Q must be finished before step K can begin.
Step Z must be finished before step V can begin.
Step C must be finished before step E can begin.
Step W must be finished before step I can begin.
Step K must be finished before step S can begin.
Step I must be finished before step Y can begin.
Step P must be finished before step V can begin.
Step V must be finished before step X can begin.
Step R must be finished before step E can begin.
Step N must be finished before step E can begin.
Step X must be finished before step J can begin.
Step A must be finished before step J can begin.
Step S must be finished before step G can begin.
Step J must be finished before step E can begin.
Step Y must be finished before step E can begin.
Step D must be finished before step G can begin.
Step E must be finished before step G can begin.
Step K must be finished before step N can begin.
Step B must be finished before step I can begin.
Step X must be finished before step S can begin.
Step V must be finished before step S can begin.
Step U must be finished before step L can begin.
Step N must be finished before step G can begin.
Step O must be finished before step L can begin.
Step X must be finished before step E can begin.
Step V must be finished before step E can begin.
Step Y must be finished before step G can begin.
Step A must be finished before step Y can begin.
Step M must be finished before step E can begin.
Step F must be finished before step Q can begin.
Step F must be finished before step X can begin.
Step L must be finished before step C can begin.
Step T must be finished before step L can begin.
Step B must be finished before step C can begin.
Step Q must be finished before step N can begin.
Step T must be finished before step G can begin.
Step R must be finished before step D can begin.
Step I must be finished before step A can begin.
Step B must be finished before step M can begin.
Step H must be finished before step A can begin.
Step F must be finished before step K can begin.
Step U must be finished before step F can begin.
Step R must be finished before step A can begin.
Step J must be finished before step D can begin.
Step V must be finished before step Y can begin.
Step F must be finished before step J can begin.
Step C must be finished before step K can begin.
Step M must be finished before step C can begin.
Step F must be finished before step E can begin.
Step I must be finished before step E can begin.
Step T must be finished before step A can begin.
Step J must be finished before step Y can begin.
Step R must be finished before step X can begin.
Step W must be finished before step S can begin.
Step V must be finished before step R can begin.
Step U must be finished before step V can begin.
Step C must be finished before step V can begin.
Step F must be finished before step Y can begin.
Step R must be finished before step G can begin.
Step W must be finished before step N can begin.
Step H must be finished before step N can begin.
Step H must be finished before step Y can begin.
Step B must be finished before step W can begin.
Step M must be finished before step Z can begin.
Step X must be finished before step A can begin.
Step A must be finished before step G can begin.
Step N must be finished before step A can begin.
Step H must be finished before step J can begin.
Step B must be finished before step O can begin.
Step W must be finished before step A can begin.
Step P must be finished before step N can begin.
Step Z must be finished before step G can begin.
Step W must be finished before step D can begin.
Step D must be finished before step E can begin.
Step W must be finished before step J can begin.
Step N must be finished before step D can begin.
Step C must be finished before step J can begin.
Step B must be finished before step Y can begin.
Step F must be finished before step P can begin.
Step L must be finished before step P can begin.
Step X must be finished before step G can begin.
Step R must be finished before step Y can begin.
Step K must be finished before step A can begin.
Step M must be finished before step Y can begin.
Step W must be finished before step Y can begin.
Step F must be finished before step I can begin.
Step L must be finished before step X can begin.
Step R must be finished before step J can begin.
Step V must be finished before step J can begin.
Step V must be finished before step D can begin.
Step H must be finished before step C can begin.
Step O must be finished before step G can begin.
Step P must be finished before step R can begin.
'''


def parse_string(string):
    string = string.replace('Step', '')
    string = string.replace('\n', '')
    s = list(filter(None, re.split("[a-z. ]", string)))
    tuples = []
    for i in range(int(len(s) / 2)):
        u = s[2*i]
        v = s[2*i + 1]
        tuples.append((u, v))
    return tuples,list(sorted(set(s)))


def run1():
    string = STRING
    tuples, letters = parse_string(string)
    g = nx.DiGraph(tuples)
    start_point = 'B'
    current_point = start_point
    choices = set()
    step=[current_point]
    for i in range(len(letters)-1):
        new_choices = set(g[current_point])
        for c in new_choices:
            if not nx.ancestors(g,c) - set(step):
                choices.add(c)
            if not nx.ancestors(g,c):
                choices.add(c)
        if not choices:
            continue
        current_point = sorted(choices)[0]
        choices.remove(current_point)
        step.append(current_point)
    # return ''.join(step)
    return ''.join(nx.lexicographical_topological_sort(g))

def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Path order", f)
    print(f"guard id * minutes asleep:", g)
