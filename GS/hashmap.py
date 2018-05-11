'''
Created on Jan 17, 2018
@author: andrewoliver
'''


class HashMap():

    # This method creates the hashmap by initializing a list with desired size and populates list with None values.
    # Parameter size denotes size of desired list (which is subsequently size of desired hashmap).
    # Parameter size must be greater than 0 or ValueError Exception is thrown.
    def __init__(self, size):
        if (size < 0):
            raise ValueError(
                "The input for size must be an integer greater than 0.")
        self.size = size
        self.hashmap = [None] * self.size  # initial placeholder for length

    # This method is a hash function. It takes in a key and uses Unicode values (from the ord() function), prime number multiplication, and modular arithmetic to generate unique hash codes.
    # Parameter key must be non null or ValueError Exception is thrown.
    def generate_hash(self, key):
        if (key is None):
            raise ValueError("Cannot generate a hash value for null key.")
        hash_code = 11
        for unicode_character in str(key):
            hash_code = (hash_code * 17 + ord(unicode_character)) % self.size
        return hash_code

    # This method takes a key-value pair and inserts it into our hashmap by inserting this key-value pair into our list.
    # It generates a hash code from the given key. Then if this position in the list is empty, the key-value pair is placed into the list.
    # If the position is not empty and the key already exists, the value is updated.
    # If neither of these conditions are true, the key-value pair is appended to the list.
    # Parameter key must be non null or ValueError Exception is thrown.
    def insert(self, key, value):
        if (key is None):
            raise ValueError("Key or Value entered cannot have a null value")

        key_hash_code = self.generate_hash(key)
        kvpair = [key, value]

        if self.hashmap[key_hash_code] is None:
            self.hashmap[key_hash_code] = list([kvpair])
            #print("Key-Value Pair has been added successfully.")
            return True
        else:
            for each_pair in self.hashmap[key_hash_code]:
                if each_pair[0] == key:
                    each_pair[1] = value
                    #print("Key-Value Pair exists already. Value has been updated.")
                    return True
            self.hashmap[key_hash_code].append(kvpair)
            # print("New Key-Value Pair has been added.)"
            return True

    # This method generates a hashcode from the parameter key.
    # If the key is not in the hashmap, the method returns false.
    # If the key is in the hashmap, the method combs through the bucket in which the key exists and removes the desired key-value pair.
    # If neither of these conditions are met, false is returned.
    # Parameter key must be non null or ValueError Exception is thrown.
    def remove(self, key):
        if (key is None):
            raise ValueError(
                "Cannot remove Key-Value Pair with null key entered.")

        key_hash_code = self.generate_hash(key)

        if self.hashmap[key_hash_code] is None:
            #print("Key-Value Pair does not exist and cannot be removed.")
            return False

        for j in range(0, len(self.hashmap[key_hash_code])):
            test = self.hashmap[key_hash_code]
            if test[j][0] == key:
                self.hashmap[key_hash_code].pop(j)
                #print("Key-Value Pair has been removed.")
                return True
        #print("Key-Value Pair has not been removed.")
        return False

    # This method takes a key and generates a hashcode from the key.
    # If the bucket of the hashcode is not empty, the method searches through the bucket and finds the correct key from the key-value pair.
    # Once this has been found, the value is returned.
    # If a key cannot be found, a null value is returned.
    # Parameter key must be non null or ValueError Exception is thrown.
    def get(self, key):
        if (key is None):
            raise ValueError("Cannot get a Key-Value Pair with a null value.")

        key_hash_code = self.generate_hash(key)
        if self.hashmap[key_hash_code] is not None:
            for kvpair in self.hashmap[key_hash_code]:
                if kvpair[0] == key:
                    return kvpair[1]
        return None