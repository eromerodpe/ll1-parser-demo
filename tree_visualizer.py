from graphviz import Digraph

def draw_tree(node, filename='output/tree'):
    dot = Digraph()
    counter = [0]

    def add_nodes(n):
        idx = str(counter[0])
        counter[0] += 1
        dot.node(idx, n.symbol)
        this_idx = idx
        for c in n.children:
            child_idx = add_nodes(c)
            dot.edge(this_idx, child_idx)
        return this_idx

    add_nodes(node)
    dot.render(filename, format='png', cleanup=True)
