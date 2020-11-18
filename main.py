from Graph import Graph

filename = 'edges.txt'
g = Graph(filename)
spanning_tree_cost, spanning_tree = g.prims_min_span()
f = open("SpanningTree.txt",'w')
f.write("Minimum spanning cost: {}\n".format(spanning_tree_cost))
f.write("Following are the edges in the minimum spanning tree of graph {}:\n".format(filename))
for edge in spanning_tree:
    f.write("{}-{}; cost={}\n".format(edge.v1_id,edge.v2_id,edge.cost))
f.close()
print("Check file 'SpanningTree.txt' for the Minimum Spanning Tree.")
