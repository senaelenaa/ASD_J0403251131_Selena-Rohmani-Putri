# ===========================
# LATIHAN 3
# Double Linked List : Search
# ===========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Mencari data dalam doubly linked list
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


# Main Program
dll = DoublyLinkedList()

dll.insert_at_end(5)
dll.insert_at_end(10)
dll.insert_at_end(15)
dll.insert_at_end(20)

key = 15

if dll.search(key):
    print(f"Data {key} ditemukan dalam Double Linked List")
else:
    print(f"Data {key} tidak ditemukan dalam Double Linked List")