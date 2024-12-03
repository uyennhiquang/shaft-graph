"""
The staff graph generates a graph whose vertices are the major roles staff of a show and edges where two vertices are adjacent if the staffs worked on the same show.

To generate such a graph, the script iterates over a list of anime. For simplicity's sake, let us first make a basic graph (using the laymen term) where the vertex is simply the name of the staff. Each anime object contains the show's title and an array of staffs. The easiest way to collect all the staff's objects whose roles are among the major roles is to iterate over the staff's positions array, and stop iterating if the current staff's position is among the major roles. We will then gather all of the staff objects into a list (which is practically the vertex set of that clique), then iterate over that list and add the members to our multigraph, and connect them with an edge whose label is the title of the current anime. (please do not think about the time complexity of this algorithm)
"""
import networkx as nx
import json
import itertools as it
import matplotlib.pyplot as plt
from pyvis.network import Network

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
                print(name)
                break

    for i in range(len(major_staffs)):
        for j in range(len(major_staffs)):
            staff1_name = major_staffs[i]["person"]["name"]
            staff2_name = major_staffs[j]["person"]["name"]

            SHAFT.add_edge(staff1_name, staff2_name, label=one_show["title"])
    # show_count += 1
# print(major_staffs)

# nx.draw_circular(SHAFT, with_labels=True)
# ax = plt.gca()
# ax.margins(0.10)
# draw_labeled_multigraph(SHAFT, "label", ax)
# plt.show()

""" 
Credit to https://perplexity.ai
"""


def visualize_graph(G, output_file='graph_visualization.html'):
    net = Network(notebook=True, height="750px", width="100%",
                  bgcolor="#222222", font_color="white")
    net.from_nx(G)

    # Customize node appearance
    for node in net.nodes:
        node['color'] = '#6ECCAF'
        node['size'] = 20  # Reduced size
        node['shape'] = 'image'
        node['image'] = G.nodes[node['id']]['image']
        if 'title' in node:
            # Styled hover text
            node['title'] = f"<div style='font-size:14px;'>{node['title']}</div>"
            # node['label'] = ''  # Remove labels from nodes

    # Customize edge appearance
    for edge in net.edges:
        edge['color'] = '#EEEEEE'
        edge['width'] = 1  # Thinner edges
        if 'label' in edge:
            edge['title'] = edge['label']  # Move edge label to hover text
            del edge['label']  # Remove visible edge label

    # Set physics layout
    net.set_options('''
    var options = {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -50,
          "centralGravity": 0.01,
          "springLength": 100,
          "springConstant": 0.08
        },
        "maxVelocity": 50,
        "solver": "forceAtlas2Based",
        "timestep": 0.35,
        "stabilization": {"iterations": 150}
      },
      "interaction": {
        "hover": true,
        "tooltipDelay": 300
      }
    }
    ''')

    net.show(output_file)


# Example usage
# Assuming you have a NetworkX graph named 'G'
# G = your_existing_networkx_graph
visualize_graph(SHAFT)
