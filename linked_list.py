class linked_list:
    def __init__(self, data):
        self.data = data
        self.next = None

linked_list1 = linked_list(3)
linked_list2 = linked_list(15)
linked_list3 = linked_list(4)
linked_list4 = linked_list(2)

linked_list1.next = linked_list2
linked_list2.next = linked_list3
linked_list3.next = linked_list4

current_linked_list = linked_list1

while current_linked_list:
  print(current_linked_list.data, end=" ")
  current_linked_list = current_linked_list.next
print("Null")