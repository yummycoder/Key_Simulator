# level 4-6 fanout 4-6
import random
from datetime import datetime

level_min = 4
level_max = 6
fanout_min = 4
fanout_max = 6
op_max = 10

def generate_tree(level, name, root, file):
    global_count = 0
    level_stack = []
    next_stack = []
    level_stack.append(root)

    for i in range(level):
        while len(level_stack) != 0 :
            node = level_stack.pop()
            for j in range(random.randrange(fanout_min, fanout_max+1)):
                global_count = global_count + 1
                node_name = name + "_" + str(global_count)
                file.write(node + " " + node_name + "\n")
                next_stack.append(node_name)

        level_stack = next_stack
        next_stack = []
    
    return global_count


random.seed(datetime.now().timestamp())



admin_root = "Admin_0"
incident_root = "Incident_0"

file = open("random_init.txt", "w")

admin_count = generate_tree(random.randrange(level_min,level_max+1), "Admin", admin_root, file)
incident_count = generate_tree(random.randrange(level_min,level_max+1), "Incident", incident_root, file)

file.close()

op_count = random.randrange(1, op_max+1)

file = open("random_update.txt", "w")
for i in range(op_count):

    admin_random = random.randrange(admin_count)
    incident_random = random.randrange(incident_count)

    admin_node = "Admin_" + str(admin_random)
    incident_node = "Incident_" + str(incident_random)
    file.write("add " + incident_node + " " + admin_node + "\n")
    file.write("del " + incident_node + " " + admin_node + "\n")
    
file.close()