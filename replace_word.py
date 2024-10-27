"""
Todo: Appraoch1: using hashmap

Approach2:
Using Trie DS
TC:
insert to trie: O(n*l) # number of words in dict +
(m*l) splitting the sentence + O(m) traverse the given sentence * O(l) length of word to be searched.
SC: O(n*l) + (m*l)
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            idx = ord(w) - ord("a")
            if not curr.children[idx]:
                newNode = TrieNode()
                curr.children[idx] = newNode
            curr = curr.children[idx]
        curr.isEnd = True

    def search(self, word):
        curr = self.root
        count = 0
        for w in word:
            idx = ord(w) - ord("a")
            if not curr.children[idx] or curr.isEnd:
                break
            curr = curr.children[idx]
            count += 1

        # what is the word is not present at all
        if not count:
            return word
        # what if the letters are there but isEnd is not true, meaning word is not present
        if not curr.isEnd:
            return word
        # if isEnd is true then return the prefix
        return word[:count]


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trieObj = Trie()
        ans = []
        # store the dictionary in Trie
        for word in dictionary:
            trieObj.insert(word)

        # split the sentence based on the space
        sent = sentence.split(" ")
        for word in sent:
            w = trieObj.search(word)
            ans.append(w)
        return " ".join(ans)
