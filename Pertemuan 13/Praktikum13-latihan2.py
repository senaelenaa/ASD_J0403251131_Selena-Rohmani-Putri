#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#===================================================================================

#===================================================================================
# Latihan 2 : Implementasi Sederhana Algoritma Kruskal 
#===================================================================================

# Daftar edge dengan format (bobot, node1, node2)
# Bobot menunjukkan biaya/jarak antar node
edges = [
    (1, 'C', 'D'), # Edge C-D dengan bobot 1
    (2, 'A', 'C'), # Edge A-C dengan bobot 2
    (3, 'B', 'D'), # Edge B-D dengan bobot 3
    (4, 'A', 'B'), # Edge A-B dengan bobot 4
    (5, 'A', 'D') # Edge A-D dengan bobot 5
]

# Algoritma Kruskal mulai dengan mengurutkan edge dari bobot terkecil
edges.sort()

# List untuk menyimpan edge yang terpilih pada MST
mst = []

# Variabel untuk menyimpan total bobot MST
total_weight = 0

# Set untuk melacak node yang sudah terhubung
connected = set()

# Proses pemilihan edge secara global berdasarkan bobot terkecil
for weight, u, v in edges:
    
    # Edge dipilih jika setidaknya satu node belum ada dalam koneksi
    # Tujuannya untuk mencegah cycle sederhana
    if u not in connected or v not in connected:
        
        # Tambahkan edge ke MST
        mst.append((u, v, weight))
        
        # Tambahkan bobot edge ke total bobot
        total_weight += weight
        
        # Tandai node sebagai sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree (Kruskal):")

# Menampilkan setiap edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)

#===================================================================================
# Jawaban Analisis :
# 1. Edge yang dipilih pertama kali adalah ('C', 'D') dengan bobot 1.
# 2. Karena Kruskal adalah algoritma "greedy" yang mencari total bobot minimum dengan 
# selalu memprioritaskan edge paling ringan di seluruh graph terlebih dahulu.
# 3. Total bobot MST yang dihasilkan adalah 6 (1 + 2 + 3).
# 4. Edge seperti ('A', 'B') atau ('A', 'D') tidak dipilih karena node-node tersebut 
# sudah terhubung melalui jalur lain yang lebih murah, sehingga jika dipilih akan membentuk cycle.
#===================================================================================