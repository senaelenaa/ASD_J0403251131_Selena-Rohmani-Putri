#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
#===================================================================================

# Class Node
class Node:
    def __init__(self, data):
        self.data = data # nilai node
        self.left = None # child kiri
        self.right = None # child kanan

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ") # tampilkan node
        preorder(root.left) # ke kiri
        preorder(root.right) # ke kanan

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}") # tampilkan posisi node
        tampil_struktur(root.left, level + 1, "L") # child kiri
        tampil_struktur(root.right, level + 1, "R") # child kanan

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right # ambil child kanan sebagai calon root baru
    T2 = y.left # simpan subtree kiri dari y

    # Proses rotasi
    y.left = x # x pindah jadi child kiri dari y
    x.right = T2 # subtree T2 jadi child kanan x

    # y menjadi root baru
    return y # kembalikan root baru

#===================================================================================
# Program utama
#===================================================================================

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root) # cek isi tree sebelum rotasi

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root) # lihat bentuk tree awal

# Melakukan rotasi kiri pada root
root = rotate_left(root) # rotasi untuk menyeimbangkan

print("\nPreorder sesudah rotasi kiri:")
preorder(root) # cek hasil setelah rotasi

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root) # lihat perubahan struktur