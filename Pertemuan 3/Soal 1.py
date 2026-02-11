# ================================
# LATIHAN 1
# Single Linked List : Delete Node
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Menghapus node dengan nilai tertentu
    def delete_node(self, key):
        temp = self.head

        # Jika data ada di node pertama (head)
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Mencari node yang akan dihapus
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika data tidak ditemukan
        if temp is None:
            print("Data tidak ditemukan")
            return

        # Menghapus node
        prev.next = temp.next

    # Menampilkan isi linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Main Program
ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

print("Linked List sebelum dihapus:")
ll.display()

ll.delete_node(20)

print("Linked List setelah menghapus 20:")
ll.display()