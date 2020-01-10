import time
from utils import open_file

day = 7
year = 2016

TESTSTRING = '''abba[mnop]qrst'''
TESTSTRING2 = '''aaaa[qwer]tyui'''
TESTSTRING3 = '''ioxxoj[asdfgh]zxcvbn'''
STRING = open_file(day, year)


def is_abba(w, x, y, z):
    return w != x and w + x == z + y


def has_aba(s):
    abas = set()
    for i in range(len(s) - 2):
        w, x, y = s[i:i + 3]
        if w == y and w != x:
            abas.add(x + w + x)
    return abas


def has_abba(s):
    for i in range(len(s) - 3):
        w, x, y, z = s[i:i + 4]
        if is_abba(w, x, y, z):
            return True
    return False


def run1():
    ips = []
    for s in STRING:
        a = False
        b = False

        subs = s.replace('[', ']').strip().split(']')
        for i in range(0, len(subs), 2):
            if has_abba(subs[i]):
                a = True
        for i in range(1, len(subs), 2):
            if has_abba(subs[i]):
                b = True
        if a and not b:
            ips.append(s)
    return len(ips)


def run2():
    ips = []
    for s in STRING:
        babs = set()

        subs = s.replace('[', ']').strip().split(']')
        hypernets = [subs[u] for u in range(1, len(subs), 2)]
        supernets = [subs[u] for u in range(0, len(subs), 2)]
        for net in supernets:
            babs |= has_aba(net)
        if not babs:
            continue

        for net in hypernets:
            for bab in babs:
                if bab in net:
                    ips.append(net)

    return len(set(ips))


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"Part 1", f)
    print(f"Part 2", g)

print(has_abba(TESTSTRING))
print(has_abba(TESTSTRING2))
print(has_abba(TESTSTRING3))
