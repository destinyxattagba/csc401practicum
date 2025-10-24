
#hashfunctions
TABLE_SIZE = 16
hashtable = [None] * TABLE_SIZE

def insert_key(key):
    h1 = key % 16
    h2 = 2 * (key % 4) +1
    i=0
    hash_function = ((h1 + (i * h2)) % 16 )
    if check_if_empty(hash_function) is True:
        hashtable[hash_function] = key
        print("key", key, "inserted at slot ", hash_function)
        print("current table: ", hashtable)
    else:
        while check_if_empty(hash_function) is False:
            print("collision at slot ", hash_function, "!")
            i=i+1
            print("attempt ", i)
            hash_function = ((h1 + (i * h2)) % 16)
        print("key", key, "inserted at slot ", hash_function)
        hashtable[hash_function] = key
        print("current table: ", hashtable)

def check_if_empty(slot):
    if hashtable[slot] is None:
        return True
    else:
        return False

def main():
    print("Welcome to the custom Hash Table")

    key = input("please enter the key value you would like to insert into the table, 00 to exit:")
    while int(key) !=00:
        insert_key(int(key))
        key = input("please enter the key value you would like to insert into the table, 00 to exit:")
    print("User exited. Goodbye.")

if __name__ == '__main__':
    main()



