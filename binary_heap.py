import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt

from helpers.rnd import random_unique_int_list


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap_list):
    heap_root = Node(heap_list[0])
    nodes = [heap_root]

    for i in range(len(heap_list)):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

        if left_child_idx < len(heap_list):
            nodes[i].left = Node(heap_list[left_child_idx])
            nodes.append(nodes[i].left)
        if right_child_idx < len(heap_list):
            nodes[i].right = Node(heap_list[right_child_idx])
            nodes.append(nodes[i].right)

    heap_graph = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap_graph = add_edges(heap_graph, heap_root, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=1500, node_color=colors)
    plt.show()


if __name__ == "__main__":
    heap = random_unique_int_list(8, 12, 0, 100)

    heapq.heapify(heap)

    draw_heap(heap)
