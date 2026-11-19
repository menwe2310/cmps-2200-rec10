from collections import Counter

def example_graph():
    # the example graph from the edge contraction lecture
    vertices = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
    edges = set([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'g'), 
                 ('d', 'e'), ('d', 'f'), ('e', 'f'),
                 ('h', 'i'), ('i', 'g'), ('h', 'g')])
    return vertices, edges


def num_components(vertices, edges, partition_graph_f):
    """
    Compute the number of connected components in a graph using contraction.
    This is complete.
    """
    if len(edges) == 0:
        # base case: return the number of super vertices in the final partition
        return len(vertices)
    else:
        new_vertices, vertex_map = partition_graph_f(vertices, edges)
        new_edges = set([(vertex_map[e[0]], vertex_map[e[1]])
                          for e in edges if vertex_map[e[0]] != vertex_map[e[1]]])
        return num_components(new_vertices, new_edges, partition_graph_f)


def edge_contract_seq(vertices, edges):
    """
    Sequential implementation of edge contraction.
    Complete the implementation below.

    Returns:
      new_vertices...set of super vertices in the contracted graph
      vertex_map.....dict from vertex_i->vertex_j, where vertex_j is the 
      super vertiex of vertex_i
    """
    # vertices in all the edges we have selected so far
    selected_vertices = set()
    # dict from vertex->super vertex
    vertex_map = {}
    # set of super vertices
    new_vertices = set()
    for e in edges:
        ### TODO: complete
        pass
    return new_vertices, vertex_map

def edge_contract_seq_sizes(vertices, edges, sizes):
    """
    Modified version of edge contraction that maintains
    a sizes dict that is a map from vertex->int, indicating
    the number of vertices in each component represented
    by each super vertex.

    Complete the implementation below.
    """
    selected_vertices = set()
    vertex_map = {}
    new_vertices = set()
    for e in edges:
        ### TODO: complete
        pass
        
    return new_vertices, vertex_map, sizes

def component_sizes(vertices, edges, partition_graph_f, sizes):
    """
    Computes the size of each connected component using
    edge_contract_seq_sizes.
    This is complete.
    """
    if len(edges) == 0:
        # base case: return the sizes of each super vertex in the final graph.        
        return [sizes[v] for v in vertices]
    else:
        new_vertices, vertex_map, sizes = partition_graph_f(vertices, edges, sizes)
        new_edges = set([(vertex_map[e[0]], vertex_map[e[1]])
                          for e in edges if vertex_map[e[0]] != vertex_map[e[1]]])
        return component_sizes(new_vertices, new_edges, partition_graph_f, sizes)