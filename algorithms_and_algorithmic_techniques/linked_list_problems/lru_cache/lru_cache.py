# LRU Cache - LEast Recently Used
# Building a caching system that has all of the normal functionality of a caching system.
# Insert key -value paris
# Retrieve values by giving keys that are associated to the values
# LRU - comes into play when asked to retreieve the moost recent key, most recently accessed key
# similarly if the cache reaches max capacity and you try to insert another key value pair that
# doesnt already exist in it, then you must evict the least recetly used key


# LRU Cache of size 3

# c --> 3 - the current most recently used key
# b --> 2
# a --> 1 - the current least recently used key

# if we were to call the getCacheValueFromKey method on the key 'a',
# we would return 1, which is the value of a and we would move a to the top of our cache,
# and set a as out new most recently used key and b would become our least recently used key


# Updated LRU Cache of size 3

# a --> 1 - the current most recently used key
# c --> 3
# b --> 2 - the current least recently used key

# since the capacity is 3, if we try to insert a new key for example d-->4, we would
# have to evict the least recenlty used key.

# d --> 4 - the current most recently used key
# a --> 1
# c --> 3 - the current least recently used key

# Now if we wanted to retrieve the key 'b', our LRU cache would return None or null value.

# if we wanted to add in the key value pair 'a' --> 5,
# we would replace the key value pair 'a' --> 1 and
# once it is replaced, we would move 'a' --> 5 to the top of the cache

# a --> 5 - the current most recently used key
# d --> 4
# c --> 3 - the current least recently used key

# all of this should be O(1)

# we need the hash table in order to get that O(1) lookup with the key value pair
# every other operation for the LRU cache can be satisfied with a linked list

# what if we combined the two and had a hash table that maps to nodes in a doubly linked list

# HashTable(Cache)    LinkedList
# c     ------>       (c-->3) <- head node
#                        ↕
# b     ------>       (b-->2)
#                        ↕
# a     ------>       (a-->1) <- tail node


# to add a value d --> 4 for example, we check in our cache to see if the key already exists.
    # if the key exists, replace the value and move the pair to the top of the cache.
    # if the key does NOT exist, add the key value pair and move the pair to the top of the cache

# then we check to see what the size of our cache is, in comparison to the capacity.
    # if the size our cache is already at capacity, we remove the Least Recently Used key value pair
    # and add the new pair to the top of the cache
    # if current size is NOT at capacity, increment current size, and we add the key value pair to the top of the cache

# the values that are stored for the keys are stored as nodes in a doubly linked list
# so when moving a pair to the top of the cache,
# you have to set the value to be the head node of the doubly linked list.

# These implementations run in O(1) time and doesnt use any auxiliary space O(1)
class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()


    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            # case 1 --> evict the LRU key value pair because we are at capacity
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            # case 2 --> we are not at capacity so we can just insert the key value pair and move it to be the head node.
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        return self.listOfMostRecent.head.key

    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("Provided key is not in the cache.")
        self.cache[key].value = value







class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head==node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None








