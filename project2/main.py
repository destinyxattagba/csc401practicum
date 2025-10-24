from project2.project2 import insert_key


def main():
    print("Welcome to the custom Hash Table")

    key = input("please enter the key value you would like to insert into the table, 00 to exit:")
    while int(key) !=00:
        insert_key(int(key))
    print("User exited. Goodbye.")

if __name__ == '__main__':
    main()


