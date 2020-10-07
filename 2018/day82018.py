import time

TESTSTRING = '''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'''
STRING = ''''''


def parse_string():
    with open('../inputs/input82018') as file:
        string = file.readline()

    string = string.split(' ')
    tree_nums = [int(s) for s in string]
    return tree_nums


class Node:
    def __init__(self, start_position, num_child_nodes, num_meta):
        self.start_position= start_position
        self.num_child_nodes = num_child_nodes
        self.num_meta_entries = num_meta
        self.meta_data = None
        self.child_node=[]

    @property
    def has_no_children(self):
        return self.num_child_nodes == 0

def get_node_from_header(idx,nums):
    return Node(idx, nums[idx],nums[idx+1])


def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]
        )





def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    total, value, remaining = parse(parse_string())
    # g = run2()
    print(time.time() - a)
    print('part 1:', total)
    print('part 2:', value)
