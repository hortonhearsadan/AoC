import time

from computer import Computer

codes = [109, 424, 203, 1, 21101, 0, 11, 0, 1106, 0, 282, 21102, 18, 1, 0, 1106, 0, 259, 2101, 0, 1, 221, 203, 1, 21102,
         1, 31, 0, 1105, 1, 282, 21101, 0, 38, 0, 1106, 0, 259, 20102, 1, 23, 2, 22101, 0, 1, 3, 21102, 1, 1, 1, 21101,
         57, 0, 0, 1105, 1, 303, 2102, 1, 1, 222, 20101, 0, 221, 3, 21002, 221, 1, 2, 21101, 0, 259, 1, 21102, 1, 80, 0,
         1105, 1, 225, 21102, 125, 1, 2, 21102, 1, 91, 0, 1106, 0, 303, 2101, 0, 1, 223, 21002, 222, 1, 4, 21102, 1,
         259, 3, 21102, 225, 1, 2, 21102, 225, 1, 1, 21101, 0, 118, 0, 1106, 0, 225, 20102, 1, 222, 3, 21101, 0, 69, 2,
         21102, 1, 133, 0, 1106, 0, 303, 21202, 1, -1, 1, 22001, 223, 1, 1, 21102, 148, 1, 0, 1106, 0, 259, 1201, 1, 0,
         223, 20101, 0, 221, 4, 21001, 222, 0, 3, 21102, 1, 22, 2, 1001, 132, -2, 224, 1002, 224, 2, 224, 1001, 224, 3,
         224, 1002, 132, -1, 132, 1, 224, 132, 224, 21001, 224, 1, 1, 21102, 195, 1, 0, 106, 0, 108, 20207, 1, 223, 2,
         20101, 0, 23, 1, 21102, -1, 1, 3, 21101, 0, 214, 0, 1105, 1, 303, 22101, 1, 1, 1, 204, 1, 99, 0, 0, 0, 0, 109,
         5, 1202, -4, 1, 249, 21202, -3, 1, 1, 22102, 1, -2, 2, 21201, -1, 0, 3, 21101, 250, 0, 0, 1106, 0, 225, 22102,
         1, 1, -4, 109, -5, 2105, 1, 0, 109, 3, 22107, 0, -2, -1, 21202, -1, 2, -1, 21201, -1, -1, -1, 22202, -1, -2,
         -2, 109, -3, 2106, 0, 0, 109, 3, 21207, -2, 0, -1, 1206, -1, 294, 104, 0, 99, 22101, 0, -2, -2, 109, -3, 2106,
         0, 0, 109, 5, 22207, -3, -4, -1, 1206, -1, 346, 22201, -4, -3, -4, 21202, -3, -1, -1, 22201, -4, -1, 2, 21202,
         2, -1, -1, 22201, -4, -1, 1, 22102, 1, -2, 3, 21101, 0, 343, 0, 1106, 0, 303, 1105, 1, 415, 22207, -2, -3, -1,
         1206, -1, 387, 22201, -3, -2, -3, 21202, -2, -1, -1, 22201, -3, -1, 3, 21202, 3, -1, -1, 22201, -3, -1, 2,
         22102, 1, -4, 1, 21101, 384, 0, 0, 1106, 0, 303, 1106, 0, 415, 21202, -4, -1, -4, 22201, -4, -3, -4, 22202, -3,
         -2, -2, 22202, -2, -4, -4, 22202, -3, -2, -3, 21202, -4, -1, -2, 22201, -3, -2, 1, 21202, 1, 1, -4, 109, -5,
         2105, 1, 0]
STRING = ''''''

TEST_STRING = ''''''
TEST_STRING2 = ''''''
TEST_STRING3 = ''''''


class TractorBeam:
    def __init__(self):
        self.cpu = None
        self.map = None


def run1():
    t = TractorBeam()
    t.cpu = Computer(codes)
    points = {}
    beam_start = {0: 0}
    beam_end = {}
    for y in range(50):
        passed_beam = False
        in_beam = False
        for x in range(0, 50):
            t.cpu.add_inputs([x, y])
            output = t.cpu.program(reset=True)
            if output == 1:
                if not in_beam:
                    in_beam = True
                    beam_start[y] = x
            elif output == 0:
                if in_beam:
                    beam_end[y] = x
                    break
            points[complex(x, y)] = output
            # t.cpu = Computer(codes)

    # draw = [[" " for x in range(50)] for y in range(50)]
    # for p, i in points.items():
    #     draw[int(p.imag)][int(p.real)] = '#' if i == 1 else " "
    # [print(''.join(x for x in y)) for y in draw]
    return len([p for p in points.values() if p == 1])


def run2():
    t = TractorBeam()
    t.cpu = Computer(codes)
    beam_start = {0: 0}
    beam_end = {}
    size = 100
    width = 0
    y = 10
    x = 0
    while width < 100:
        in_beam = False
        start = beam_start.get(y - 1, 0)
        x = start
        while True:
            t.cpu.add_inputs([x, y])

            output = t.cpu.program(reset=True)
            if output == 1:
                if not in_beam:
                    in_beam = True
                    beam_start[y] = x
                    x = beam_end.get(y - 1, x + 1)
                else:
                    x += 1
            elif output == 0:
                if in_beam:
                    beam_end[y] = x
                    break
                else:
                    x += 1
        if y > 200:
            if abs(beam_start[y] - beam_end[y - size + 1]) >= size:
                coord = complex(beam_start[y], y - size + 1)
                return int(coord.real * 10000 + coord.imag)
        y += 1

    # draw = [[" " for x in range(50)] for y in range(50)]
    # for p, i in points.items():
    #     draw[int(p.imag)][int(p.real)] = '#' if i == 1 else " "
    # [print(''.join(x for x in y)) for y in draw]


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part2:", g)
    print(time.time() - start_time)
