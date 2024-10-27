"""
Tries are DS (also called prefix tree) that are used to store the strings (or dictionaries) efficiently.
The Trie Node cannot store characters, since there is no way to make the connections between words.
Thus need children of type TrieNode. Since each index belongs to a character, there is no need to store the
character. We can simply check if TrieNode exists on that index.
hmap can also be used to store children, under the hood hmap also use array.
SC:
The words can be stored in hmap as well. When multiple words are stored in hmap, each word is stored separately.
But in Trie the same part of wrods can be resued. For example, cat, cattle, catch. Thus for large dataset Tries work better
for sparse data, for each charcater we create array of character 26, even though they are Null pointers they
will occupy space. Then hmap can be used.

TC:
hmap search for word: generate hash code (l) but the length of string is constant, thus O(1)
Trie search for word: O(l) l: length of word, thus O(1)

hmap search for prefix: iterate over each word in hset, check if prefix exists. O(n) * O(l)
Trie search for hmap: iterate over the Trie and check. O(l) length of prefix.
"""

class TrieNode:
    # the trie node will have 26 children, (just like trees) and an isEnd variable to verfiy if the word ends.
    def __init__(self, isEnd):
        self.children = [None for _ in range(26)]
        self.isEnd = isEnd

class Trie:

    def __init__(self):
        self.root = TrieNode(False)


    def insert(self, word: str) -> None:
        # get the root of Trie
        curr = self.root
        # traverse the word
        for w in word:
            # check if the letter is already there
            idx = ord(w) - ord("a")
            if not curr.children[idx]: # letter not there
                newNode = TrieNode(False)
                curr.children[idx] = newNode
            # keep moving forward
            curr =  curr.children[idx]
        curr.isEnd = True



    def search(self, word: str) -> bool:
        # get the root of Trie
        curr = self.root
        # traverse the word
        for w in word:
            idx = ord(w) - ord("a")
            if not curr.children[idx]:  # letter not there
                return False
            else:
                curr = curr.children[idx]

        return curr.isEnd


    def startsWith(self, prefix: str) -> bool:
        # get the root of Trie
        curr = self.root
        # traverse the word
        for w in prefix:
            idx = ord(w) - ord("a")
            if not curr.children[idx]:  # letter not there
                return False
            else:
                curr = curr.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# word = "abc"
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)