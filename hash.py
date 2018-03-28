# Create a hash table with add/delete/lookup methods


class HashMap:
    """Hash map inits with a map of a given size (m), map method, remove from map
    method, lookup method
    """

    def __init__(self, map_size=17):
        self.hash_map = self.create_initial_map(map_size)
        self.map_size = len(self.hash_map)

    def create_initial_map(self, map_size):
        map = []
        for i in range(map_size):
            map.append(None)
        return map

    def hash_function(self, key):
        ascii_sum = 0

        for item in str(key):
            if type(item) == int:
                ascii_sum += chr(item)
            else:
                ascii_sum += ord(item)

        return ascii_sum

    def get_index(self, key):
        return self.hash_function(key) % self.map_size

    def insert(self, key, value):
        index = self.get_index(key)
        current_value = self.hash_map[index]

        if current_value is not None:
            if isinstance(current_value, list):
                self.hash_map[index].append((key, value))
            else:
                self.hash_map[index] = [current_value, (key, value)]
        else:
            self.hash_map[index] = (key, value)

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
