class TrieNode:
    def __init__(self):
        self.nxt = {}  # Dictionary to store next nodes (key: character, value: TrieNode)
        self.sub = {}  # Dictionary to store counts of substrings (key: character, value: count)
        self.score = 0  # Score associated with the node (for end-of-word)

class Trie:
    def __init__(self):
        self.nodes = []  # List to store all nodes
        self.new_node()  # Initialize the root node

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

