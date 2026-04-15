#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 4 : Membuat Traversal Inorder
#===================================================================================

# Class node adalah unit dasar pada Tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #c kanan

# Membuat fungsi inorder : left ==> root ==> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

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
print("Hasil Traversal Inorder : ", end=" ")
inorder(root)

#===================================================================================
# Penjelasan :
# Program ini bertujuan untuk mengimplementasikan traversal inorder pada struktur binary tree.
# Class Node digunakan sebagai dasar pembentukan tree yang memiliki data serta child kiri dan kanan.
# Fungsi inorder bekerja dengan prinsip Left => Root => Right, yaitu menelusuri child kiri terlebih dahulu, kemudian mencetak nilai node saat ini, lalu dilanjutkan ke child kanan secara rekursif.
# Pada program ini dibuat sebuah tree dengan root "A", memiliki child "B" dan "C", serta node "B" memiliki dua child yaitu "D" dan "E".
# Ketika fungsi inorder dijalankan, program akan menampilkan urutan node sesuai metode inorder, yang menunjukkan proses penelusuran dari sisi paling kiri menuju kanan secara bertahap.
#===================================================================================