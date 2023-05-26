# level 4-6 fanout 4-6
import random
from datetime import datetime

level_min = 4
level_max = 6
fanout_min = 4
fanout_max = 6
op_max = 10


# generateTree(levelMin, levelMax, parent, fanoutMin, fanoutMax):
#   n = generate_node(...)
#   if parent:
#     print(f"{parent} - {n}")
#   if randrange(levelMin, levelMax) > 0: 
#     fanout = randrange(fanoutMin, fanoutMax)
#     for i in range(0, fanout):
#         generateTree(levelMin - 1, levelMax - 1, n, , fanoutMin, fanoutMax);

def generate_tree(levelMin, levelMax, parent, fanoutMin, fanoutMax, name_prefix, file, global_count):
    random.seed(datetime.now().timestamp())
    n = name_prefix + str(global_count)
    if parent:
        file.write(f"{parent} {n}\n")
    if random.randrange(levelMin, levelMax) > 0: 
        fanout = random.randrange(fanoutMin, fanoutMax)
        for i in range(0, fanout):
            global_count = generate_tree(levelMin - 1, levelMax - 1, n, fanoutMin, fanoutMax, name_prefix, file, global_count+1)
    return global_count




file = open("random_init.txt", "w")

admin_count = generate_tree(level_min, level_max, "Admin_0", fanout_min, fanout_max, "Admin_", file, 1)
incident_count = generate_tree(level_min, level_max, "Incident_0", fanout_min, fanout_max, "Incident_", file, 1)

file.close()

random.seed(datetime.now().timestamp())
op_count = random.randrange(1, op_max+1)

file = open("random_update.txt", "w")
for i in range(op_count):

    
    admin_random = random.randrange(admin_count)
    incident_random = random.randrange(incident_count)

    admin_node = "Admin_" + str(admin_random)
    incident_node = "Incident_" + str(incident_random)
    if i%2 == 0:
        file.write("add " + incident_node + " " + admin_node + "\n")
    else:
        file.write("del " + incident_node + " " + admin_node + "\n")
    
file.close()