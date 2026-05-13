#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#===================================================================================

#===================================================================================
# Materi 2 : Implementasi Prim 
#===================================================================================

import heapq  # Digunakan untuk priority queue (antrian prioritas)
 
# Representasi graph berbobot
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, # A terhubung ke B, C, dan D
    'B': {'A': 4, 'D': 3}, # B terhubung ke A dan D
    'C': {'A': 2, 'D': 1}, # C terhubung ke A dan D
    'D': {'A': 5, 'B': 3, 'C': 1} # D terhubung ke A, B, dan C
} 
 
def prim(graph, start): 
 
    # Menyimpan node yang sudah dikunjungi
    visited = set([start]) 
 
    # Priority queue untuk menyimpan edge
    edges = [] 
 
    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
 
    # Menyimpan hasil Minimum Spanning Tree
    mst = [] 
    
    # Menyimpan total bobot MST
    total_weight = 0 
 
    # Selama masih ada edge yang bisa diproses
    while edges: 
 
        # Ambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges) 
 
        # Jika node tujuan belum dikunjungi
        if v not in visited: 
 
            # Tandai node sebagai sudah dikunjungi
            visited.add(v) 
 
            # Tambahkan edge ke MST
            mst.append((u, v, weight)) 
            
            # Tambahkan bobot ke total
            total_weight += weight 
 
            # Periksa semua tetangga dari node v
            for neighbor, w in graph[v].items(): 
 
                # Jika tetangga belum dikunjungi
                if neighbor not in visited: 
                    
                    # Tambahkan edge ke priority queue
                    heapq.heappush(edges, (w, v, neighbor)) 
 
    # Mengembalikan MST dan total bobot
    return mst, total_weight 
 
 
# Menjalankan algoritma Prim dari node 'A'
mst, total = prim(graph, 'A') 
 
# Menampilkan hasil MST
print("Minimum Spanning Tree:") 
 
# Menampilkan setiap edge pada MST
for edge in mst: 
    print(edge) 
 
# Menampilkan total bobot MST
print("Total bobot =", total)