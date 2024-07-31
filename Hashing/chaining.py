"""Hashing Using chaining : in chaining we use of Array of LinkedList means
 each block in array will be LinkedList
 
 Node Class: Defines a node in the linked list with a key, value (data), and a
 pointer to the next node.
 Linked_List Class: Implements the linked list with methods to add, remove,
 traverse, search, and get nodes by index.
 Dictionary Class: Implements the hash table using an array of linked lists,
 with methods to put (insert/update) key-value pairs, search for keys,
 and print the entire table.
 Example Usage: Demonstrates inserting key-value pairs, updating values,
 searching for keys, and removing keys. The print_table method is used to
 print the contents of each bucket in the hash table for verification.

 *** here we are using rehashing technique in chaining  to avoid traverse
  through long linked list and avoid T.C. O(n), with rehashing technique we
  can keep T.C of search O(1) which is constant.****  """


class Node:
    def __init__(self, key, value):
        self.key = key
        self.data = value
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def add(self, key, value):
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def remove(self, key):
        if self.head.key == key:
            self.head = self.head.next
            return

        if self.head == None:
            return "List is Empty"
        else:

            curr = self.head
            while curr:
                if curr.next.key == key:
                    break
                curr = curr.next
            if curr.next == None:
                return "Not Found"
            else:
                curr.next = curr.next.next

    def traverse(self):
        curr = self.head

        while curr != None:
            print(curr.key, ":", curr.data, " ", end=" ")
            curr = curr.next

    def size(self):
        curr = self.head
        counter = 0
        while curr != None:
            counter += 1
            curr = curr.next
        return counter

    def search(self, key):
        pos = 0
        curr = self.head

        while curr is not None:

            if curr.key == key:
                return pos

            curr = curr.next
            pos = pos + 1

        return -1

    def get_node_at_index(self, index):
        curr = self.head
        counter = 0
        while curr != None:
            if counter == index:
                return curr
            curr = curr.next
            counter += 1
        return None


class Dictionary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # LinkedList is one bucket and array o LL is buckets
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        L = []

        for _ in range(capacity):
            L.append(Linked_List())

        return L

    # Magic method to put value as dictionary and not to use put method
    # everytime to insert value
    def __setitem__(self, key, value):  # ex. D1["python"] = 43
        self.put(key, value)

    # Magic method to show get item method as dictionary behavior
    def __getitem__(self, key):  # ex print(D1["python"]) it will give value of python,
        return self.get_item(key)

    def get_item(self, key):
        bucket_index = self.hash_function(key)

        res = self.buckets[bucket_index].search(key)

        if res == -1:
            return None
        else:
            node = self.buckets[bucket_index].get_node_at_index(res)
            return node.data if node else None

    def __delitem__(self, key):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].remove(key)

    def put(self, key, value):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index, key)
        if (
            node_index == -1
        ):  # means that key is no available in the LL so u can add new
            #  insert
            self.buckets[bucket_index].add(key, value)
            self.size += 1
            load_factor = self.size / self.capacity
            print(load_factor)
            if load_factor >= 2:
                self.rehash()
        else:  # otherwise update the value of that key.
            #  update
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.data = value

    """ In rehash function we are assigning old array to old_bucket and 
        resizing old array to new array(double size) and  traverse through
        each item of old array and then traverse through each linked_list at
        each index of the old array and get Node of linked list using
        get_node_at_index function and get key and value of that node and
        pass 'put' function of Dictionary to insert in new created array of
        linked list  """

    def rehash(self):
        self.capacity = self.capacity * 2
        old_buckets = self.buckets  # save whole array in old buckets(aray of LL)
        # make size =0  for new array.
        self.size = 0
        # Make new array of double size capacity
        self.buckets = self.make_array(self.capacity)
        for i in old_buckets:  # Old bucket is array of LinkedList and i is
            # index of each LinkedList
            for j in range(i.size()):  # i.size will give length of linkedlist
                node = i.get_node_at_index(j)  # it will give node at that index
                key_item = node.key
                value_item = node.data
                # Send values to add node to new double size array
                self.put(key_item, value_item)

    def get_node_index(self, bucket_index, key):
        # buckets is array and buckets[bucket_index] is oblject of LL ,
        # so we can access functions of LL class, which is search.
        node_index = self.buckets[bucket_index].search(key)
        return node_index

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def print_table(self):

        for i in range(self.capacity):
            print(f"Bucket{i} : ", end=" ")
            self.buckets[i].traverse()


D1 = Dictionary(4)
D1.put("python", 34)
D1.put("java", 49)
D1.put("cpp", 99)
D1.put("ruby", 56)
D1.put("perl", 90)
D1.put("python", 100)
D1.put("ruby", 1000)
D1.put("ruby1", 10)
D1.put("ruby3", 10)
D1.put("ruby2", 10)
print("Hash Table contents : ")
D1.print_table()


# Check  if the updates and insertion work
print("\nSearching for keys:")
print("Index of python : ", D1.get_node_index(D1.hash_function("python"), "python"))
print("Index of Ruby : ", D1.get_node_index(D1.hash_function("ruby"), "ruby"))

# Remove a key and print table again

print("Removing Java")
D1.buckets[D1.hash_function("java")].remove("java")
D1.print_table()

print("\nRemoving python")
D1.buckets[D1.hash_function("python")].remove("python")
D1.print_table()
print("\n==================================================")
print("Using Magic method, we can add and fetch items as dictionary behaviour")

D1["Python1"] = 500
D1.print_table()
print(D1["Python1"])

del D1["ruby3"]  # delete using magic method
# print(D1) # Using magic function using __str__ funcion
