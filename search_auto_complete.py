class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.current_input = ""
        self.current_node = self.trie
        self.sentence_to_count = {}

        for i in range(len(sentences)):
            self.add_sentence(sentences[i], times[i])

    def add_sentence(self, sentence: str, count: int):
        # Update the overall sentence count
        self.sentence_to_count[sentence] = (
            self.sentence_to_count.get(sentence, 0) + count
        )
        node = self.trie

        for char in sentence:
            if char not in node:
                node[char] = {}
            if "suggestions" not in node:
                node["suggestions"] = []
            node["suggestions"].append((self.sentence_to_count[sentence], sentence))
            node["suggestions"].sort(
                key=lambda x: (-x[0], x[1])
            )  # Keep most frequent first
            if len(node["suggestions"]) > 3:
                node["suggestions"].pop()  # Only keep top 3
            node = node[char]

    def input(self, c: str) -> List[str]:
        if c == "#":
            # Add the current input to the system
            self.add_sentence(self.current_input, 1)
            self.current_input = ""
            self.current_node = self.trie
            return []

        self.current_input += c
        if self.current_node and c in self.current_node:
            self.current_node = self.current_node[c]
            return [
                sentence for _, sentence in self.current_node.get("suggestions", [])
            ]
        else:
            self.current_node = None
            return []


# time complexity is O(m*k^2)
# space complexity is O(m*k)
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
