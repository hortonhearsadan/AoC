import time
from utils import open_file
import numpy as np
import networkx as nx
import scipy as sp

dir_path = __file__.split('/')
day = int(dir_path[-1][3:-3])
year = int(dir_path[-2])

TESTSTRING = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''
STRING = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''


class Mask:
    def __init__(self, mask):
        self.mask = mask
        self.mems=[]

class MemAdd:
    def __init__(self,loc,bit):
        self.bit = bit

        self.loc = loc

def bitify(i):
    return bin(int(i))[2:].zfill(36)

def parse_input():
    f = open_file(day,year)
    f=TESTSTRING.split('\n')
    f=STRING.split('\n')
    inputs=[]
    instr=None
    for m in f:
        if 'mask' in m:
            if instr:
                inputs.append(instr)
            instr = Mask(m[6:].strip())
        elif 'mem' in m:
            loc,bit = m[4:].strip().split(' = ')
            loc =int(loc[:-1])
            bit = bitify(bit)
            instr.mems.append(MemAdd(loc,bit))
    inputs.append(instr)

    return inputs


def add_mask(value, mask):
    r = list(value)
    for i,m in enumerate(mask):
        if m in {'1','0'}:
            r[i]=m
    return ''.join(r)



def run1(data):
    mem={}
    for d in data:
        mask = d.mask
        for memadd in d.mems:
            value = memadd.bit
            result = add_mask(value,mask)
            mem[memadd.loc] = int(result,2)
    return sum(mem.values())


def add_mask_2(addr,mask):
    locs=[]
    r = list(addr)
    for i,m in enumerate(mask):
        if m in {'1','X'}:
            r[i]=m

    for i,b in enumerate(r):
        if b =='X':
            locs.append(r[:i]+['1']+r[i+1:])
            locs.append(r[:i]+['0']+r[i+1:])
    return [''.join(l) for l in locs]



def run2(data):
    mem={}
    for d in data:
        mask = d.mask
        for memadd in d.mems:
            value = memadd.bit
            result = add_mask(value,mask)

            locs = add_mask_2(bitify(memadd.loc),mask)
            for l in locs:
                mem[int(l,2)]=int(result,2)
            # mem[memadd.loc] = int(result,2)
    return sum(mem.values())



if __name__ == "__main__":
    a = time.time()
    inputs = parse_input()
    f = run1(inputs)
    g = run2(inputs)
    print(f"Part 1: {f}")
    print(f"Part 2: {g}")
    print(f"Runtime: {round((time.time() - a)*1000,3)}ms")
