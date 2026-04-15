#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 5 : Membuat Traversal Postorder
#===================================================================================

# Class node adalah unit dasar pada Tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #c kanan

# Membuat Traversal Postorder : Root ==> Left ==> Right
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


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
print("Hasil Traversal Postorder : ", end=" ")
postorder(root)

#===================================================================================
# Penjelasan :
# Program ini bertujuan untuk mengimplementasikan traversal postorder pada struktur binary tree.
# Class Node digunakan sebagai dasar pembentukan tree yang memiliki data serta child kiri dan kanan.
# Fungsi postorder bekerja dengan prinsip Left => Right => Root, yaitu menelusuri child kiri terlebih dahulu, kemudian child kanan, dan terakhir mencetak nilai node saat ini secara rekursif.
# Pada program ini dibuat sebuah tree dengan root "A", memiliki child "B" dan "C", serta node "B" memiliki dua child yaitu "D" dan "E".
# Ketika fungsi postorder dijalankan, program akan menampilkan urutan node sesuai metode postorder, yang menunjukkan bahwa pencetakan dilakukan setelah seluruh cabang ditelusuri.
#===================================================================================