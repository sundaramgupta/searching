def main():
    a = [2, 4, 5, 6, 7, 9, 10, 32, 62]
    key = int(input("Enter the key to be searched for: "))
    size = len(a)
    interpo_search(a, key, size)

def interpo_search(a, key, size):
    l = 0
    h = size-1

    while l <= h:
        mid = l + ((key-a[l])//(a[h]-a[l])*(h-l))
        if key == a[mid]:
            print(mid)
            return
        elif key < a[mid]:
            h = mid - 1
        else:
            l = mid + 1
    print("Not found")
main()
