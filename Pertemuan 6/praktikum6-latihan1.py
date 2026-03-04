#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan : 1 (Memahami Kode Program (Insertion Sort)
#===================================================================================

# Kode Program Insertion Sort :
def insertion_sort(data):
    
    # Perulangan dimulai dari indeks 1
    # karena indeks 0 dianggap sudah dalam keadaan terurut
    for i in range(1, len(data)):
        
        # key adalah nilai yang akan disisipkan
        # ke dalam bagian list yang sudah terurut
        key = data[i]
        
        # j adalah indeks elemen sebelum i
        j = i - 1
        
        # Selama:
        # 1. j masih dalam batas indeks (>= 0)
        # 2. data[j] lebih besar dari key
        # maka elemen digeser ke kanan
        while j >= 0 and data[j] > key:
            
            # Menggeser elemen ke kanan
            data[j + 1] = data[j]
            
            # Pindah ke elemen sebelumnya
            j -= 1
        
        # Setelah menemukan posisi yang tepat,
        # key dimasukkan ke posisi tersebut
        data[j + 1] = key
    
    # Mengembalikan data yang sudah terurut
    return data

# Program
data = [5, 2, 4, 6, 1, 3]
hasil = insertion_sort(data)

print("Data setelah diurutkan:", hasil)

#===================================================================================
# Soal dan Jawaban :
#  1. Mengapa perulangan dimulai dari indeks 1?
#   Karena elemen pertama (indeks 0) dianggap sudah terurut.
#   Insertion Sort bekerja dengan menganggap bagian kiri sudah
#   terurut, lalu menyisipkan elemen berikutnya ke posisi yang benar.

# 2. Apa fungsi variabel key?
#   Variabel key menyimpan nilai yang akan dibandingkan dan
#   ditempatkan pada posisi yang sesuai dalam bagian list
#   yang sudah terurut.

# 3. Mengapa digunakan while, bukan for?
#   Karena jumlah pergeseran tidak diketahui secara pasti.
#   Perulangan berhenti ketika menemukan posisi yang tepat,
#   sehingga lebih fleksibel menggunakan while.

# 4. Operasi apa yang terjadi di dalam while?
#   Terjadi proses pergeseran elemen yang lebih besar dari key
#   ke satu posisi di sebelah kanan sampai ditemukan posisi
#   yang sesuai untuk menyisipkan key.
#===================================================================================