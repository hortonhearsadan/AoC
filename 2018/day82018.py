import time

TESTSTRING = '''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'''
STRING = ''''''


def parse_string():
    with open('../inputs/input82018') as file:
        string = file.readline()

    string = string.split(' ')
    tree_nums = list(string)
    return tree_nums


class Node:
    def __init__(self, num_child_nodes, num_meta):
        self.num_child_nodes = num_child_nodes
        self.num_meta_entries = num_meta
        self.meta_data = None


def run1():
    nums = parse_string()
    header_index = 0

    root_node = Node(nums[header_index], nums[header_index + 1])
    meta_data_index = - root_node.num_meta_entries
    root_node.meta_data = nums[- root_node.num_meta_entries:]
    


def run2():
    pass


if __name__ == "__main__":
    a = time.time()
    f = run1()
    g = run2()
    print(time.time() - a)
    print(f"sleepiest_guard id * minutes asleep", f)
    print(f"guard id * minutes asleep:", g)
