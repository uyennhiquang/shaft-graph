"""
Prints the degree of each staff. Note that every time an edge would connect staffs there are also loops for each staff.
"""
import networkx as nx
import json

file = "./new_shows_obj.json"
with open(file, 'r') as f:
    data = json.load(f)

shows = data["shows"]
# one_show = shows[0]

major_positions = ["Director", "Music", "Character Design"]

show_count = 0
max_shows = 1
SHAFT = nx.MultiGraph()
for one_show in shows:
    if show_count > max_shows:
        break
    major_staffs = []
    for staff in one_show["staffs"]:
        for position in staff["positions"]:
            if position in major_positions:
                major_staffs.append(staff)
                name = staff["person"]["name"]
                SHAFT.add_node(
                    name, image=staff["person"]["images"]["jpg"]["image_url"])
                # print(name)
                break

    for i in range(len(major_staffs)):
        for j in range(len(major_staffs)):
            staff1_name = major_staffs[i]["person"]["name"]
            staff2_name = major_staffs[j]["person"]["name"]

            SHAFT.add_edge(staff1_name, staff2_name, label=one_show["title"])
    # show_count += 1
# print(major_staffs)

sorted_degree_list = sorted(SHAFT.degree, key=lambda tuple: tuple[1], reverse=True)
staff_count = 0
for staff_tuple in sorted_degree_list:
    # print(staff_tuple) # Prints the degree counting the loops
    print((staff_tuple[0], int(staff_tuple[1]/2))) # Prints the degree not counting loops
    staff_count += 1
print("Staff count: ", staff_count)