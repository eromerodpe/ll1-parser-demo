from collections import defaultdict

class LL1Grammar:
    def __init__(self):
        self.productions = defaultdict(list)
        self.non_terminals = set()
        self.terminals = set()
        self.first = defaultdict(set)
        self.follow = defaultdict(set)
        self.table = defaultdict(dict)
        self.start_symbol = None

    def load_grammar(self, grammar_text):
        for line in grammar_text.strip().split('\n'):
            head, prods = line.split('->')
            head = head.strip()
            if self.start_symbol is None:
                self.start_symbol = head
            self.non_terminals.add(head)
            for prod in prods.split('|'):
                prod = prod.strip().split()
                self.productions[head].append(prod)
                for symbol in prod:
                    if not symbol.isupper() and symbol != 'ε':
                        self.terminals.add(symbol)

    def compute_first(self):
        changed = True
        while changed:
            changed = False
            for head in self.productions:
                for prod in self.productions[head]:
                    for symbol in prod:
                        before = len(self.first[head])
                        if symbol not in self.non_terminals:
                            self.first[head].add(symbol)
                            break
                        else:
                            self.first[head] |= (self.first[symbol] - {'ε'})
                            if 'ε' not in self.first[symbol]:
                                break
                        if all('ε' in self.first[sym] for sym in prod):
                            self.first[head].add('ε')
                        changed |= before != len(self.first[head])

    def compute_follow(self):
        self.follow[self.start_symbol].add('$')
        changed = True
        while changed:
            changed = False
            for head in self.productions:
                for prod in self.productions[head]:
                    trailer = self.follow[head].copy()
                    for symbol in reversed(prod):
                        if symbol in self.non_terminals:
                            before = len(self.follow[symbol])
                            self.follow[symbol] |= trailer
                            changed |= before != len(self.follow[symbol])
                            if 'ε' in self.first[symbol]:
                                trailer |= (self.first[symbol] - {'ε'})
                            else:
                                trailer = self.first[symbol]
                        else:
                            trailer = {symbol}

    def build_table(self):
        for head in self.productions:
            for prod in self.productions[head]:
                first_set = self.get_first_string(prod)
                for terminal in first_set - {'ε'}:
                    self.table[head][terminal] = prod
                if 'ε' in first_set:
                    for terminal in self.follow[head]:
                        self.table[head][terminal] = prod

    def get_first_string(self, symbols):
        result = set()
        for sym in symbols:
            if sym not in self.non_terminals:
                result.add(sym)
                return result
            result |= (self.first[sym] - {'ε'})
            if 'ε' not in self.first[sym]:
                return result
        result.add('ε')
        return result

    def print_table(self):
        import pandas as pd
        import pandas.io.formats.style
        terminals = list(sorted(self.terminals | {'$'}))
        non_terminals = sorted(self.non_terminals)
        data = []
        for nt in non_terminals:
            row = []
            for t in terminals:
                row.append(' '.join(self.table[nt].get(t, [])))
            data.append(row)
        df = pd.DataFrame(data, index=non_terminals, columns=terminals)
        print(df.to_markdown())
