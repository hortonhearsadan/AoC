import string
import time
from utils import open_file

day = 4
year = 2020

TESTSTRING = """"""
STRING = """"""

fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}

eye_colours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def is_valid(self):
        return (
            self.byr_is_valid()
            and self.iyr_is_valid()
            and self.eyr_is_valid()
            and self.hgt_is_valid()
            and self.hcl_is_valid()
            and self.ecl_is_valid()
            and self.pid_is_valid()
        )

    def byr_is_valid(self):
        return number_range_validation(1920, 2002, int, self.byr)

    def iyr_is_valid(self):
        return number_range_validation(2010, 2020, int, self.iyr)

    def eyr_is_valid(self):
        return number_range_validation(2020, 2030, int, self.eyr)

    def hgt_is_valid(self):
        unit = self.hgt[-2:]
        if unit == "cm":
            return number_range_validation(150, 193, float, self.hgt[:-2])
        elif unit == "in":
            return number_range_validation(59, 76, float, self.hgt[:-2])

        return False

    def hcl_is_valid(self):
        if not self.hcl[0] == "#":
            return False
        if len(self.hcl) != 7:
            return False

        return all(c in string.hexdigits for c in self.hcl[1:])

    def ecl_is_valid(self):
        return self.ecl in eye_colours

    def pid_is_valid(self):
        return len(self.pid) == 9 and self.pid.isdigit()

    @classmethod
    def from_dict(cls, pp_dict):
        return Passport(
            byr=pp_dict["byr"],
            iyr=pp_dict["iyr"],
            eyr=pp_dict["eyr"],
            hgt=pp_dict["hgt"],
            hcl=pp_dict["hcl"],
            ecl=pp_dict["ecl"],
            pid=pp_dict["pid"],
            cid=pp_dict.get("cid"),
        )


def number_range_validation(lower, upper, type_, number):
    try:
        v = lower <= type_(number) <= upper
    except:
        v = False

    return v


def parse_input():
    with open(f"../inputs/input{day}{year}") as f:
        strings = f.read()
    strings = strings.split("\n\n")
    for i, s in enumerate(strings):
        strings[i] = s.replace("\n", ",").replace(" ", ",")
    return strings


def run1(inputs):
    valid_passports = []
    for i in inputs:
        invalid = False
        for f in fields:
            if not f + ":" in i:
                invalid = True
                break
        if invalid:
            continue
        pp_dict = {}
        for j in i.split(","):
            if j == "":
                continue
            k, v = j.split(":")
            pp_dict[k] = v
        valid_passports.append(Passport.from_dict(pp_dict))

    return valid_passports


def run2(passports: [Passport]):
    return sum(p.is_valid() for p in passports)


if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(f)
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
    print(f"Part 1: {len(f)}")
    print(f"Part 2: {g}")
