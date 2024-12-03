"""
See staff_data_show_centric.py. This one in particular will examine the top 15 VA from every show.
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
SHAFT = nx.Graph()
for one_show in shows:
  if show_count > max_shows:
    break
  voice_actors = []
  va_counter = 0
  max_va = 15
  for char in one_show["chars"]:
    if va_counter > max_va:
      break
    for voice_actor in char["voice_actors"]:
      if voice_actor["language"] != "Japanese":
        continue
      else:
        voice_actors.append(voice_actor) 
        break
    
    va_counter += 1

  for i in range(len(voice_actors)):
      for j in range(len(voice_actors)):
        if i == j:
          continue
        va1_name = voice_actors[i]["person"]["name"]
        va2_name = voice_actors[j]["person"]["name"]

        SHAFT.add_edge(va1_name, va2_name, label=one_show["title"])
  # show_count += 1
# print(major_staffs)

sorted_degree_list = sorted(SHAFT.degree, key=lambda tuple: tuple[1], reverse=True)
with open("./graphs/top_va.txt", "w") as f:
  for va_tuple in sorted_degree_list:
      print(va_tuple)
      f.write(va_tuple.__str__())
      f.write("\n")