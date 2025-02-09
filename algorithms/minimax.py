from .trie import Trie
from typing import Tuple

class Minimax:
    def __init__(self, n, m):
        self.trie = Trie(n,m)
        self.trie1 = Trie(1,1)
        self.words=[]
        self.grid = [['.'] * m for _ in range(n)]
        self.n = n
        self.m = m

    def insert(self, s, sc):
        self.words.append((s, sc))

    def grid_gen(self):
        for word, score in self.words:
            self.trie.insert(word, score)
            self.trie1.insert(word[::-1], score)
        self.grid = self.trie.grid_gen()
        return self.grid

    def minimax(self, i: int, j: int, s: str) -> Tuple[int, str]:
        score = 0
        s = self.grid[i][j] + s
        score += self.trie1.work(s)
        if i == self.n - 1 and j == self.m - 1:
            return (score, 'F')
        aux1 = -1
        aux2 = -1
        if i < self.n - 1:
            aux1, move = self.minimax(i + 1, j, s)
        if j < self.m - 1:
            aux2, move = self.minimax(i, j + 1, s)
        if aux1 == -1:
            return aux2 + score, 'R'
        elif aux2 == -1:
            return aux1 + score, 'D'
        if (i + j) % 2:
            if aux1 > aux2:
                return aux1 + score, 'D'
            else:
                return aux2 + score, 'R'
        else:
            if aux1 < aux2:
                return aux1 + score, 'D'
            else:
                return aux2 + score, 'R'
                