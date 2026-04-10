class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []

        # キーが既に存在する場合は更新
        for pair in self.data_map[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # 新規追加
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]

        return None

    def keys(self):
        all_keys = []

        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_keys.append(pair[0])

        return all_keys


my_hash_table = HashTable()
my_hash_table.set_item("banana", 1400)
my_hash_table.set_item("apple", 800)
my_hash_table.set_item("orange", 100)
print(my_hash_table.keys())
print(my_hash_table.get_item("apple"))

my_hash_table.print_table()