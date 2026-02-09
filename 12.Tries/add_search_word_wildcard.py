class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class InsertAndSearchWordsWithWildcards:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(M) where M is length of word | Space: O(M) for new nodes
    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True

    # Time: O(M) for no wildcards, O(N*26^K) worst case where N is nodes, K is wildcards | Space: O(M) for recursion
    def search(self, word: str) -> bool:
        return self.search_helper(0, word, self.root)
    
    # Time: O(M) best case, O(N*26^K) worst case | Space: O(M) for recursion depth
    def search_helper(self, word_index: int, word: str, node: TrieNode) -> bool:
        for i in range(word_index, len(word)):
            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if self.search_helper(i + 1, word, child):
                        return True
                return False
            
            elif c in node.children:
                node = node.children[c]
            
            else:
                return False
        return node.is_word

def main():
    # Create a new WordDictionary with wildcard support
    word_dict = InsertAndSearchWordsWithWildcards()
    
    # Test 1: Insert words
    print("=== Test 1: Inserting words ===")
    words = ["bad", "dad", "mad", "pad", "bat", "cat", "dog", "application"]
    for word in words:
        word_dict.insert(word)
        print(f"Inserted: {word}")
    
    # Test 2: Search for exact words (no wildcards)
    print("\n=== Test 2: Searching for exact words ===")
    exact_searches = ["bad", "dad", "bat", "dog", "application", "app", "xyz"]
    for word in exact_searches:
        result = word_dict.search(word)
        print(f"Search '{word}': {result}")
    
    # Test 3: Search with single wildcard
    print("\n=== Test 3: Searching with single wildcard ===")
    single_wildcard = [".ad", "b.d", "ba.", "d.g", ".at"]
    for pattern in single_wildcard:
        result = word_dict.search(pattern)
        print(f"Search '{pattern}': {result}")
    
    # Test 4: Search with multiple wildcards
    print("\n=== Test 4: Searching with multiple wildcards ===")
    multiple_wildcards = ["..d", "b..", "...", ".........", "a..........n"]
    for pattern in multiple_wildcards:
        result = word_dict.search(pattern)
        print(f"Search '{pattern}': {result}")
    
    # Test 5: Search with all wildcards
    print("\n=== Test 5: Searching with all wildcards ===")
    all_wildcards = ["...", ".........", "..........."]
    for pattern in all_wildcards:
        result = word_dict.search(pattern)
        print(f"Search '{pattern}': {result}")
    
    # Test 6: Edge cases
    print("\n=== Test 6: Edge cases ===")
    word_dict.insert("a")
    word_dict.insert("")
    edge_cases = [".", "a", "", "..", "...."]
    for pattern in edge_cases:
        result = word_dict.search(pattern)
        print(f"Search '{pattern}': {result}")
    
    # Test 7: Mixed patterns
    print("\n=== Test 7: Mixed wildcard patterns ===")
    mixed_patterns = [".pplication", "app........", "a..l.c.t..n", "d.."]
    for pattern in mixed_patterns:
        result = word_dict.search(pattern)
        print(f"Search '{pattern}': {result}")

if __name__ == "__main__":
    main()
