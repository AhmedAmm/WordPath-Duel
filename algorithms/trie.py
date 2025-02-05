import random
class TrieNode:
    def __init__(self):
        self.nxt = {}  # Dictionary to store next nodes (key: character, value: TrieNode)
        self.sub = {}  # Dictionary to store counts of substrings (key: character, value: count)
        self.score = 0  # Score associated with the node (for end-of-word)

class Trie:
    def __init__(self,n,m):
        self.nodes = []  # List to store all nodes
        self.new_node()  # Initialize the root node
        self.grid = [['.'] * m for _ in range(n)]
        self.n = n
        self.m = m

    def new_node(self):
        node = TrieNode()
        self.nodes.append(node)
        return len(self.nodes) - 1  # Return the index of the new node

    def init(self):
        self.nodes = []  # Reset the list of nodes
        self.new_node()  # Create the root node

    def insert(self, s, sc):
        curr = 0  # Start at the root node
        for i in range(len(s)):
            c = s[i]  # Current character
            if c not in self.nodes[curr].nxt:
                self.nodes[curr].nxt[c] = self.new_node()  # Create a new node if it doesn't exist
            if c not in self.nodes[curr].sub:
                self.nodes[curr].sub[c] = 0
            self.nodes[curr].sub[c] += 1  # Increment the substring count
            curr = self.nodes[curr].nxt[c]  # Move to the next node
            if i == len(s) - 1:  # If it's the last character of the word
                self.nodes[curr].score += sc  # Add the score to the node

    def work(self, s):
        ans = 0
        curr = 0  # Start at the root node
        for i in range(len(s)):
            c = s[i]  # Current character
            if c not in self.nodes[curr].nxt:
                break  # If the character doesn't exist in the trie, stop
            curr = self.nodes[curr].nxt[c]  # Move to the next node
            ans += self.nodes[curr].score  # Add the score of the current node
        return ans

    def rec(self,i,j,curr):
        if i==self.n-1 and j==self.m-1: return
        if len(self.nodes[curr].nxt)==0: return
        l=[]
        for v in self.nodes[curr].nxt.keys():
           l.append(v)
        random.shuffle(l)
        k=0
        val=random.randint(0,2)
        if(val==0):
            if i!=self.n-1 and self.grid[i+1][j]=='.':
                self.grid[i+1][j]=l[k]
                self.rec(i+1,j,self.nodes[curr].nxt.get(l[k]))
                k+=1
            if j!=self.m-1 and self.grid[i][j+1]=='.' and len(l)>k:
                self.grid[i][j+1]=l[k]
                self.rec(i,j+1,self.nodes[curr].nxt.get(l[k]))
                k+=1
        else :
            if j!=self.m-1 and self.grid[i][j+1]=='.' and len(l)>k:
                self.grid[i][j+1]=l[k]
                self.rec(i,j+1,self.nodes[curr].nxt.get(l[k]))
                k+=1
            if i!=self.n-1 and self.grid[i+1][j]=='.' and len(l)>k:
                self.grid[i+1][j]=l[k]
                self.rec(i+1,j,self.nodes[curr].nxt.get(l[k]))
                k+=1


    def grid_gen(self):
        l = []
        for v in self.nodes[0].nxt.keys():
            l.append(v)
        random.shuffle(l)
        k=0
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]=='.':
                    char = l[k]
                    self.grid[i][j]=l[k]
                    self.rec(i, j,self.nodes[0].nxt[char])
                    k=(k+1)%len(l)
        return self.grid

