"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        runner = self.root
        for char in word:
            if char not in runner.children:
                runner.children[char] = TrieNode()
            runner = runner.children[char]
        runner.endOfWord = True

    def search(self, word: str) -> bool:
        def helper(root, index):
            current = root
            for i in range(index, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in current.children.values():
                        if helper(child, i + 1):
                            return True
                    return False
                else:
                    if ch not in current.children:
                        return False
                    current = current.children[ch]
            return current.endOfWord

        return helper(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)