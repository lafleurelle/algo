class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if (index>self.size-1) | (index<0) | (self.head is None):
            return -1
        else:
            node = self.head
            for i in range(index):
                node = node.next
            return node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if self.size < index:
            return
        if index == 1:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            node = Node(val)
            last_node = self.head
            t = 1
            while t < index:
                last_node = last_node.next
                t += 1
            node.next = last_node.next
            last_node.next = node
            self.size += 1
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if (index > self.size - 1) | (index < 0) | (self.head is None):
            return
        else:
            node = self.head
            if index == 0:
                self.head = node.next
            else:
                for i in range(index-1):
                    node = node.next
                node.next = node.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
