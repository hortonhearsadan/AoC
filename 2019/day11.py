import time
from enum import IntEnum, Enum
from computer import Computer

codes = [3, 8, 1005, 8, 318, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008,
         8, 1, 10, 4, 10, 101, 0, 8, 29, 1, 107, 12, 10, 2, 1003, 8, 10, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10,
         1008, 8, 0, 10, 4, 10, 1002, 8, 1, 59, 1, 108, 18, 10, 2, 6, 7, 10, 2, 1006, 3, 10, 3, 8, 1002, 8, -1, 10,
         1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 1002, 8, 1, 93, 1, 1102, 11, 10, 3, 8, 102, -1, 8, 10, 1001, 10,
         1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 101, 0, 8, 118, 2, 1102, 10, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4,
         10, 1008, 8, 0, 10, 4, 10, 101, 0, 8, 145, 1006, 0, 17, 1006, 0, 67, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4,
         10, 1008, 8, 0, 10, 4, 10, 101, 0, 8, 173, 2, 1109, 4, 10, 1006, 0, 20, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10,
         4, 10, 108, 0, 8, 10, 4, 10, 102, 1, 8, 201, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4,
         10, 1002, 8, 1, 224, 1006, 0, 6, 1, 1008, 17, 10, 2, 101, 5, 10, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10,
         108, 1, 8, 10, 4, 10, 1001, 8, 0, 256, 2, 1107, 7, 10, 1, 2, 4, 10, 2, 2, 12, 10, 1006, 0, 82, 3, 8, 1002, 8,
         -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 1002, 8, 1, 294, 2, 1107, 2, 10, 101, 1, 9, 9, 1007, 9,
         988, 10, 1005, 10, 15, 99, 109, 640, 104, 0, 104, 1, 21102, 1, 837548352256, 1, 21102, 335, 1, 0, 1105, 1, 439,
         21102, 1, 47677543180, 1, 21102, 346, 1, 0, 1106, 0, 439, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10,
         104, 0, 104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 21102, 1, 235190374592, 1,
         21101, 393, 0, 0, 1105, 1, 439, 21102, 3451060455, 1, 1, 21102, 404, 1, 0, 1105, 1, 439, 3, 10, 104, 0, 104, 0,
         3, 10, 104, 0, 104, 0, 21102, 837896909668, 1, 1, 21102, 1, 427, 0, 1105, 1, 439, 21102, 1, 709580555020, 1,
         21102, 438, 1, 0, 1105, 1, 439, 99, 109, 2, 21201, -1, 0, 1, 21102, 1, 40, 2, 21102, 1, 470, 3, 21102, 460, 1,
         0, 1106, 0, 503, 109, -2, 2105, 1, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 465, 466, 481, 4, 0, 1001,
         465, 1, 465, 108, 4, 465, 10, 1006, 10, 497, 1101, 0, 0, 465, 109, -2, 2105, 1, 0, 0, 109, 4, 1201, -1, 0, 502,
         1207, -3, 0, 10, 1006, 10, 520, 21101, 0, 0, -3, 21202, -3, 1, 1, 22101, 0, -2, 2, 21101, 1, 0, 3, 21101, 0,
         539, 0, 1106, 0, 544, 109, -4, 2105, 1, 0, 109, 5, 1207, -3, 1, 10, 1006, 10, 567, 2207, -4, -2, 10, 1006, 10,
         567, 21202, -4, 1, -4, 1105, 1, 635, 22101, 0, -4, 1, 21201, -3, -1, 2, 21202, -2, 2, 3, 21101, 0, 586, 0,
         1105, 1, 544, 22102, 1, 1, -4, 21102, 1, 1, -1, 2207, -4, -2, 10, 1006, 10, 605, 21102, 1, 0, -1, 22202, -2,
         -1, -2, 2107, 0, -3, 10, 1006, 10, 627, 21202, -1, 1, 1, 21101, 627, 0, 0, 105, 1, 502, 21202, -2, -1, -2,
         22201, -4, -2, -4, 109, -5, 2105, 1, 0]
TEST_STRING = ''''''
TEST_STRING2 = ''''''
TEST_STRING3 = ''''''


class PanelColour(IntEnum):
    Black = 0
    White = 1


class PanelPaint(Enum):
    Black = ' '
    White = '#'


class TurnDirection(IntEnum):
    Left = 0
    Right = 1



class Robot:
    def __init__(self):
        self.brain = None
        self.direction = None
        self.position = None


def get_facing_direction(direction, turn_direction):
    if turn_direction == TurnDirection.Left:
        return direction * 1j
    if turn_direction == TurnDirection.Right:
        return direction * -1j


def move_to_new_position(position, direction):
    return position + direction


def paint(robot):
    painting = {}

    while not robot.brain.halted:
        colour, turn_direction = (robot.brain.outputs[-2], robot.brain.outputs[-1])
        painting[robot.position] = PanelColour(colour)
        robot.direction = get_facing_direction(robot.direction, turn_direction)
        robot.position = move_to_new_position(robot.position, robot.direction)
        position_colour = painting.get(robot.position, PanelColour.Black)
        robot.brain.add_input(position_colour)
        robot.brain.program()
    return painting


def run1():
    position_colour = PanelColour.Black
    robot = Robot()
    robot.position = complex(0)
    robot.brain = Computer(codes)
    robot.direction = 1j
    robot.brain.add_input(position_colour)
    robot.brain.program()

    painting = paint(robot)
    return len(painting.keys())


def visualise(painting):
    keys = painting.keys()
    x_s = [p.real for p in keys]
    y_s = [p.imag for p in keys]
    x_max = int(max(x_s))
    y_min = int(min(y_s))

    tmp = [[" "] * (x_max + 1) for _ in range(abs(y_min) + 1)]
    for i, j in painting.items():
        x = int(i.real)
        y = int(-i.imag)
        tmp[y][x] = PanelPaint.White.value if j == PanelColour.White else PanelPaint.Black.value
    return tmp


def run2():
    position_colour = PanelColour.White
    robot = Robot()
    robot.position = complex(0)
    robot.brain = Computer(codes)
    robot.direction = 1j
    robot.brain.add_input(position_colour)
    output = robot.brain.program()

    painting = paint(robot)
    p = visualise(painting)
    return p


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part2:")
    [print((" ".join(x))) for x in g]
    print(time.time() - start_time)
