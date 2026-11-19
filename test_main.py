from main import *

def example_graph():
    # the example graph from the edge contraction lecture
    vertices = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
    edges = set([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'g'), 
                 ('d', 'e'), ('d', 'f'), ('e', 'f'),
                 ('h', 'i'), ('i', 'g'), ('h', 'g')])
    return vertices, edges

# 3 pts
def test_edge_contract_seq():
    vertices, edges = example_graph()
    # will use a sorted edge list for testing to ensure we get the same result.
    edges = sorted(list(edges))
    # edges in order are:
    # [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'g'), ('d', 'e'), ('d', 'f'), ('e', 'f'), ('h', 'g'), ('h', 'i'), ('i', 'g')]
    new_vertices, vertex_map = edge_contract_seq(vertices, edges)
    # these are the super vertices
    assert sorted(list(new_vertices)) == ['b', 'c', 'e', 'f', 'g', 'i']
    # map: a->b  d->e  h->g, plus the singletons  
    assert vertex_map['a'] == 'b'
    assert vertex_map['b'] == 'b'
    assert vertex_map['c'] == 'c'
    assert vertex_map['d'] == 'e'    
    assert vertex_map['e'] == 'e'
    assert vertex_map['f'] == 'f'
    assert vertex_map['g'] == 'g'
    assert vertex_map['h'] == 'g'
    assert vertex_map['i'] == 'i'

# 2 pts
def test_num_components():
    vertices, edges = example_graph()
    assert num_components(vertices, edges, edge_contract_seq) == 2

# 3 pts
def test_edge_contract_seq_sizes():
    vertices, edges = example_graph()
    sizes = Counter()
    sizes.update(vertices)
    # i'm sorting the edge set so we get the same results for testing.
    new_vertices, vertex_map, sizes = edge_contract_seq_sizes(vertices, sorted(list(edges)), sizes)
    # super vertices e,b,g now have size 2
    assert sizes['b'] == 2
    assert sizes['e'] == 2
    assert sizes['g'] == 2
    assert sizes['a'] == 1
    assert sizes['c'] == 1
    assert sizes['d'] == 1
    assert sizes['f'] == 1
    assert sizes['h'] == 1

# 2 pts
def test_component_sizes():
    vertices, edges = example_graph()
    # initialize counts to be 1 for each vertex.
    sizes = Counter()
    sizes.update(vertices)
    # sizes is: {'a': 1, 'b': 1, ...}
    assert sorted(component_sizes(vertices, edges, edge_contract_seq_sizes, sizes)) == [3, 6]
