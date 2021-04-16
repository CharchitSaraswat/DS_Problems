def print_hash(hash_table):
    for i in range(len(hash_table)):
        print(i, end=" ")
        for j in hash_table[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()

def hashing_func(key):
    return key%len(hash_table)

def insert_hash(key, value, hash_table):
    hashing_key = hashing_func(key)
    hash_table[hashing_key].append(value)

hash_table = [[] for i in range(10)]
insert_hash(1, "ABCD", hash_table)
insert_hash(2, "XYZ", hash_table)
insert_hash(11, "PQRST", hash_table)
insert_hash(4, "dhakhd", hash_table)
insert_hash(31, "askdaskhd", hash_table)
print_hash(hash_table)
