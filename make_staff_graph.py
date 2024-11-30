""" 
The staff graph generates a graph whose vertices are the major roles staff of a show and edges where two vertices are adjacent if the staffs worked on the same show.

To generate such a graph, the script iterates over a list of anime. For simplicity's sake, let us first make a basic graph (using the laymen term) where the vertex is simply the name of the staff. Each anime object contains the show's title and an array of staffs. The easiest way to collect all the staff's objects whose roles are among the major roles is to iterate over the staff's positions array, and stop iterating if the current staff's position is among the major roles. We will then gather all of the staff objects into a list (which is practically the vertex set of that clique), then iterate over that list and add the members to our multigraph, and connect them with an edge whose label is the title of the current anime. (please do not think about the time complexity of this algorithm)
"""
import networkx as nx
import json

file = "./new_shows_obj.json"
with open(file, 'r') as f:
  data = json.load(f)

shows = data["shows"]
one_show = shows[0]

major_positions = ["Director", "Music", "Character Design"]

# G = nx.MultiGraph()

major_staffs = []
for staff in one_show["staffs"]:
  for position in staff["positions"]:
    if position in major_positions:
      major_staffs.append(staff)
      print(staff["person"]["name"])
      break
  

# print(major_staffs)

  





