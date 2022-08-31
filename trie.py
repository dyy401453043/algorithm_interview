# leetcode208 实现字典树Trie
class Trie:

    def __init__(self):
        self.is_end = False
        self.next = [None] * 26

    def insert(self, word: str) -> None:
        temp = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not temp.next[index]:
                temp.next[index] = Trie()
            temp = temp.next[index]
        temp.is_end = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True
        temp = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not temp.next[index]:
                return False
            temp = temp.next[index]
        return temp.is_end

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        temp = self
        for ch in prefix:
            index =ord(ch) - ord('a')
            if not temp.next[index]:
                return False
            temp = temp.next[index]
        return True
