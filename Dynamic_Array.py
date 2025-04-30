class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def expand_capacity(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def append(self, value):
        if self.size == self.capacity:
            self.expand_capacity()
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            print("Invalid index!")
            return
        if self.size == self.capacity:
            self.expand_capacity()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index!")
            return
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def display(self):
        print("Current Strings:", [self.array[i] for i in range(self.size)])


def menu():
    dynamic_array = DynamicArray()
    while True:
        print("\nMenu:")
        print("1. Append string")
        print("2. Insert string specific position")
        print("3. Remove string specific position")
        print("4. Display all strings")
        print("5. Exit")
        
        choice = input("Enter the number of the option you want to choose: ")
        
        if choice == "1":
            value = input("Enter string to append: ")
            dynamic_array.append(value)
        elif choice == "2":
            index = int(input("Enter index to insert at: "))
            value = input("Enter string to insert: ")
            dynamic_array.insert(index, value)
        elif choice == "3":
            index = int(input("Enter index to remove: "))
            dynamic_array.remove(index)
        elif choice == "4":
            dynamic_array.display()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()
