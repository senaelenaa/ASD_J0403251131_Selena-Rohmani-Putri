#============================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#============================

#==========================================
#Implementasi Dasar : Linked List + Inster Awal
#==========================================

#Mmbuat class Node (Merupakan unit dasae Linked List)
class Node:
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke note berikutnya (awal=none)

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None

    def enqueue(self,data):
        #Menambah data di belakang (rear)
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong, rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #Rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self):
        #Menghapus data dari depan


        #1) Lihat data dari paling depan
        data_terhapus = self.front.data

        #2) Geser front ke node berikutnya
        self.front = self.front.next

        #3) Jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None

            return data_terhapus

    def tampilkan(self):

        current = self.front
        print("Front->", end="")
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print("->", end="")
            current = current.next
        print("->Rear")

#Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()