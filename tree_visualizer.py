from graphviz import Digraph

def draw_tree(tree, filename='parse_tree'):
    dot = Digraph()
    counter = [0]

    def add_nodes(node, parent_id=None):
        node_id = str(counter[0])
        dot.node(node_id, node['symbol'])
        counter[0] += 1
        if parent_id is not None:
            dot.edge(parent_id, node_id)
        for child in node['children']:
            add_nodes(child, node_id)

    add_nodes(tree)
    dot.render(filename, format='png', cleanup=True)