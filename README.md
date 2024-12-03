# Shaft (and other anime studio) graphs
[Link to GitHub Pages](https://uyennhiquang.github.io/shaft-graph/)

This repository contains the code used to generate the graphs for the anime studio SHAFT. For both types of graphs - VA and Staff graph - the vertices are the VA/staff who worked on each series/show, and two vertices are adjacent if they worked on the same project. Here are some noteworthy quirks:

- Both are multigraphs.
- For both graphs, as they use a similar algorithm in building the graph from the JSON data, a clique is formed every iteration as the script iterates over the list of shows.
- Interestingly enough, for the VA graph, there is a connected component among some of the VA who voiced Assault Lily (you could even say they form a clique), so the VA graph is disconnected.
- The staff graph has one isolated vertex purely because the data includes a show entry where the studio did a commercial animation.
- A staff's "impact" or "closeness" with the studio can be thought of as their degree.
- Both are certainly not Eulerian or Hamiltonian (speaking of low hanging fruits).