class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
    def how_many(node):
        if not node:
            return 0
        elif node.info in [v1,v2]:
            return 1 + how_many(node.left) + how_many(node.right)
        else:
            return 0 + how_many(node.left) + how_many(node.right)
        
    left_has_2 = how_many(root.left) == 2
    right_has_2 = how_many(root.right) == 2
    
    if not any((left_has_2, right_has_2)):
        return root
    else:
        if left_has_2:
            return lca(root.left, v1, v2)
        elif right_has_2:
            return lca(root.right, v1, v2)
            
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
