class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack empty")

    def print_stack(self):
        print(self.stack)

    def size(self):
        return len(self.stack)


def menu():
    stack = None
    while True:
        print("1. create stack")
        print("2. push item")
        print("3. pop item")
        print("4. peek next element")
        print("5. check if stack is empty")
        print("6. check if stack is full")
        print("7. print stack")
        print("8. stack size")
        print("9. exit")
        choice = int(input("enter number of choice: "))

        if choice == 1:
            max_size = int(input("enter max size of stack: "))
            stack = Stack(max_size)
        elif choice == 2:
            if stack is not None:
                item = input("enter item to push: ")
                stack.push(item)
            else:
                print("create a stack first")
        elif choice == 3:
            if stack is not None:
                stack.pop()
            else:
                print("create a stack first")
        elif choice == 4:
            if stack is not None:
                print("next element:", stack.peek())
            else:
                print("create a stack first")
        elif choice == 5:
            if stack is not None:
                print("stack is empty:", stack.is_empty())
            else:
                print("create a stack first")
        elif choice == 6:
            if stack is not None:
                print("stack is full:", stack.is_full())
            else:
                print("create a stack first")
        elif choice == 7:
            if stack is not None:
                stack.print_stack()
            else:
                print("create a stack first")
        elif choice == 8:
            if stack is not None:
                print("stack size:", stack.size())
            else:
                print("create a stack first")
        elif choice == 9:
            break
        else:
            print("invalid choice, please try again")


if __name__ == "__main__":
    menu()
