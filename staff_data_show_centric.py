"""
Prints the degree of each staff. This will only care whether two staffs worked on a show before, regardless of how many times they've worked together
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
SHAFT = nx.Graph()
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
            if i == j:
                continue
            staff1_name = major_staffs[i]["person"]["name"]
            staff2_name = major_staffs[j]["person"]["name"]

            SHAFT.add_edge(staff1_name, staff2_name, label=one_show["title"])
    # show_count += 1
# print(major_staffs)

sorted_degree_list = sorted(SHAFT.degree, key=lambda tuple: tuple[1], reverse=True)
staff_count = 0

with open("./graphs/top_staff.txt", "w") as f:
    for staff_tuple in sorted_degree_list:
        print(staff_tuple)
        f.write(staff_tuple.__str__())
        f.write("\n")
        staff_count += 1
    print("Staff count: ", staff_count)