#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 2 : Membuat Binary Search Sederhana
#===================================================================================

# Class node digunakan untuk dasar seperti tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #c kanan

# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.right.right = Node("E")

# Menampilkan isi node
print("Data pada root : ", root.data)
print("Child kiri root : ", root.left.data)
print("Child kanan root : ", root.right.data)
print("Child kiri dari B : ", root.left.left.data)
print("Child kiri dari C : ", root.right.right.data)

#===================================================================================
# Penjelasan :
# Setiap node memiliki atribut data, serta pointer ke child kiri (left) dan kanan (right).
# Pada program ini, dibuat sebuah root dengan nilai "A", kemudian ditambahkan child level pertama yaitu "B" sebagai anak kiri dan "C" sebagai anak kanan.
# Selanjutnya, ditambahkan child level kedua yaitu "D" sebagai anak kiri dari "B" dan "E" sebagai anak kanan dari "C".
# Setelah struktur tree terbentuk, program menampilkan isi dari setiap node.
#===================================================================================