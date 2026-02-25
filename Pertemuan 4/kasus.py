#===================================================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#===================================================================================

#===================================================================================
#Studi Kasus : Sistem Antrian Layanan Akademik
#Implementasi Queue =>
# Enqueue (tambah data ke antrian) : Memindahkan pointer rear
# Dequeue (hapus data dari antrian) : memindahkan pointer front
# Stack ==> Front -> B -> A -> None
# Front-> A > B >  C  ->Rear

#===================================================================================

#1. Mendefinisikan node (unit dasar linked list)
class node:
    def __init__(self, nim, nama):
        self.nim = nim    #Menyimpan NIM mahasiswa
        self.nama = nama  #menyimpan nama mahasiswa
        self.next = None   #pointer ke node berukutnya

#2. Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        #ketika queue kosong maka front = rear = none
        return self.front is None
    
    def enqueue(self, nim, nama):
        nodeBaru = node(nim, nama) #membuat node baru dengan data nim dan nama
        #Jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty(): #jika queue kosong
            self.front = nodeBaru #front dan rear menunjuk ke node baru
            self.rear = nodeBaru
            return
        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan rear
        nodeBaru = node(nim, nama) #membuat node baru
        self.rear.next = nodeBaru #rear menunjuk ke node baru
        self.rear = nodeBaru #rear menjadi node baru

    #Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty(): #jika queue kosong
            print("Antrian kosong, tidak ada yang bisa dilayani.")
            return None
        
        #lihat data bagian front, simpan variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #jika front menjadi none(data anrtian terakhir dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):

        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}")
            current = current.next
            no += 1 

#Program Utama

def main():

    #instantiasi queue akademik 
    q = queueAkademik()

    while True :
        print("==== Sistem Antrian Akademik ====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian.")

        elif pilihan == "2":
            node_dilayani = q.dequeue()
            print(f"Mahasiswa dengan NIM {node_dilayani.nim} dan Nama {node_dilayani.nama} dilayani.")
            
        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()