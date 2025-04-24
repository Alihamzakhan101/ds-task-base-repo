# main.py

# This file contains a menu-driven application to perform basic data structure operations.
# Students are expected to implement missing features or enhance existing ones.

def display_menu():
    print("\nData Structure Task App")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. dequeue operations")
    print("4. Dictionary Operations")
    print("5. Exit")

def stack_operations():
    stack = []
    print("\n-- Stack Operations --")
    while True:
        print("1. Push\n2. Pop\n3. Display\n4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to push: ")
            stack.append(item)
        elif choice == "2":
            if stack:
                print("Popped item:", stack.pop())
            else:
                print("Stack is empty.")
        elif choice == "3":
            print("Stack content:", stack)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def queue_operations():
    # TODO: Implement queue using list or collections.deque
    print("\n-- Queue Operations --")
    print("TODO: Implement this feature")
    
def deque_operations():
    d = deque()
    print("\n-- Deque Operations --")
    while True:
        print("1. Append Right\n2. Append Left\n3. Pop Right\n4. Pop Left\n5. Display\n6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to append right: ")
            d.append(item)
        elif choice == "2":
            item = input("Enter item to append left: ")
            d.appendleft(item)
        elif choice == "3":
            if d:
                print("Popped item from right:", d.pop())
            else:
                print("Deque is empty.")
        elif choice == "4":
            if d:
                print("Popped item from left:", d.popleft())
            else:
                print("Deque is empty.")
        elif choice == "5":
            print("Deque content:", list(d))
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
            
def dictionary_operations():
    # TODO: Implement basic dictionary operations like add, delete, search, display
    print("\n-- Dictionary Operations --")
    print("TODO: Implement this feature")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            stack_operations()
        elif choice == "2":
            queue_operations()
        elif choice == "3":
            dictionary_operations()
        elif choice == "4":
            print("Exiting... Goodbye!")
            
        else:
            print("Invalid choice.")
            
def test():
    print("Testing")

if __name__ == "__main__":
    main()
