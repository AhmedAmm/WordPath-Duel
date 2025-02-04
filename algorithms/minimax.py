from .trie import Trie


class Minimax:
    def __init__(self, n, m):
        self.trie = Trie()
        self.grid = []
        self.n = n
        self.m = m

    def minimax(self, i: int, j: int, s: str) -> (int, str):
        score = 0
        s = self.grid[i][j] + s
        score += self.trie.work(s)
        if i == self.n - 1 and j == self.m - 1:
            return (score, 'F')
        aux1 = -1
        aux2 = -1
        if i < self.n - 1:
            aux1, _ = self.minimax(i + 1, j, s)
        if j < self.m - 1:
            aux2, _ = self.minimax(i, j + 1, s)
        if aux1 == -1:
            return aux2 + score, 'D'
        elif aux2 == -1:
            return aux1 + score, 'R'
        if (i + j) % 2:
            if aux1 > aux2:
                return aux1 + score, 'R'
            else:
                return aux2 + score, 'D'
        else:
            if aux1 < aux2:
                return aux1 + score, 'R'
            else:
                return aux2 + score, 'D'
