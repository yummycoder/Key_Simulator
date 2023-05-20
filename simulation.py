import argparse

class Name:

    def __init__(self, name):
        self.name = name
        self.ancestor = set()
        self.successor = set()
    
    # def __repr__(self):
    #     return self.name
    
    def add_ancestor(self, ancestor):
        self.ancestor.add(ancestor)

    def add_successor(self, successor):
        self.successor.add(successor)
    
    def del_ancestor(self, ancestor):
        if ancestor in self.ancestor:
            self.ancestor.remove(ancestor)

    def del_successor(self, successor):
        if successor in self.successor:
            self.successor.remove(successor)
    
    def print_ancestor(self):
        print(self.ancestor)

    def print_successor(self):
        print(self.successor)


POISE = dict()

def add(node1, node2):
    if node1 not in POISE:
        POISE[node1] = Name(node1)
    if node2 not in POISE:
        POISE[node2] = Name(node2)
    POISE[node1].add_successor(node2)
    POISE[node2].add_ancestor(node1)

def delete(node1, node2):
    POISE[node1].del_successor(node2)
    POISE[node2].del_ancestor(node1)
    # for ancesstor in POISE[node1].ancestor:
    #     POISE[ancesstor].del_successor(node1)
    # for successor in POISE[node1].successor:
    #     POISE[successor].del_ancestor(node1)
    # del POISE[node1]

    

parser = argparse.ArgumentParser()
parser.add_argument("init", type=str)
parser.add_argument("-op", dest="opreation", type=str)
# parser.add_argument("-r", dest="removeFile", type=argparse.FileType('r'))
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
    
    POISE[names[0]].add_successor(names[1])
    POISE[names[1]].add_ancestor(names[0])


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

# output result
for key in POISE:
    print(key)
    print("ancestor")
    POISE[key].print_ancestor()
    print("successor")
    POISE[key].print_successor()
    print("\n")

