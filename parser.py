from table_generator import LL1Grammar

def parse_input(grammar_text, input_string):
    grammar = LL1Grammar(grammar_text)
    parse_table = grammar.construct_parse_table()

    stack = ['$', grammar.start_symbol]
    input_tokens = input_string.split() + ['$']
    steps = []

    tree = {'symbol': grammar.start_symbol, 'children': []}
    nodes = [tree]

    i = 0
    while stack:
        top = stack.pop()
        current = input_tokens[i]

        if top == current:
            steps.append(f"Match: {current}")
            i += 1
            continue
        elif top in grammar.terminals or top == '$':
            raise SyntaxError(f"Unexpected token: {current}")
        elif (top, current) in parse_table:
            production = parse_table[(top, current)]
            rhs = production.split()
            steps.append(f"{top} -> {' '.join(rhs)}")

            parent = nodes.pop()
            for sym in reversed(rhs):
                if sym != 'ε':
                    node = {'symbol': sym, 'children': []}
                    parent['children'].insert(0, node)
                    nodes.append(node)

            if rhs != ['ε']:
                stack.extend(reversed(rhs))
        else:
            raise SyntaxError(f"No rule for ({top}, {current})")

    return tree, steps