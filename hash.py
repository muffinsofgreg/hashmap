# Create a hash table with add/delete/lookup methods


class HashMap:
    """
    Hash map inits with a list of a given size (m);
    Keywords: map_size (default = 17)
    """

    def __init__(self, map_size=17):
        self.hash_map = self.create_map(map_size)
        self.map_size = len(self.hash_map)

    def create_map(self, map_size):
        map = []
        for i in range(map_size):
            map.append(None)
        return map

    def hash(self, key):
        """
        For a given key, hashes the key into an int value
        Keywords: key
        returns: int
        """
        ascii_sum = 0

        if type(key) == int:
            ascii_sum += ord(chr(key))
        else:
            for item in key:
                ascii_sum += ord(item)

        return ascii_sum

    def get_index(self, key):
        """
        For a given key, invokes hash() and returns an index value n-1
        where n is the size of the Hash Map
        keywords: key
        returns: int
        """
        return self.hash(key) % self.map_size

    def insert(self, key, value):
        index = self.get_index(key)
        current_value = self.hash_map[index]

        if current_value is not None:
            if isinstance(current_value, list): # if current value already exists as a list
                for i in range(len(current_value)):
                    if current_value[i][0] == key and current_value[i][1] == value: # if (key, value) already exist, pass
                        break
                    elif current_value[i][0] == key: # if key already exists, but new value, update (key, value)
                        self.hash_map[index][i] = (key, value)
                        break
                    else:
                        pass
                else: # else, append list with new (key, value)
                    self.hash_map[index].append((key, value))

            else:
                if current_value[0] == key: # if not list, but current value, then must be single tuple
                    if current_value[1] == value:  # If keys and value are the same, break
                        pass
                    else:  # if just keys are the same, update value to new value
                        self.hash_map[index] = (key, value)
                else:  # turn tuple into a list of tuples
                    self.hash_map[index] = [current_value, (key, value)]
        else: # finally, if no current_value, create (key, value) tuple
            self.hash_map[index] = (key, value)

    def remove(self, key):
        pass

    def lookup(self, key):
        index = self.get_index(key)
        lookup_value = self.hash_map[index]

        if lookup_value is None:
            raise KeyError('{}'.format(key))
        elif isinstance(lookup_value, list):
            for each in lookup_value:
                if each[0] == key:
                    return each[1]
            else:
                raise KeyError('{}'.format(key))
        else:
            if key == lookup_value[0]:
                return lookup_value[1]
            else:
                raise KeyError('{}'.format(key))

    def __str__(self):

        def print_bucket_summary():
            return "Hashmap with {} buckets.\n\n".format(len(self.hash_map))

        def print_map():
            string = ""
            for i in range(len(self.hash_map)):
                string += "{0} | {1}\n".format(i, self.hash_map[i])
            return string

        return print_bucket_summary() + print_map()

    def __repr__(self):
        return str(self.hash_map)

    def __len__(self):
        return len(self.hash_map)

    def __getitem__(self, position):
        return self.hash_map[position]
