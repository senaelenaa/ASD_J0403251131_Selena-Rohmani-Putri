#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Latihan 1 : BST
#===================================================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai/data pada node
        self.left = None # Pointer ke anak kiri (awal kosong)
        self.right = None # Pointer ke anak kanan (awal kosong)

def insert(root, data):
    if root is None:
        return Node(data) # Jika root kosong, buat node baru sebagai root
    
    if data < root.data:
        # Jika data lebih kecil, masuk ke subtree kiri
        root.left = insert(root.left, data)
    elif data > root.data:
        # Jika data lebih besar, masuk ke subtree kanan
        root.right = insert(root.right, data)
    
    return root # Mengembalikan root setelah proses insert

# Mengisi data BST
root = None # Inisialisasi root awal (kosong)
data_list = [50, 30, 70, 20, 40, 60, 80] # Data yang akan dimasukkan ke BST

for data in data_list:
    root = insert(root, data) # Memasukkan tiap elemen ke dalam BST

print("BST berhasil dibuat") # Menandakan BST sudah terbentuk


#===================================================================================
# Latihan 2 : Traversal Inorder
#===================================================================================

def inorder(root):
    if root is not None:
        inorder(root.left) # Kunjungi subtree kiri terlebih dahulu
        print(root.data, end=" ") # Cetak data node saat ini
        inorder(root.right) # Kunjungi subtree kanan

print("Hasil inorder: ")
inorder(root) # Menjalankan traversal inorder pada BST
print() # Untuk baris baru

#===================================================================================
# Latihan 3 : Search di BST
#===================================================================================

def search(root, key):
    if root is None:
        return False # Jika node kosong, data tidak ditemukan
    
    if root.data == key:
        return True # Jika data ditemukan, kembalikan True
    elif key < root.data:
        # Jika key lebih kecil, cari di subtree kiri
        return search(root.left, key)
    else:
        # Jika key lebih besar, cari di subtree kanan
        return search(root.right, key)

# Uji pencarian
key = 100 # Data yang ingin dicari

if search(root, key):
    print("Data Ditemukan") # Output jika data ada di BST
else:
    print("Data Tidak Ditemukan") # Output jika data tidak ada