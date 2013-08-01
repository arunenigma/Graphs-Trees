class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        return str(self.value)
        
class BST(object):
    """
    Binary Search Tree
    """
    def __init__(self):
        self.root = None
        
    def addNode(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            
            while 1:  # infinite loop
                if value <= current.value:
                    if current.left:  # meaning current.left is not None
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                elif value > current.value:
                    if current.right: 
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                else:
                    break
                    
    def BFS(self):
        """
        Breadth First Search
        """ 
        self.root.level = 0 # root level is always 0; initially it was None
        queue = [self.root]
        out = []
        current_level = self.root.level
 
        while len(queue) > 0:  # when stack not empty     
            current_node = queue.pop(0)  # list used as a Queue FIFO
            out.append(str(current_node) + ' ')
            
            if current_node.level > current_level:
                current_level += 1
                
            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  
            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)                
        print ''.join(out) 
    
    def inorder(self, node):
        """
            Depth First Traversal (DFS)
            Symmetric
            Pattern: Left, Root, Right
        """
        if node is not None:
            self.inorder(node.left)
            print node.value,
            self.inorder(node.right)
            
    def preorder(self,node): 
        """
            Depth First Traversal (DFS)
            Asymmetric
            Pattern: Root, Left, Right
        """
        if node is not None:
            print node.value,
            self.preorder(node.left)
            self.preorder(node.right)
 
    def postorder(self,node):
        """
            Depth First Traversal (DFS)
            Asymmetric
            Pattern: Left, Right, Root
        """
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.value, 
             

tree = BST()
lst = [2, 1, 3, 6, 7, 4, 1, 3, 1, 4, 7, 11, 4, 45, 2]
for i in lst:
    tree.addNode(i)
print 'Breadth First Traversal'
tree.BFS()
print '\n' 
print 'Inorder Traversal'
tree.inorder(tree.root) 
print '\n' 
print 'Preorder Traversal' 
tree.preorder(tree.root) 
print '\n' 
print 'Postorder Traversal'
tree.postorder(tree.root)           
