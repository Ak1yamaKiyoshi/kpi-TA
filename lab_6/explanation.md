
### Hashing Functions Explanation

#### Cuckoo Hashing

Cuckoo hashing uses two hash functions to resolve collisions. When a collision occurs, the existing item is displaced to its alternate location, determined by the second hash function. This process repeats until all items are placed without collision or a loop is detected.

**Hash Functions:**
```py
def hash1(self, key):
    return abs(hash(key)) % self.table_size

def hash2(self, key):
    return (abs(hash(key)) * 5) % self.table_size
```

- `hash1` calculates a position using the modulo of the table size.
- `hash2` uses a different strategy, multiplying the hash by 5 before modulo, to ensure a different distribution.

**Insertion Example:**
```py
def insert_cuckoo(self, key, value, count=0, table=1):
    if count > self.table_size:
        return False
    if table == 1:
        hash_index = self.hash1(key)
        if self.hash_table1[hash_index] is None:
            self.hash_table1[hash_index] = (key, value)
            return True
        else:
            displaced_key, displaced_value = self.hash_table1[hash_index]
            self.hash_table1[hash_index] = (key, value)
            return self.insert_cuckoo(displaced_key, displaced_value, count + 1, 2)
    else:
        hash_index = self.hash2(key)
        if self.hash_table2[hash_index] is None:
            self.hash_table2[hash_index] = (key, value)
            return True
        else:
            displaced_key, displaced_value = self.hash_table2[hash_index]
            self.hash_table2[hash_index] = (key, value)
            return self.insert_cuckoo(displaced_key, displaced_value, count + 1, 1)
```

#### Hopscotch Hashing

Hopscotch hashing aims to keep items close to their original hash index but allows for a "hop" within a small range to resolve collisions. This method isn't fully implemented in the provided code but is indicated by the `display_hopscotch_hashing` method.

**Display Function:**
```py
def display_hopscotch_hashing(self):
    output = "Hopscotch Hashing:\n"
    for i, item in enumerate(self.hash_table1):
        if item is not None:
            hop_info = self.calculate_hop_information(i, self.hash1(item[0]))
            output += f"Table 1 - {i} [Hop: {hop_info}]: {item[0]}, {item[1]}\n"
    for i, item in enumerate(self.hash_table2):
        if item is not None:
            hop_info = self.calculate_hop_information(i, self.hash2(item[0]))
            output += f"Table 2 - {i} [Hop: {hop_info}]: {item[0]}, {item[1]}\n"
```

The `calculate_hop_information` function, which would calculate the distance (hop) from the original hash index, is used to display how far an item has moved from its initial position. This is a placeholder for the actual hopscotch logic.
```py
def calculate_hop_information(self, current_index, original_hash):
    return abs(current_index - original_hash)
```
