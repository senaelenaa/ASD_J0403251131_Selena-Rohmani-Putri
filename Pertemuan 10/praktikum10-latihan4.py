#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
#===================================================================================

class Node:
    def __init__(self, data):
        self.data = data # nilai node
        self.left = None # child kiri
        self.right = None # child kanan

def preorder(root):
    if root is not None:
        print(root.data, end=" ") # tampilkan node
        preorder(root.left) # ke kiri
        preorder(root.right) # ke kanan

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}") # tampilkan posisi node
        tampil_struktur(root.left, level + 1, "L") # child kiri
        tampil_struktur(root.right, level + 1, "R") # child kanan

# Fungsi rotasi kanan
def rotate_right(y):
    # y adalah root lama
    x = y.left # ambil child kiri sebagai calon root baru
    T2 = x.right # simpan subtree kanan dari x

    # Proses rotasi
    x.right = y # y pindah jadi child kanan dari x
    y.left = T2 # subtree T2 jadi child kiri y

    # x menjadi root baru
    return x # kembalikan root baru

#===================================================================================
# Program utama
#===================================================================================

# Membuat tree yang tidak seimbang (condong ke kiri):
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root) # cek isi sebelum rotasi

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root) # lihat bentuk awal

# Melakukan rotasi kanan pada root
root = rotate_right(root) # rotasi untuk menyeimbangkan

print("\nPreorder sesudah rotasi kanan:")
preorder(root) # cek hasil setelah rotasi

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root) # lihat perubahan struktur