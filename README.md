# Minimum-Spanning-Tree
In this project we find the Minimum Spanning Tree of an undirected graph using Prim's algorithm. A Minimum Spanning Tree of a graph is the set of edges that connects every vertex of the graph with minimum total edge cost, and has no cycles.
The edges of the graph are provided in the text file named "edges.txt". The first line indicates the total number of nodes and edges (space separated) in the graph. On every line from the second line onwards, the first two values indicate the IDs of the two end vertices. The third value indicates the edge cost (space separated).

Instructions to run the project:
1)  Clone this repository on your local machine.
2)  Add your input text file to the folder (the graph in your input file should have the format same as the one in "edges.txt")
3)  Specify the name of your input file in the file "main.py" on line 3.
4)  Run the file "main.py".
5)  Check the file "SpanningTree.txt" for the output.

Edge.py:
This file defines the "Edge" class.
Every edge has an "id" two end vertices named "v1" and "v2" and an edge-cost.

Vertex.py:
This file defines the "Vertex" class.
Every vertex has an "id", and a list "edges" that stores the "ids" of all the edges incident to that vertex.

Graph.py:
This file defines the "Graph" class.
The graph has two dictonary named "edges" and "vertices" which stores all the edge and vertex instances with their respective "ids" as keys.

main.py:
This is the file that creates the "Graph" instance by passing the input file.
Here we call the "prims_min_span" method on the graph instance that generates the output file.

Time Complexity Analysis:
Total time required = O(|E|*|V|)