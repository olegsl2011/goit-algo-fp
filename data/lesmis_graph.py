import networkx as nx

gml_file_path = './data/lesmis.gml'

graph = nx.read_gml(gml_file_path)

# Add edge weights: as edge value is the level of coappearance, let's make the weight as 1 / value
for u, v, d in graph.edges(data=True):
    d['weight'] = 1 / d['value']

print('Les Miserables graph loaded\n')
