"""
Read make_staff_graph_str.py for algorithm for making these graphs
"""
import networkx as nx
import json
import itertools as it
import matplotlib.pyplot as plt
from pyvis.network import Network


file = "./va_obj.json"
with open(file, 'r') as f:
    data = json.load(f)

shows = data["shows"]
# one_show = shows[0]


show_count = 0
max_shows = 30
SHAFT = nx.MultiGraph()
for one_show in shows:
  if show_count > max_shows:
    break
  voice_actors = []
  va_counter = 0
  max_va = 10
  for char in one_show["chars"]:
    if va_counter > max_va:
      break
    for voice_actor in char["voice_actors"]:
      if voice_actor["language"] != "Japanese":
        continue
      else:
        voice_actors.append(voice_actor) 
        name = voice_actor["person"]["name"]
        SHAFT.add_node(
          name, image=voice_actor["person"]["images"]["jpg"]["image_url"])
        break
    
    va_counter += 1

  for i in range(len(voice_actors)):
      for j in range(len(voice_actors)):
          va1_name = voice_actors[i]["person"]["name"]
          va2_name = voice_actors[j]["person"]["name"]

          SHAFT.add_edge(va1_name, va2_name, label=one_show["title"])
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
    net = Network(notebook=True, height="750px", width="100%", bgcolor="#222222", font_color="white")
    net.from_nx(G)

    # Customize node appearance
    for node in net.nodes:
        node['color'] = '#6ECCAF'
        node['size'] = 20  # Reduced size
        node['shape'] = 'image'
        node['image'] = G.nodes[node['id']]['image']
        if 'title' in node:
            node['title'] = f"<div style='font-size:14px;'>{node['title']}</div>"  # Styled hover text
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
visualize_graph(SHAFT)
