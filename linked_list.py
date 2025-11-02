class NodeList:
    def __init__(self, data):
        self.data = data
        self.next = None

NodeList1 = NodeList(3)
NodeList2 = NodeList(15)
NodeList3 = NodeList(4)
NodeList4 = NodeList(2)

NodeList1.next = NodeList2
NodeList2.next = NodeList3
NodeList3.next = NodeList4

current_NodeList = NodeList1

while current_NodeList:
  print(current_NodeList.data, end=" ")
  current_NodeList = current_NodeList.next
print("None")