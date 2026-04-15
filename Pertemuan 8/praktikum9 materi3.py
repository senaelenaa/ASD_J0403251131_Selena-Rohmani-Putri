#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 3 : Membuat Traversal Preorder
#===================================================================================

# Class node adalah unit dasar pada Tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #c kanan

# Fungsi Preorder : Root ==> Left ==> Right ==>
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

# Membuat tree
# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal Preorder
print("Hasil Traversal Preorder : ")
preorder(root)

#===================================================================================
# Penjelasan :
# Program ini bertujuan untuk mengimplementasikan traversal preorder pada struktur binary tree.
# Class Node digunakan sebagai dasar pembentukan tree yang memiliki data serta child kiri dan kanan.
# Fungsi preorder bekerja dengan prinsip Root => Left => Right, yaitu mencetak nilai node saat ini terlebih dahulu, kemudian menelusuri child kiri dan dilanjutkan ke child kanan secara rekursif.
# Pada program ini dibuat sebuah tree dengan root "A", memiliki child "B" dan "C", serta "B" memiliki dua child yaitu "D" dan "E".
# Ketika fungsi preorder dijalankan, program akan menampilkan urutan node sesuai metode preorder, yang menunjukkan proses penelusuran tree dari akar hingga ke seluruh cabangnya.
#===================================================================================