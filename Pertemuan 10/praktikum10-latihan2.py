#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 4 : Membuat BST yang Tidak Seimbang
#===================================================================================

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data #nilai pada node
        self.left = None #child kiri
        self.right = None #child kanan

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data) # node pertama jadi root
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data) # rekursif ke kiri
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data) # rekursif ke kanan
    return root # kembalikan root setelah insert

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ") # cetak node sekarang
        preorder(root.left) # lanjut ke kiri
        preorder(root.right) # lanjut ke kanan

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}") # tampilkan posisi & level
        tampil_struktur(root.left, level + 1, "L") # child kiri (level naik)
        tampil_struktur(root.right, level + 1, "R") # child kanan (level naik)

#===================================================================================
# Program utama
#===================================================================================

root = None   # inisialisasi root

# Data dimasukkan berurutan naik
data_list = [10, 20, 30] # bikin BST tidak seimbang (ke kanan)

for data in data_list:
    root = insert(root, data) # insert satu per satu ke BST

print("Preorder BST:")
preorder(root) # tampilkan hasil preorder

print("\n\nStruktur BST:")
tampil_struktur(root) # tampilkan struktur tree