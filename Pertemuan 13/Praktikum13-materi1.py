#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#===================================================================================

#===================================================================================
# Materi 1 : Implementasi Kruskal
#===================================================================================

# Daftar edge dalam bentuk:
# (bobot, node1, node2)
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort() 
 
# Menyimpan edge yang terpilih ke MST
mst = [] 

# Menyimpan total bobot MST
total_weight = 0 
 
# Set sederhana untuk node yang sudah terhubung
connected = set() 
 
# Periksa setiap edge yang sudah diurutkan
for weight, u, v in edges: 
 
    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 
 
        # Tambahkan edge ke MST
        mst.append((u, v, weight)) 
        
        # Tambahkan bobot ke total
        total_weight += weight 
 
        # Tandai node sebagai sudah terhubung
        connected.add(u) 
        connected.add(v) 
 
# Menampilkan hasil MST
print("Minimum Spanning Tree:") 
 
# Menampilkan setiap edge dalam MST
for edge in mst: 
    print(edge) 
 
# Menampilkan total bobot MST
print("Total bobot =", total_weight)