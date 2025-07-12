class LL1Grammar:
    def __init__(self, grammar_text):
        self.productions = {}
        self.terminals = set()
        self.non_terminals = set()
        self.first_sets = {}
        self.follow_sets = {}
        self.start_symbol = ''
        self._parse_grammar(grammar_text)

    def _parse_grammar(self, text):
        for line in text.strip().split('\n'):
            head, prods = line.split('->')
            head = head.strip()
            if not self.start_symbol:
                self.start_symbol = head
            self.non_terminals.add(head)
            self.productions[head] = [prod.strip().split() for prod in prods.split('|')]
            for prod in self.productions[head]:
                for symbol in prod:
                    if not symbol.isupper() and symbol != 'ε':
                        self.terminals.add(symbol)

    def construct_parse_table(self):
        table = {}
        self._compute_first_sets()
        self._compute_follow_sets()
        for head, prods in self.productions.items():
            for prod in prods:
                first = self._get_first_of_string(prod)
                for terminal in first - {'ε'}:
                    table[(head, terminal)] = ' '.join(prod)
                if 'ε' in first:
                    for terminal in self.follow_sets[head]:
                        table[(head, terminal)] = ' '.join(prod)
        return table

    def _compute_first_sets(self):
        for symbol in self.non_terminals:
            self.first_sets[symbol] = set()
        changed = True
        while changed:
            changed = False
            for head, prods in self.productions.items():
                for prod in prods:
                    for symbol in prod:
                        if symbol in self.terminals or symbol == 'ε':
                            if symbol not in self.first_sets[head]:
                                self.first_sets[head].add(symbol)
                                changed = True
                            break
                        else:
                            before = len(self.first_sets[head])
                            self.first_sets[head].update(self.first_sets[symbol] - {'ε'})
                            if 'ε' not in self.first_sets[symbol]:
                                break
                            if before != len(self.first_sets[head]):
                                changed = True
                    else:
                        if 'ε' not in self.first_sets[head]:
                            self.first_sets[head].add('ε')
                            changed = True

    def _compute_follow_sets(self):
        for symbol in self.non_terminals:
            self.follow_sets[symbol] = set()
        self.follow_sets[self.start_symbol].add('$')
        changed = True
        while changed:
            changed = False
            for head, prods in self.productions.items():
                for prod in prods:
                    trailer = self.follow_sets[head].copy()
                    for symbol in reversed(prod):
                        if symbol in self.non_terminals:
                            before = len(self.follow_sets[symbol])
                            self.follow_sets[symbol].update(trailer)
                            if 'ε' in self.first_sets[symbol]:
                                trailer.update(self.first_sets[symbol] - {'ε'})
                            else:
                                trailer = self.first_sets[symbol]
                            if before != len(self.follow_sets[symbol]):
                                changed = True
                        else:
                            trailer = {symbol}

    def _get_first_of_string(self, symbols):
        result = set()
        for symbol in symbols:
            if symbol in self.terminals or symbol == 'ε':
                result.add(symbol)
                break
            result.update(self.first_sets[symbol] - {'ε'})
            if 'ε' not in self.first_sets[symbol]:
                break
        else:
            result.add('ε')
        return result