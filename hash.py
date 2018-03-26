# Create a hash table with add/delete/lookup methods


class HashMap:
    """Hash map inits with a map of a given size (m), map method, remove from map
    method, lookup method
    """

    def __init__(self, map_size):
        self.hash_map = self.create_map(map_size)

    def create_map(self, map_size):
        map = []
        for i in range(map_size):
            map.append(None)
        return map

    def hash_key(self, key):
        pass

    def insert(self, item):
        # Hashes a key and places key/value in index in map
        pass

    def remove(self, item):
        pass

    def lookup(self, hashtable, key):
        # Give a hashed list, lookup based on a given
        pass

    def __str__(self):
        return "Hashmap with {} buckets.".format(len(self.hash_map))

    def __len__(self):
        return len(self.hash_map)

    def __getitem__(self, position):
        return self.hash_map[position]
