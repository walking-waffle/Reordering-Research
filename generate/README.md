# Graph Reordering - BFS Ordering
A Python-based random graph generator built with NetworkX. This tool can generate several graph models, optionally assign random edge weights, export graphs as __**edge lists**__, and visualize small graphs.

Supported graph models:

* Watts-Strogatz Small World Graph
* Powerlaw Cluster Graph
* Barabási-Albert Graph


## Requirements
Install dependencies:  
`pip install networkx matplotlib`

## Usage
`ws  [-w] n k p`  
`plc [-w] n m p`  
`ba  [-w] n m`  


## Output
The generated graph is exported as:  

`<graph_type>.el`

If weighted mode is enabled, edge weights are stored in the edge list.


## Visualization
Graphs with fewer than or equal to 1000 vertices are automatically visualized using Matplotlib.

Large graphs skip visualization to avoid performance issues.

## Graph Resources
[Connected-Watts-Strogatz](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.connected_watts_strogatz_graph.html)
  
[Powerlaw Cluster](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.powerlaw_cluster_graph.html)
  
[Barabasi-Albert](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.barabasi_albert_graph.html)
        