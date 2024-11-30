import networkx as nx
from pyvis.network import Network
import random

def create_multigraph_visualization(nodes, edges, output_file='multigraph.html'):
    # Create a multigraph
    G = nx.MultiGraph()

    # Add nodes with hover text
    for node, hover_text in nodes.items():
        G.add_node(node, title=hover_text)

    # Add edges with labels
    for edge in edges:
        G.add_edge(edge[0], edge[1], label=edge[2])

    # Create a PyVis network
    net = Network(notebook=True, height="500px", width="100%", bgcolor="#222222", font_color="white")
    net.from_nx(G)

    # Customize node appearance
    for node in net.nodes:
        node['color'] = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        node['size'] = 30

    # Customize edge appearance
    for edge in net.edges:
        edge['color'] = 'lightgray'

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
      }
    }
    ''')

    # Save and show the graph
    net.show(output_file)

# Example usage
nodes = {
    "A": "This is node A",
    "B": "This is node B",
    "C": "This is node C",
    "D": "This is node D"
}

edges = [
    ("A", "B", "Edge 1"),
    ("A", "C", "Edge 2"),
    ("B", "C", "Edge 3"),
    ("C", "D", "Edge 4"),
    ("A", "D", "Edge 5"),
    ("A", "B", "Edge 6")  # Multiple edge between A and B
]

create_multigraph_visualization(nodes, edges)