import random
from Vertex import Vertex
from Edge import Edge

class Graph:

    def __init__(self, filename, debug=False):

        self.edges = dict()
        self.vertices = dict()

        with open(filename,'r') as f:
            topline = f.readline().strip().split()
            self.no_of_vertices = int(topline[0])
            self.no_of_edges = int(topline[1])
            edge_id_count = 1
            for line in f:
                line_arr = line.strip().split()
                # line_arr = [x for x in line_arr]
                cost = int(line_arr.pop())
                for v_id in line_arr:
                    if v_id not in self.vertices:
                        v = Vertex(v_id,edge_id_count)
                        self.vertices[v_id] = v
                    else:
                        self.vertices[v_id].update_edges(edge_id_count)
                new_edge = Edge(edge_id_count,line_arr[0],line_arr[1],cost)
                self.edges[edge_id_count] = new_edge
                edge_id_count+=1



    def prims_min_span(self):
        total_span_cost = 0
        spanning_tree = list()
        discovered = set()
        starting=random.choice(list(self.vertices.keys()))
#         starting=random.choice(self.vertices)
#         starting = starting.Id
#         print(starting)
        discovered.add(starting)
        remaining = set(self.vertices.keys()) - discovered
        while len(remaining) > 0:
            qualified_edges = list()
            for Id,edge in self.edges.items():
                if (edge.v1_id in discovered and edge.v2_id in remaining) or (edge.v2_id in discovered and edge.v1_id in remaining):
                    qualified_edges.append(edge)

            qualified_edges.sort(key=lambda x:x.cost, reverse=False)
            chosen_edge = qualified_edges[0]
            total_span_cost += chosen_edge.cost
            v1_id = chosen_edge.v1_id
            v2_id = chosen_edge.v2_id
            spanning_tree.append(chosen_edge)
            if v1_id not in discovered:
                discovered.add(v1_id)
                remaining.remove(v1_id)

            else:
                discovered.add(v2_id)
                remaining.remove(v2_id)

        return (total_span_cost,spanning_tree)

    def __str__(self):
        s="The Edges are as follows:\n"
        for edge in g.edges.values():
            s += edge.__str__() + "\n"
        s+="\nThe Vertices are as follows:\n"
        for vertex in g.vertices.values():
            s += vertex.__str__() + "\n"
        return s
