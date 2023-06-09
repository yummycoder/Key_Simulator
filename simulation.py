import argparse
# import pdb; pdb.set_trace()

class Name:

    def __init__(self, name):
        self.name = name
        self.parent = set()
        self.child = set()
    
    def __repr__(self):
        return self.name
    
    def add_parent(self, parent):
        self.parent.add(parent)

    def add_child(self, child):
        self.child.add(child)
    
    def del_parent(self, parent):
        if parent in self.parent:
            self.parent.remove(parent)

    def del_child(self, child):
        if child in self.child:
            self.child.remove(child)

    def get_parent(self):
        return self.parent

    def get_child(self):
        return self.child
    
    def print_parent(self):
        print(self.parent)

    def print_child(self):
        print(self.child)


POISE = dict()

def add(node1, node2):
    if node1 not in POISE:
        POISE[node1] = Name(node1)
    if node2 not in POISE:
        POISE[node2] = Name(node2)
    POISE[node1].add_child(node2)
    POISE[node2].add_parent(node1)

def delete(node1, node2):
    POISE[node1].del_child(node2)
    POISE[node2].del_parent(node1)

def calculate_ancestor():
    ancestor_init = {}
    for key in POISE:
        ancestor_init[key] = set()

    visited = set()
    def cal_ance(key):
        if key in visited:
            return ancestor_init[key]
        else:
            visited.add(key)
        if len(POISE[key].get_parent()) == 0:
            return {key}
        else:
            parents = list(POISE[key].get_parent())
            ancestor_init[key] = ancestor_init[key].union(POISE[key].get_parent())
            for parent in parents:
                ancestor = cal_ance(parent)
                ancestor_init[key] = ancestor_init[key].union(ancestor)
            return ancestor_init[key]


    for key in POISE:
        if len(POISE[key].get_child()) == 0:
            cal_ance(key)
        else:
            continue

    return ancestor_init
    

def cal_size(ances_init, ances_change, kp_size, cp_size, pke_size, name_size):
    for key in ances_init:
        if (ances_init[key] != ances_change[key]):
            print(key,": ")
            print("Key-Oriented: ")
            print("KP-ABE attributes in new key: ", len(ances_change[key])+1, " key size: ", kp_size[len(ances_change[key])+1], "KB")
            print("CP-ABE attributes in new key: ", len(ances_change[key])+1, " key size: ", cp_size[len(ances_change[key])+1], "KB")
            delete = len(ances_init[key] - ances_change[key])
            add = len(ances_change[key] - ances_init[key])
            print("ME-PKE key delete: ", delete, " key size: ", name_size*delete, "KB")
            print("ME-PKE key add: ", add, " key size: ", pke_size[add], "KB")
            print("\n")

def load_data(path, result):
    file = open(path, "r")
    lines = file.read().splitlines()
    for line in lines:
        if line.startswith("#"):
            continue
        word = line.split('\t')
        num = int(word[0])
        value = float(word[1])
        result.append(value)

# main
parser = argparse.ArgumentParser()
parser.add_argument("init", type=str)
parser.add_argument("-op", dest="opreation", type=str)
args = parser.parse_args()

init_file = args.init
init = open(init_file, "r")
lines = init.read().splitlines()
for line in lines:
    names = line.split(' ')
    if names[0] not in POISE:
        POISE[names[0]] = Name(names[0])
    if names[1] not in POISE:
        POISE[names[1]] = Name(names[1])
    
    POISE[names[0]].add_child(names[1])
    POISE[names[1]].add_parent(names[0])



# calculate ancestor
ances_init = calculate_ancestor()


op_file = args.opreation
op = open(op_file, "r")
lines = op.read().splitlines()
for line in lines:
    word = line.split(' ')
    op = word[0]
    if op == "add":
        add(word[1], word[2])

    elif op == "del":
        delete(word[1], word[2])




# load key size data
kp_path = "./key_size_kp.txt"
cp_path = "./key_size_cp.txt"
pke_path = "./key_size_pke.txt"
kp_size = [0]
cp_size = [0]
pke_size = [0]
load_data(kp_path, kp_size)
load_data(cp_path, cp_size)
load_data(pke_path, pke_size)


# for key in POISE:
#     print(POISE[key])

# calculate ancestor
ances_change = calculate_ancestor()

name_size = 0.016
cal_size(ances_init, ances_change, kp_size, cp_size, pke_size, name_size)

# output result
# for key in POISE:
#     print(key)
#     print("parent")
#     POISE[key].print_parent()
#     print("child")
#     POISE[key].print_child()
#     print("\n")

