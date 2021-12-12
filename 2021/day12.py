from copy import deepcopy

import networkx
import networkx as nx
from itertools import groupby
import matplotlib.pyplot as plt
TEST_STRING = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

TEST_STRING_2 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

REAL_STRING = """kc-qy
qy-FN
kc-ZP
end-FN
li-ZP
yc-start
end-qy
yc-ZP
wx-ZP
qy-li
yc-li
yc-wx
kc-FN
FN-li
li-wx
kc-wx
ZP-start
li-kc
qy-nv
ZP-qy
nv-xr
wx-start
end-nv
kc-nv
nv-XQ"""

def is_visitable(node,hubs,counter):
    return node in hubs or counter[node] ==0

def is_visitable_2(node,hubs,counter):
    vis = [v for h,v in counter.items() if h not in hubs and v >1]
    if len(vis) > 1:
        return False

    return node in hubs or counter[node] <2

def search(nodes,hubs,visit_counter,g, current_path, full_paths, vis_func):
    for node in nodes:

        if node == "end":
            full_paths.append(current_path + [node])
            continue
        # visit_counter = {n: 0 for n in g.nodes()}
        v = deepcopy(visit_counter)
        v[node] +=1
        valids = [n for n in g[node] if vis_func(n,hubs,v)]
        if not valids:
            continue
        search(valids,hubs,deepcopy(v),g, current_path + [node], full_paths, vis_func)


def main():
    part_1(REAL_STRING,is_visitable)
    part_1(REAL_STRING,is_visitable_2)

def part_1(s,vis_func):
    g= nx.Graph()
    for subs in s.split("\n"):
        u,v = subs.split("-")
        g.add_edge(u,v)

    hubs = [n for n in g.nodes if n.isupper()] + ["end"]

    points = list(g["start"])
    g.remove_node("start")
    full_paths=[]
    for node in points:
        if node == "end":
            continue
        current_path = ["start",node]
        visit_counter = {n: 0 for n in g.nodes()}
        visit_counter[node] +=1
        valids = {n for n in g[node] if vis_func(n,hubs,visit_counter)}
        if not valids:
            continue
        search(valids,hubs,deepcopy(visit_counter),g, current_path, full_paths, vis_func)

    for f in full_paths:
        print(f)

    print(len(full_paths))

    pass


if __name__ == '__main__':
    main()