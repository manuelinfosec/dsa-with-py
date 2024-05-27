"""
A Trie (pronounced "try"), also known as a prefix tree,
is a tree-like data structure used to store a dynamic set
of strings, where each node represents a single character
of a string. It is commonly used for tasks such as autocomplete
and spell checking.
"""


class TrieNode:
    """
    A class representing a single node in a Trie.
    Each node contains a dictionary of its child nodes and a boolean
    indicating whether it marks the end of a valid word.
    """

    def __init__(self, char: str | None = None):
        self.char: str | None = char
        # Mapping characters to corresponding child nodes
        self.children: dict[str, TrieNode] = {}
        # Is this the end of a valid word (False by default)
        self.word = False

    def visualize(self, level=0, prefix=""):
        """
        Recursively visualizes the Trie node and its children with indentation and lines.

        Args:
            level (int): The current level of the node in the Trie (used for indentation).
            prefix (str): The prefix string used for visualizing connections.
        """
        # Print the current node's character and word status with indentation and prefix
        if self.char:
            if self.word:
                print(f"{prefix}{self.char}-EOW")
            else:
                print(f"{prefix}{self.char}")

        # Prepare the prefix for child nodes
        new_prefix = prefix + ("|  " if prefix else "")
        child_count = len(self.children)

        # Recursively visualize each child node with lines
        for idx, child in enumerate(self.children.values()):
            if idx == child_count - 1:  # Last child
                child.visualize(level + 1, new_prefix[:-3] + "   +--")
            else:  # Not the last child
                child.visualize(level + 1, new_prefix[:-3] + "|  +--")


class Trie:
    """
    A class representing the Trie data structure.
    It supports insertion of words, searching for words,
    and checking if any word in the Trie starts with a given prefix.
    """

    def __init__(self):
        """
        Initializes the Trie with an empty root node.
        """
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to insert.
        """
        curr = self.root
        # Iterate through every character of the string
        for letter in word:
            # Check if this character is already a child node
            if letter not in curr.children:
                # If not, create a new node for the current character
                # and assign it as a child of the current node
                curr.children[letter] = TrieNode(letter)
            # Reassign the child node as the current node
            curr = curr.children[letter]
        # At the end of iteration, mark last node as the end of word
        curr.word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists in the Trie, False otherwise.
        """
        curr = self.root
        # Iterate through every character in the string
        for letter in word:
            # Check if the letter is a child of the current node
            if letter not in curr.children:
                # If it's not a child, then the entire word doesn't exist
                return False
            # Reassign the child node as the current node
            curr = curr.children[letter]
        # At the end of iteration, check if last character has an EOW flag
        return curr.word

    def startswith(self, prefix: str) -> bool:
        """
        Checks if any word in the Trie starts with a given prefix.

        Args:
            prefix (str): The prefix to check for.

        Returns:
            bool: True if any word starts with the prefix, False otherwise.
        """
        curr = self.root
        # Iterate through every character in the string
        for letter in prefix:
            # Check if the letter is a child of the current node
            if letter not in curr.children:
                # If it's not a child, then the entire prefix doesn't exist
                return False
            # Reassign the child node as the current node
            curr = curr.children[letter]
        # If nothing goes wrong, the prefix exists in the tree
        return True

    def visualize(self):
        self.root.visualize()


trie = Trie()


# Insert words into the Trie
trie.insert("apple")
trie.insert("ape")
# trie.insert("ac")
# trie.insert("ab")

# Search for words
# print(trie.search("apple"))  # True
# print(trie.search("app"))  # True
# print(trie.search("appl"))  # False

# # Check for prefixes
# print(trie.startswith("app"))  # True
# print(trie.startswith("apl"))  # False


# Auto-complete example
words = ["apple", "app", "apricot", "banana", "bat", "batch", "batman"]
for word in words:
    trie.insert(word)


trie.visualize()
