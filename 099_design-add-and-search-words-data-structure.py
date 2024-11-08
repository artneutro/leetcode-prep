# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class WordDictionary:

    def __init__(self):
        self.value = '/'
        self.end = False
        self.children = {}

    def modifyValue(self, char: str) -> None :
        self.value = char

    def modifyEnd(self, val: bool) -> None :
        self.end = val

    def addWord(self, word: str) -> None:
        # Recursively create a WordDictionary object and insert into the next level children
        if self.value == '/' :
        # We are in the root
            if len(word) == 1 :
                self.end = True
            next_char = word[0]
            if next_char in self.children :
            # The char is already there
                self.children[next_char].addWord(word[1:])
            else :
            # The char is not there yet
                New_WordDictionary = WordDictionary()
                New_WordDictionary.modifyValue(next_char)
                self.children[next_char] = New_WordDictionary
                self.children[next_char].addWord(word[1:])
        else :
        # We are not in the root
            if len(word) > 0 :
            # If word reached the end, do nothing
                next_char = word[0]
                if next_char in self.children :
                # The char is already there
                    self.children[next_char].addWord(word[1:])
                else :
                # The char is not there yet
                    New_WordDictionary = WordDictionary()
                    New_WordDictionary.modifyValue(next_char)
                    self.children[next_char] = New_WordDictionary
                    self.children[next_char].addWord(word[1:])
            else :
                self.end = True

    def search(self, word: str) -> bool:
        # Check if the WordDictionary is the root
        if len(word) == 0 :
        # It reach the end of the word, then check if children is empty
            if self.children == {} :
                return True
            else :
                return False
        # Case when word is larger than current max and finish with '.'
        if self.children == {} :
            return False
        # The word still has more chars
        next_char = word[0]
        if next_char == '.' :
        # If next char is '.', then check all the children
            if len(word[1:]) == 0 :
                for i in list(self.children.keys()) :
                    if self.children[i].end :
                        return True
            else :
                for i in list(self.children.keys()) :
                    if self.children[i].search(word[1:]) :
                        return True
        else :
        # If the char is defined, check if is in children recursively
            if next_char in self.children :
                if len(word[1:]) == 0 :
                    return self.children[next_char].end
                else :
                    return self.children[next_char].search(word[1:])
            else :
                return False
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



