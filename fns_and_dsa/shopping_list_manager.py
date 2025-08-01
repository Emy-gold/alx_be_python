def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: ").strip())
        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add:").strip()
            shopping_list.append(item)
            print(f"'{item} is added correctly'")
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' is removed succefuly")
            else :
                print(f"'{item}' is not found")    
        elif choice == 3:
            if not shopping_list:
                print("The list is empty")
            else:
                index = 1
                for item in shopping_list:
                    print(index, item)
                    index+=1
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()