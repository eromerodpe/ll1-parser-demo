from table_generator import LL1Grammar

class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

    def add(self, child):
        self.children.append(child)

def parse_input(grammar_text, input_string):
    g = LL1Grammar()
    g.load_grammar(grammar_text)
    g.compute_first()
    g.compute_follow()
    g.build_table()

    stack = ['$', g.start_symbol]
    input_tokens = input_string.split() + ['$']
    cursor = 0
    root = Node(g.start_symbol)
    nodes_stack = [root]
    steps = []

    while stack:
        top = stack.pop()
        node = nodes_stack.pop()
        current = input_tokens[cursor]

        steps.append(f"STACK: {stack} | INPUT: {input_tokens[cursor:]} | TOP: {top}")

        if top == current:
            cursor += 1
            continue
        elif top in g.terminals or top == '$':
            raise SyntaxError(f"Unexpected token: {current}")
        elif current in g.table[top]:
            production = g.table[top][current]
            for sym in reversed(production):
                if sym != 'ε':
                    stack.append(sym)
            for sym in production:
                child = Node(sym)
                node.add(child)
                if sym != 'ε':
                    nodes_stack.append(child)
        else:
            raise SyntaxError(f"No rule for ({top}, {current})")

    return root, steps
