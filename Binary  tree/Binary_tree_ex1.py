import collections
# Define  a tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Define insert function
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=' ')
        inOrderPrint(r.right)


def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)


def postOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        postOrderPrint(r.right)
        postOrderPrint(r.left)

# Adjacency List
def makeList(r):
    if r is None:
        return
    else:
        dic[r.data] = []
        
        if r.left:
            dic[r.data].append(r.left.data)
        if r.right:
            dic[r.data].append(r.right.data)    
        makeList(r.left)
        makeList(r.right)
        return dic


# Using Adjacancy list for Breadth First search.
def bfs(al):  # Breadth first search
    queue = collections.deque('g')
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)  # Find Child and add visited node into Visited List.
        for x in al[node]:  # Fetching  adjacant nodes from adjacancy
            # list and adding into queue.
            queue.append(x)
    print(visited)


# Depth First Search , Using Adjacant list here
def dfs(al):  # Here al is adjacancy list which we craeted above.
   
    stack = ['g']
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
                

# Check if Binary tree contains a key coded in python.
# as it is serach we can use Breadth First search or Depth First Search.
def search_key(al, key):
    stack = ['g']
    visited = []
    found = False
    while stack:
        node = stack.pop()
        if node == key:
            found = True
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
    return found


if __name__ == "__main__":
    print("Welcome to Tree")
    root = Node("g")
    root.insert("c")
    root.insert("b")
    root.insert("a")
    root.insert("e")
    root.insert("d")
    root.insert("f")
    root.insert("i")
    root.insert("h")
    root.insert("j")
    root.insert("k")

dic = {}
alist = makeList(root)

# Printing all nodes inorder. 
print("Inorder traversal")
inOrderPrint(root)
# Printing all nodes in preorder.
print("\n\nPreorder Traversal :")
preOrderPrint(root)
print("\n\nPostOrder Traversal :")
postOrderPrint(root)
print("\n\nAdjacency List :")
for ele in alist:
    print(f"{ele} : {dic[ele]}")

print("\n\nBreadth First Search : ")
bfs(alist)

print("\n\nSearch for give node wether exist : ", search_key(alist, 'a'), "\n")