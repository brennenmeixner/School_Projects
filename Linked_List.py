class Node:
    def __init__(self, name, roll_number, course, total_marks):
        self.name = name
        self.roll_number = roll_number
        self.course = course
        self.total_marks = total_marks
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def check_record(self, roll_number):
        """Check if a record with the given roll number exists"""
        temp = self.head
        while temp:
            if temp.roll_number == roll_number:
                return True
            temp = temp.next
        return False

    def create_record(self, name, roll_number, course, total_marks):
        """Create a new student record (node)"""
        if self.check_record(roll_number):
            print("Record with Roll Number {} already exists.".format(roll_number))
            return
        new_node = Node(name, roll_number, course, total_marks)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Record Inserted Successfully")

    def search_record(self, roll_number):
        """Search a record by roll number"""
        temp = self.head
        while temp:
            if temp.roll_number == roll_number:
                print(f"Student Name: {temp.name}, Roll Number: {temp.roll_number}, Course: {temp.course}, Total Marks: {temp.total_marks}")
                return
            temp = temp.next
        print("Record not found.")

    def delete_record(self, roll_number):
        """Delete a student record by roll number"""
        temp = self.head
        prev = None
        while temp:
            if temp.roll_number == roll_number:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                del temp
                print("Record Deleted Successfully")
                return 0
            prev = temp
            temp = temp.next
        return -1

    def show_records(self):
        """Display all student records"""
        if not self.head:
            print("No records found.")
            return
        temp = self.head
        while temp:
            print(f"Student Name: {temp.name}, Roll Number: {temp.roll_number}, Course: {temp.course}, Total Marks: {temp.total_marks}")
            temp = temp.next

def main():
    student_list = StudentLinkedList()

    while True:
        print("\nStudent Record Menu:")
        print("1. Create Record")
        print("2. Search Record")
        print("3. Delete Record")
        print("4. Show All Records")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter Name of Student: ")
            roll_number = int(input("Enter Roll Number of Student: "))
            course = input("Enter Course of Student: ")
            total_marks = int(input("Enter Total Marks of Student: "))
            student_list.create_record(name, roll_number, course, total_marks)

        elif choice == 2:
            roll_number = int(input("Enter Roll Number to Search: "))
            student_list.search_record(roll_number)

        elif choice == 3:
            roll_number = int(input("Enter Roll Number to Delete: "))
            result = student_list.delete_record(roll_number)
            if result == -1:
                print(f"No record found with Roll Number {roll_number}.")

        elif choice == 4:
            student_list.show_records()

        elif choice == 5:
            print("Exiting Program.")
            break

        else:
            print("Invalid choice, please try again.")

# Call main function to run the program
if __name__ == "__main__":
    main()
