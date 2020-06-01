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

        for i in range(self.size):
        	self._buckets[i] = None
        self.size = 0

    def get(self, key):
        """
        Returns the value with the given key.
        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """
        # FIXME: Write this function

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
        
        # This is the hashed key. In other words, this is the index for the list.
        hash = self._hash_function(key)
        index = hash % self.capacity  # This accounts for the case in which the hashed key is larger than the size of the list.

        # Have a pointer point to a linked list at the location in the list.
        the_list = self._buckets[index]

        # Check to see if that bucket contains the original key.
        if the_list.contains(key):  # If the bucket contains the key, update the value of the key to the new value.
        	# Iterate through the list until the key is found.
        	current = the_list.head  # Pointer for iteration.
        	found = False  # Boolean flag.
        	while current is not None and not found:  # Iterate until it reaches the end or until key found.
        		if current.key == key:  # If the current pointer's key is found.
        			found = True
        			current.value = value  # Update value.
        		else:  # If the key is not at the current pointer, increment pointer.
        			current = current.next

        else:  # If the bucket does not contain the key, add the key to the front.
        	the_list.add_front(key, value)
        	self.size += 1  # Increment size

    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.
        Args:
            key: they key to search for and remove along with its value
        """
        
        # Calculate the hashed key.
        hash = self._hash_function(key)
        index = hash % self.capacity

        the_list = self._buckets[index]
        the_list.remove(key)
        self.size -= 1

        # Find the original key in the linked list. (Iterate through the whole list).
        # If found, remove that original key/value pair.
        # If not found, do nothing.

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table

        Returns:
            True if the key is found False otherwise

        """

        hash = self._hash_function(key)  # Calculate the hash key.
        index = hash % self.capacity  # Calculate the index into the hash table.

        the_list = self._buckets[index]  # Assign a pointer to the list in the specific bucket.

        if the_list.head is None:  # If the linkedlist is empty, return False.
        	return False
		
		# If the linkedlist is not empty, the key exists.
        return True

    def empty_buckets(self):
        """
        Returns:
            The number of empty buckets in the table
        """
        # FIXME: Write this function

    def table_load(self):
        """
        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.

        """
        # FIXME: Write this function

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
