import time
from utils import open_file

day = 2
year = 2015

TESTSTRING = ''''''
STRING = ''''''


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    @property
    def smallest_side(self):
        sides = [self.length * self.width, self.length * self.height, self.width * self.height]
        return min(sides)

    def get_wrapping_paper_amount(self):
        return self.surface_area + self.smallest_side

    @property
    def smallest_perimeter(self):
        perims = [2*(self.length + self.width), 2*(self.length+self.height), 2*(self.height + self.width)]
        return min(perims)

    @property
    def volume(self):
        return self.length * self.width * self.height

    def get_ribbon_amount(self):
        return self.smallest_perimeter + self.volume

def parse_string_into_boxes(boxes):
    _boxes =[]
    for b in boxes:
        b = b.replace('\n','').split('x')
        dims = [int(d) for d in b]
        _boxes.append(Box(*dims))
    return _boxes

def run1():
    boxes = open_file(day,year)
    boxes = parse_string_into_boxes(boxes)
    return sum(b.get_wrapping_paper_amount() for b in boxes)

def run2():
    boxes = open_file(day, year)
    boxes = parse_string_into_boxes(boxes)
    return sum(b.get_ribbon_amount() for b in boxes)


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)
