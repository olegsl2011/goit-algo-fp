import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colormaps


def draw_graph(g, title=None, highlighted_edges=None, edge_labels=None):
    degree_dict = dict(g.degree())
    degrees = list(degree_dict.values())

    colormap = colormaps.get_cmap('cool')

    node_colors = [colormap(d / max(degrees)) for d in degrees]

    plt.figure(figsize=(16, 9))

    if title:
        plt.title(title)

    pos = nx.spring_layout(g, k=0.3, iterations=100)

    nx.draw(g, pos, node_size=100, node_color=node_colors, edge_color='#808080', width=0.5, with_labels=True,
            font_size=8)

    if highlighted_edges:
        nx.draw_networkx_edges(g, pos, edgelist=highlighted_edges, edge_color='red', width=0.5)

    if edge_labels:
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=6)

    plt.show()
