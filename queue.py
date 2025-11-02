
class Stack_view:
    def __init__(self):
        self.items = []
        
    def add(self):
        """Add items to the top of the stack"""
        added_items = input("Add the elements : ")
        self.items.append(added_items)
        print(f"{added_items} added successfully")

    def pop(self):
        """Remove the items from the top of the stack"""
        if not self.isEmpty():
            removed_item = self.items.pop()
            return removed_item
        else:
            print("List is empty")
            return None
    
    def peek(self):
        """Return the item at the top of the stack, without removing"""
        if not self.isEmpty():
           return self.items[-1]
        else:
            return "List is empty"  

    def isEmpty(self):
        """Check the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Returns the number of the items in the stack"""
        return len(self.items)
        
    
    def view_items(self):
        return self.items

my_stack = Stack_view()

my_stack.add()
my_stack.add()
my_stack.add()
print(my_stack.peek())
print(my_stack.view_items())
print(my_stack.pop())
print(my_stack.view_items())
print(my_stack.isEmpty())
print(f"Items count : {my_stack.size()}")