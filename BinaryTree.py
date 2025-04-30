class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert(node.right, key)

    def delete(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self.delete(node.left, key)
        elif key > node.val:
            node.right = self.delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get inorder successor (smallest in the right subtree)
            min_larger_node = self.findMin(node.right)
            node.val = min_larger_node.val
            node.right = self.delete(node.right, min_larger_node.val)
        return node

    def find(self, node, key):
        if node is None:
            return None
        if node.val == key:
            return node
        if key < node.val:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def preorder(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=' ')

    def sum_of_nodes(self, node):
        if node is None:
            return 0
        return node.val + self.sum_of_nodes(node.left) + self.sum_of_nodes(node.right)

    def findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def findMax(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

def menu():
    tree = BinaryTree()

    while True:
        print("\nBinary Tree Operations Menu:")
        print("1. Insert")
        print("2. Delete")
        print("3. Find")
        print("4. Print Preorder")
        print("5. Print Inorder")
        print("6. Print Postorder")
        print("7. Sum of all nodes")
        print("8. Find Minimum")
        print("9. Find Maximum")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter integer to insert: "))
            tree.insert(tree.root, val)
        elif choice == '2':
            val = int(input("Enter integer to delete: "))
            tree.root = tree.delete(tree.root, val)
        elif choice == '3':
            val = int(input("Enter integer to find: "))
            result = tree.find(tree.root, val)
            if result:
                print(f"Found: {result.val}")
            else:
                print("Not found.")
        elif choice == '4':
            print("Preorder Traversal:")
            tree.preorder(tree.root)
            print()
        elif choice == '5':
            print("Inorder Traversal:")
            tree.inorder(tree.root)
            print()
        elif choice == '6':
            print("Postorder Traversal:")
            tree.postorder(tree.root)
            print()
        elif choice == '7':
            total = tree.sum_of_nodes(tree.root)
            print(f"Sum of all nodes: {total}")
        elif choice == '8':
            if tree.root:
                print(f"Minimum value: {tree.findMin(tree.root).val}")
            else:
                print("Tree is empty.")
        elif choice == '9':
            if tree.root:
                print(f"Maximum value: {tree.findMax(tree.root).val}")
            else:
                print("Tree is empty.")
        elif choice == '10':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    menu()
