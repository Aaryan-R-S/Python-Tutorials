import random
print(" ")
print("Welcome to My Kirana Store!")

items = []
prices = []
customerId = None

def customer (r):
    print(f"\nCustomer Id. ------------------------- {r}")
    while True:
        print("\nPress Enter when list is completed\n")
        item = input("Enter Item's Name : ")
        if item != "":
            items.append(item)
        else:
            break
        price = int(input("Enter Item's Price : "))
        prices.append(price)

def receipt(r):
    print(f"\nCustomer Id. ------------------------- {r}")
    total = 0

    for i in range(len(items)):
        print(f'{i+1}. {items[i]} ...... {prices[i]}.00 Rs')
        total += prices[i]
        
    print(f"Total Amount to be paid -------------- {total} Rs\n")


if __name__ == "__main__":
    while True:
        print("\nEnter \"Ctrl+c\" to leave the program!")
        r = random.randint(10000,99999)
        customer(r)    
        receipt(r)    