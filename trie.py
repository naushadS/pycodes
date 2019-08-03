from typing import Tuple
class TrieNode(object):
    def __init__(self, char:str):
        self.char = char
        self.children = []
        self.counter = 1
        self.last_node = False
    
    def add(self, word:str):
        node = self
        for char in word:
            char_found = False
            for child in node.children:
                if child.char == char:
                    char_found = True
                    child.counter += 1
                    node = child
                    break
            if not char_found:
                charNode = TrieNode(char)
                node.children.append(charNode)
                node = charNode
        node.last_node = True

    def find_prefix(self, prefix:str) -> Tuple[bool,int]:
        node = self
        word_found = False
        if not root.children:
            return False, 0
        for char in prefix:
            char_present = False
            for child in node.children:
                if char == child.char:
                    char_present = True
                    node = child
                    break
            if not char_present:
                return False, 0
        return True, node.counter

    #def find_word(self, word : str):
        

if __name__ == "__main__":
    root = TrieNode('*')
    root.add("hackathon")
    root.add('hack')

    print('hac',root.find_prefix('hac'))
    print('hack',root.find_prefix('hack'))
    print('hackathon',root.find_prefix('hackathon'))
    print('ha',root.find_prefix('ha'))
    print('hammer',root.find_prefix('hammer'))
