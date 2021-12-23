import math
import time
from collections import deque, Counter, defaultdict
from itertools import combinations

import numpy as np
from scipy.spatial.transform import Rotation
from utils import open_file

filename = "C:\\Users\\danie\\PycharmProjects\\aoc-rs\\input\\y21d19.txt"
TESTSTRING = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""

rotations= [
    Rotation.from_euler('YX', [90, 0], degrees=True),
    Rotation.from_euler('YX', [90, 90], degrees=True),
    Rotation.from_euler('YX', [90, 180], degrees=True),
    Rotation.from_euler('YX', [90, 270], degrees=True),
    Rotation.from_euler('YX', [270, 0], degrees=True),
    Rotation.from_euler('YX', [270, 90], degrees=True),
    Rotation.from_euler('YX', [270, 180], degrees=True),
    Rotation.from_euler('YX', [270, 270], degrees=True),
    Rotation.from_euler('ZX', [0, 0], degrees=True),
    Rotation.from_euler('ZX', [0, 90], degrees=True),
    Rotation.from_euler('ZX', [0, 180], degrees=True),
    Rotation.from_euler('ZX', [0, 270], degrees=True),
    Rotation.from_euler('ZX', [90, 0], degrees=True),
    Rotation.from_euler('ZX', [90, 90], degrees=True),
    Rotation.from_euler('ZX', [90, 180], degrees=True),
    Rotation.from_euler('ZX', [90, 270], degrees=True),
    Rotation.from_euler('ZX', [180, 0], degrees=True),
    Rotation.from_euler('ZX', [180, 90], degrees=True),
    Rotation.from_euler('ZX', [180, 180], degrees=True),
    Rotation.from_euler('ZX', [180, 270], degrees=True),
    Rotation.from_euler('ZX', [270, 0], degrees=True),
    Rotation.from_euler('ZX', [270, 90], degrees=True),
    Rotation.from_euler('ZX', [270, 180], degrees=True),
    Rotation.from_euler('ZX', [270, 270], degrees=True),
    ]

class Scanner:
    def __init__(self,beacons):
        self.beacons = beacons
        self.position = None


def parse_input():
    inputs =[]
    with open(filename, 'r') as f:
        string = f.readlines()
    # string = TESTSTRING.splitlines()
    beacons=[]
    for line in string:
        if '---' in line:
            beacons =[]
        elif line == '\n' or line == '':
            inputs.append(Scanner(beacons))
            beacons = []
        else:
            point =np.array([int(p.strip()) for p in line.split(',')])
            beacons.append(point)
    if beacons:

        inputs.append(Scanner(beacons))
    return inputs

def run1(data):
    known_beacons = set(tuple(p) for p in data[0].beacons)
    data[0].position = np.array([0,0,0])

    remaining_scanners = deque(data[1:])

    while remaining_scanners:
        scanner = remaining_scanners.pop()
        match=False
        for rotated_beacons in rotate_scanner(scanner):
            c = defaultdict(int)
            for b in known_beacons:
                for r in rotated_beacons:
                    c[tuple(r - b)] +=1

            offset = max(c,key=c.get)
            count = c[offset]
            if count >= 12:
                known_beacons |= set(tuple(r - offset) for r in rotated_beacons)
                scanner.position = np.array(offset)
                match=True
                break
        if not match:
            remaining_scanners.appendleft(scanner)

    positions = [s.position for s in data]
    max_dist = max(np.abs(s1-s2).sum() for s1,s2 in combinations(positions,2))
    return len(known_beacons), int(max_dist)


def run2(data):
    pass


def rotate_scanner(scanner):
    scanner_rotations = []
    for rotation in rotations:
        s = np.round(rotation.apply(scanner.beacons))
        scanner_rotations.append(s)
    return scanner_rotations

if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f,g = run1(inputs)
    # g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
