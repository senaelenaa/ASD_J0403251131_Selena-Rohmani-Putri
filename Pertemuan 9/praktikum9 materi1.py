#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 1 : Membuat Node
#===================================================================================

# Class node digunakan untuk dasar seperti tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #c kanan

# Membuat sebuah node root
root = Node("A")

# Menampilkan isi node
print("Data pada root : ", root.data)
print("Child kiri root : ", root.left)
print("Child kanan root : ", root.right)

#===================================================================================
# Penjelasan :
# Class Node digunakan sebagai representasi satu node yang memiliki tiga atribut utama, yaitu data untuk menyimpan nilai, serta left dan right yang masing-masing menunjuk ke child kiri dan kanan.
# Pada program ini dibuat satu node utama sebagai root dengan nilai "A", sementara child kiri dan kanan masih bernilai None karena belum diisi node lain.
# Selanjutnya, program menampilkan isi dari root beserta kondisi child-nya untuk menunjukkan bahwa node telah berhasil dibuat namun belum memiliki cabang.
#===================================================================================