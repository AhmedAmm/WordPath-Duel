from algorithms.trie import Trie

n, m = 6, 10
trie = Trie(n, m)
trie1=Trie(1, 1)

# List of words with scores
words = [
    ("aa", 10),
    ("aaa", 20),
    ("abc", 50),
    ("abb", 4),
    ("abba", 6),
    ("aaba", 7),
    ("abcd", 3),
    ("aaab", 5),
    ("abbb", 2),
    ("a", -10)
]

# Insert words into the Trie
for word, score in words:
    trie.insert(word, score)
    trie1.insert(word[::-1], score)

# Generate the grid
grid = trie.grid_gen()


def minimax(i: int, j: int, s: str) -> (int, str):
    score = 0
    s = grid[i][j] + s
    score += trie1.work(s)
    if i == n - 1 and j == m - 1:
        return (score, 'F')
    aux1 = -1
    aux2 = -1
    path1=''
    path2=''
    if i < n - 1:
        aux1, path1 = minimax(i + 1, j, s)
    if j < m - 1:
        aux2, path2 = minimax(i, j + 1, s)
    if aux1 == -1:
        return aux2 + score, 'R'+path2
    elif aux2 == -1:
        return aux1 + score, 'D'+path1
    if (i + j) % 2:
        if aux1 > aux2:
            return aux1 + score, 'D'+path1
        else:
            return aux2 + score, 'R'+path2
    else:
        if aux1 < aux2:
            return aux1 + score, 'D'+path1
        else:
            return aux2 + score, 'R'+path2

ans,path = minimax(0, 0, '')
for row in grid:
        print(" ".join(str(cell) if isinstance(cell, str) else '.' for cell in row))
print(ans)
print(path)
