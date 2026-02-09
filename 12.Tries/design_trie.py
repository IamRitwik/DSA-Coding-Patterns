class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(M)
    # Space: O(M)
    def insert(self, word: str) -> None:
        node = self.root

        # for each char in word, if its not child of current node
        # create a TrieNode for that character
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        # mark last node as end of word
        node.is_word = True

    # Time: O(M)
    # Space: O(1)
    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    # Time: O(M)
    # Space: O(1)
    def has_prefix(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
            
        return True

def main():
    # Create a new Trie
    trie = Trie()
    
    # Test 1: Insert words
    print("=== Test 1: Inserting words ===")
    words = ["apple", "app", "application", "apply", "banana", "band"]
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")
    
    # Test 2: Search for exact words
    print("\n=== Test 2: Searching for exact words ===")
    search_words = ["apple", "app", "appl", "application", "banana", "ban", "orange"]
    for word in search_words:
        result = trie.search(word)
        print(f"Search '{word}': {result}")
    
    # Test 3: Check for prefixes
    print("\n=== Test 3: Checking prefixes ===")
    prefixes = ["app", "appl", "ban", "bana", "car", "a"]
    for prefix in prefixes:
        result = trie.has_prefix(prefix)
        print(f"Has prefix '{prefix}': {result}")
    
    # Test 4: Edge cases
    print("\n=== Test 4: Edge cases ===")
    trie.insert("")  # Insert empty string
    print(f"Search empty string: {trie.search('')}")
    print(f"Has prefix empty string: {trie.has_prefix('')}")
    
    # Test 5: Single character words
    print("\n=== Test 5: Single character words ===")
    trie.insert("a")
    trie.insert("i")
    print(f"Search 'a': {trie.search('a')}")
    print(f"Search 'i': {trie.search('i')}")
    print(f"Search 'b': {trie.search('b')}")

if __name__ == "__main__":
    main()