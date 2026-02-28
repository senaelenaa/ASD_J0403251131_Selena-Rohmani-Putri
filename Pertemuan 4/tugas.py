#===================================================================================
#Nama : Selena Rohmani Putri
#NIM : J0403251131
#Kelas : B2
#===================================================================================

#===================================================================================
#Studi Kasus : Sistem Antrian Bengkel Motor
#Implementasi Queue =>
# Enqueue (tambah motor ke antrian) : Memindahkan pointer rear
# Dequeue (motor dilayani/selesai servis) : memindahkan pointer front
# Front -> Motor1 -> Motor2 -> Motor3 -> Rear
#===================================================================================


# 1. Mendefinisikan node (unit dasar linked list)
class Node:
    def __init__(self, no_polisi, nama_pemilik, jenis_motor):
        self.no_polisi = no_polisi          # Menyimpan nomor polisi motor
        self.nama_pemilik = nama_pemilik    # Menyimpan nama pemilik
        self.jenis_motor = jenis_motor      # Menyimpan jenis motor
        self.next = None                    # Pointer ke node berikutnya


# 2. Mendefinisikan Queue Bengkel
class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # Queue kosong jika front bernilai None
        return self.front is None

    # Menambahkan motor ke antrian (enqueue)
    def enqueue(self, no_polisi, nama_pemilik, jenis_motor):
        nodeBaru = Node(no_polisi, nama_pemilik, jenis_motor)

        # Jika antrian kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Jika tidak kosong, tambahkan di belakang (rear)
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # Melayani motor paling depan (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada motor yang bisa dilayani.")
            return None

        motor_dilayani = self.front
        self.front = self.front.next

        # Jika antrian menjadi kosong setelah dequeue
        if self.front is None:
            self.rear = None

        return motor_dilayani

    # Menampilkan seluruh antrian
    def tampilkan(self):
        if self.is_empty():
            print("Antrian bengkel masih kosong.")
            return

        print("=== Daftar Antrian Bengkel (Front -> Rear) ===")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. No Polisi: {current.no_polisi}, "
                  f"Nama: {current.nama_pemilik}, "
                  f"Jenis Motor: {current.jenis_motor}")
            current = current.next
            no += 1


# Program Utama

def main():
    q = QueueBengkel()

    while True:
        print("\n==== Sistem Antrian Bengkel Motor ====")
        print("1. Tambah Motor ke Antrian")
        print("2. Layani Motor")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            no_polisi = input("Masukkan Nomor Polisi: ").strip()
            nama_pemilik = input("Masukkan Nama Pemilik: ").strip()
            jenis_motor = input("Masukkan Jenis Motor: ").strip()

            q.enqueue(no_polisi, nama_pemilik, jenis_motor)
            print("Motor berhasil ditambahkan ke antrian.")

        elif pilihan == "2":
            motor_dilayani = q.dequeue()
            if motor_dilayani is not None:
                print(f"Motor dengan No Polisi {motor_dilayani.no_polisi} "
                      f"atas nama {motor_dilayani.nama_pemilik} "
                      f"sedang dilayani.")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()