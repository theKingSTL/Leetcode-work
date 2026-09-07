class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str) -> list[list[str]]:
        class Node:
            def __init__(self):
                self.children = {}
                self.suggested = []
            def append(self, product):
                if len(self.suggested) < 3:
                    self.suggested.append(product)

        
        #build product page 
        products.sort()
        root = Node()
        for p in products:
            node = root
            for char in p:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
                node.append(p)
        
        node = root
        ans = []
        for letter in searchWord:
            if node is not None and letter in node.children:
                node = node.children[letter]
                ans.append(node.suggested)
            else:
                node = None
                ans.append([])
        
        return ans 
            
            



