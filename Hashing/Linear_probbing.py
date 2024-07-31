# Create Dictionary function using Hashing.
class Dictionary:

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size  # Intitalize array to store keys
        self.data = [None] * self.size  # Initialize array to store value of the key.

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.rehash(hash_value)

                while (
                    self.slots[new_hash_value] != None
                    and self.slots[new_hash_value] != key
                ):
                    new_hash_value = self.rehash(new_hash_value)

                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:
                    self.data[new_hash_value] = value

    # To set the value in dictionary format
    def __setitem__(self, key, value):
        self.put(key, value)

    # Function to get the value
    def get(self, key):
        start_position = self.hash_function(key)
        curr_position = start_position
        while self.slots[curr_position] != None:
            if self.slots[curr_position] == key:
                return self.data[curr_position]
            curr_position = self.rehash(curr_position)
            # means you have looped and came to starting position.
            if curr_position == start_position:
                return "Item Not Found"
        return "Not Found"  # If current postion is None means Item dosent exist.

    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i], ":", self.data[i], end="  ")
        return ""
    # This magic method will allow us to use D1["python"] syntax to fetch the value of key.
    def __getitem__(self, key):
        return self.get(key)

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size  
    
    """for quadratic hashing ,you will be squaring old_hash value every time"""

    def hash_function(self, key):
        # hash function gives you hahing value, and abs convert -ve value inti positive.
        return abs(hash(key)) % self.size  # Giving an index to store key and value.


""" Using __setitem__ magic method we can assign value as dictionary"""
d1 = Dictionary(3)
# d1.put("python", 45)
d1["python"] = 45
# d1.put("java", 34)
d1["java"] = 34
# d1.put("php", 100)
# d1["php"] = 100
# print(d1.slots)
# print(d1.data)
# d1["python"] = 1000
# print(d1.slots)
# print(d1.data)
# ================================
print(d1.get("python"))
print(d1.get("java"))
print(d1.get("c++"))
d1["C++"] = 30
print(d1.get("C++"))
print(d1.slots)
print(d1.data)
print(d1["python"])
print(d1["ggfgg"])
#### Print Dictinary using Magic __str__ function
print(d1)
