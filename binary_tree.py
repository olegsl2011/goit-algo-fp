import uuid
import networkx as nx
import matplotlib.pyplot as plt

from helpers.rnd import random_unique_int_list

colormap = plt.get_cmap('cool')


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def insert_to_binary_tree(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert_to_binary_tree(root.left, key)
    elif key > root.val:
        root.right = insert_to_binary_tree(root.right, key)

    return root


def list_to_binary_tree(lst):
    if not lst:
        return None

    root = Node(lst[0])

    for key in lst[1:]:
        root = insert_to_binary_tree(root, key)

    return root


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


def create_graph(tree_root):
    g = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    g = add_edges(g, tree_root, pos)

    return g, pos


def draw_graph(g, pos, title=None):
    colors = [node[1]['color'] for node in g.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in g.nodes(data=True)}

    plt.figure(figsize=(8, 5))

    if title:
        plt.title(title)

    nx.draw(g, pos=pos, labels=labels, arrows=False, node_size=1000, node_color=colors)

    plt.show()


def set_node_colors_bfs(graph, root):
    queue = [root]
    visited = set()

    while queue:
        current_node = queue.pop(0)
        if current_node.id not in visited:
            visited.add(current_node.id)
            color_value = len(visited)
            graph.nodes[current_node.id]['color'] = colormap(color_value / len(graph.nodes))

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def set_node_colors_dfs(graph, root):
    stack = [root]
    visited = set()

    while stack:
        current_node = stack.pop()
        if current_node.id not in visited:
            visited.add(current_node.id)
            color_value = len(visited)
            graph.nodes[current_node.id]['color'] = colormap(color_value / len(graph.nodes))

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)


if __name__ == "__main__":
    list_example = random_unique_int_list(8, 12, 0, 100)
    root = list_to_binary_tree(list_example)

    g, pos = create_graph(root)
    draw_graph(g, pos, title="Binary Tree")

    set_node_colors_bfs(g, root)
    draw_graph(g, pos, title="Breadth-first Search in Binary Tree")

    set_node_colors_dfs(g, root)
    draw_graph(g, pos, title="Depth-first Search in Binary Tree")
