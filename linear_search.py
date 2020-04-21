def main():
    a = [2,4,5,6,7,9,10,32,62]
    key = int(input("Enter the key to be searched for: "))
    linear_search(a,key)

def linear_search(a,key):
    for ele in a:
        if ele==key:
            print(a.index(ele))
            return
    print("Key not in the list")
    
main()
