import math


def main():
    a = [2, 4, 5, 6, 7, 9, 10, 32, 62]
    key = int(input("Enter the key to be searched for: "))
    size = len(a)
    jump_search(size, key, a)


def jump_search(size, key, a):
    block_size = int(math.sqrt(size))
    low = 0
    high = block_size-1

    while key > a[high] and block_size < size:
        low = high
        high = high + block_size
        if high >= size:
            high = size
    for ele in a:
        if ele == key:
            print(a.index(ele))
            return
    print("Not found")


main()
