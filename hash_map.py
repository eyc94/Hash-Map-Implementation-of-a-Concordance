# hash_map.py
# ===================================================
# Implement a hash map with chaining
# ===================================================

class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
            key: the key for the new node
            value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """Removes node from linked list
        Args:
            key: key of the node to remove """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
            key: key of node
        Return:
            node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Creates a new hash map with the specified number of buckets.
    Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
    """

    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.
        """

        for i in range(self.capacity):
            self._buckets[i].head = None
        self.size = 0

    def get(self, key):
        """
        Returns the value with the given key.
        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """

        # Handles the case in which the capacity of the array of buckets is 0.
        if self.capacity == 0:
            return None

        hash = self._hash_function(key)  # Hash the key.
        index = hash % self.capacity  # Find the index from the hash.

        current_bucket = self._buckets[index]  # Grab the bucket at that index.

        if current_bucket.head is None:  # This accounts for an empty bucket (empty LinkedList).
            return None
        else:  # If the bucket is not empty, iterate and try to find the key.
            current = current_bucket.head  # Set a current pointer to iterate with.
            while current is not None:  # Iterate while pointer is not None.
                if current.key == key:  # If the pointer's key is what we're looking for.
                    return current.value  # Return that key's value.
                else:  # If the key is not what we're looking for, move pointer.
                    current = current.next
        return None  # Return None if we've exhausted our search.

    def resize_table(self, capacity):
        """
        Resizes the hash table to have a number of buckets equal to the given
        capacity. All links need to be rehashed in this function after resizing
        Args:
            capacity: the new number of buckets.
        """

        # Create a new hash table that is empty.
        new_buckets = []
        for i in range(capacity):  # Fill that hashtable with empty LinkedLists.
            new_buckets.append(LinkedList())

        # Reset the size
        self.size = 0

        # Iterate through the old hash table.
        for i in range(self.capacity):
            if self._buckets[i].head is not None:
                current = self._buckets[i].head
                while current is not None:
                    key_to_transfer = current.key  # Grab the key you want to copy over.
                    value_to_transfer = current.value  # Grab the value you want to copy over.
                    new_hash = self._hash_function(key_to_transfer)
                    new_index = new_hash % capacity

                    new_list = new_buckets[new_index]

                    if new_list.contains(key_to_transfer):
                        list_pointer = new_list.head
                        found = False
                        while list_pointer is not None and not found:
                            if list_pointer.key == key_to_transfer:
                                found = True
                                list_pointer.value = value_to_transfer
                            else:
                                list_pointer = list_pointer.next
                    else:
                        new_list.add_front(key_to_transfer, value_to_transfer)
                        self.size += 1

                    current = current.next

        self.capacity = capacity
        self._buckets = new_buckets

    def put(self, key, value):
        """
        Updates the given key-value pair in the hash table. If a link with the given
        key already exists, this will just update the value and skip traversing. Otherwise,
        it will create a new link with the given key and value and add it to the table
        bucket's linked list.

        Args:
            key: they key to use to has the entry
            value: the value associated with the entry
        """
        
        # Handle the case in which the hashmap is completely empty with a capacity of 0.
        if self.capacity == 0:
            return None
        
        hash = self._hash_function(key)  # First, place the new key inside a hash function.
        index = hash % self.capacity  # This is the index into the array of buckets.

        current_bucket = self._buckets[index]  # Use the index to grab the LinkedList at that bucket.

        # Must check to see if the current bucket contains the key we want to add.
        if current_bucket.contains(key):  # If the current bucket contains the key we want to add, update the existing value.
            # First, find the node to update.
            current_node = current_bucket.head  # Pointer to iterate through list.
            found = False
            while current_node is not None and not found:  # Iterate until you hit the end or you find the node.
                if current_node.key == key:  # Found the key.
                    found = True  # Update flag
                    current_node.value = value  # Update the value at that key.
                else:  # If the key is not the right key
                    current_node = current_node.next  # Move along.
        else:  # If the current bucket does not contain the key we want to add to front.
            current_bucket.add_front(key, value)
            self.size = self.size + 1  # Increment size.

    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.
        Args:
            key: they key to search for and remove along with its value
        """

        # Handle the case in which the hashmap is completely empty with a capacity of 0.
        if self.capacity == 0:
            return None
        
        hash = self._hash_function(key)  # Hash the key.
        index = hash % self.capacity  # Calculate the index into the array of buckets.

        current_bucket = self._buckets[index]  # Grabs the bucket at the index. 
        current_bucket.remove(key)  # Uses the LinkedList's remove function to remove the node with the key.
        self.size -= 1  # Decrement size by 1.

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table

        Returns:
            True if the key is found False otherwise

        """

        hash = self._hash_function(key)  # Hash the key
        index = hash % self.capacity  # Calculate the index.

        current_bucket = self._buckets[index]  # Grab the bucket at the index.

        if current_bucket.head is None:  # If that bucket is empty, return False.
            return False
        else:  # If the bucket is not empty, search for the key.
            current_pointer = current_bucket.head  # Pointer that iterates.
            while current_pointer is not None:  # Iterate until the pointer reaches the end.
                if current_pointer.key == key:  # If the current pointer's key is what we're looking for.
                    return True  # Return true.
                else:  # Otherwise, increment the pointer.
                    current_pointer = current_pointer.next

        # Pointer reached the end and could not find the key we're looking for.
        return False

    def empty_buckets(self):
        """
        Returns:
            The number of empty buckets in the table
        """

        # Initialize variable to count number of empty buckets.
        number_of_empty = 0

        # Iterate through all existing buckets.
        for i in range(self.capacity):
            if self._buckets[i].head is None:  # If the bucket is empty.
                number_of_empty += 1  # Increment count.

        return number_of_empty  # Return the number of empty buckets.

    def table_load(self):
        """
        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.

        """

        load_factor = self.size / self.capacity
        return load_factor

    def __str__(self):
        """
        Prints all the links in each of the buckets in the table.
        """

        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out
