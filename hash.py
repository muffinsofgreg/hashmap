# Create a hash table with add/delete/lookup methods


class HashMap:
    """Hash map inits with a map of a given size (m), map method, remove from map
    method, lookup method
    """

    def __init__(self, map_size=15):
        self.hash_map = self.create_initial_map(map_size)

    def create_intial_map(self, map_size):
        map = []
        for i in range(map_size):
            map.append(None)
        return map

    def hash_function(self, key):
        ascii_sum = 0

        for item in key:
            if type(item) == int:
                ascii_sum += chr(item)
            else:
                ascii_sum += ord(item)

        remainder = ascii_sum % len(self.hash_map)
        return remainder

    def insert(self, key, value):
        # Hashes a key (hash_function) and places key/value in index in map
        pass

    def remove(self, key):
        pass

    def lookup(self, key):
        # Give a hashed list, lookup based on a given
        pass

    def __str__(self):
        return "Hashmap with {} buckets.".format(len(self.hash_map))

    def __len__(self):
        return len(self.hash_map)

    def __getitem__(self, position):
        return self.hash_map[position]
