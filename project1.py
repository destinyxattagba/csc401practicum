import random
def randomize_in_place(array):
    n = len(array)-1
    for index in range(len(array)):
        print("current array: ", array, "current index: ", index)
        randint = random.randint(index, n)
        print("Generated random number: ", randint)
        array[index], array[randint] = array[randint] , array[index]
        print("new array: ", array)
