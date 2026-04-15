#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 6 : Struktur Organisasi Perusahaan
#===================================================================================

# Class node digunakan untuk dasar seperti tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
   
# Fungsi untuk traversal preorder
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

# Membuat tree struktur organisasi perusahaan
root = Node("Direktur")

# Membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Membuat child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.right = Node("Staff3")

# Menjalankan traversal preorder 
print("Struktur Organisasi (Preorder):")
preorder(root)

#===================================================================================
# Penjelasan :
# Program ini bertujuan untuk merepresentasikan struktur organisasi perusahaan menggunakan konsep binary tree.
# Class Node digunakan untuk menyimpan data berupa jabatan serta memiliki child kiri dan kanan untuk menunjukkan hubungan hierarki.
# Pada program ini, "Direktur" dijadikan sebagai root, kemudian memiliki dua child yaitu "Manajer A" dan "Manajer B".
# Selanjutnya, "Manajer A" memiliki dua staff yaitu "Staff1" dan "Staff2", sedangkan "Manajer B" memiliki satu staff yaitu "Staff3".
# Untuk menampilkan struktur organisasi, digunakan fungsi traversal preorder dengan urutan Root => Left => Right, sehingga data ditampilkan mulai dari pimpinan tertinggi hingga ke bawah sesuai hierarki.
#===================================================================================