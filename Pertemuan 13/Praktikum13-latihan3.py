#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#===================================================================================

#===================================================================================
# Latihan 3 : Implementasi Algoritma Prim
#===================================================================================

import heapq  # Digunakan untuk priority queue (antrian prioritas)

# Representasi weighted graph menggunakan dictionary
# Setiap node memiliki tetangga beserta bobotnya
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5}, # A terhubung ke B, C, dan D
    'B': {'A': 4, 'D': 3}, # B terhubung ke A dan D
    'C': {'A': 2, 'D': 1}, # C terhubung ke A dan D
    'D': {'A': 5, 'B': 3, 'C': 1} # D terhubung ke A, B, dan C
}

def prim(graph, start):
    
    # Mencatat node yang sudah dikunjungi
    visited = set([start]) 
    
    # Priority queue untuk menyimpan edge
    edges = []
    
    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    
    # Menyimpan edge yang dipilih untuk MST
    mst = []
    
    # Menyimpan total bobot MST
    total_weight = 0
    
    # Selama masih ada edge dalam antrean
    while edges:
        
        # Mengambil edge dengan bobot terkecil
        # dari node yang sudah dikunjungi
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan belum dikunjungi
        if v not in visited:
            
            # Tandai node sebagai sudah dikunjungi
            visited.add(v)
            
            # Tambahkan edge ke MST
            mst.append((u, v, weight))
            
            # Tambahkan bobot edge ke total
            total_weight += weight
            
            # Menambahkan edge dari node baru
            # yang dikunjungi ke dalam antrean
            for neighbor, w in graph[v].items():
                
                # Hanya tambahkan node yang belum dikunjungi
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    
    # Mengembalikan MST dan total bobot
    return mst, total_weight

# Menjalankan fungsi Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree (Prim):")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)

#===================================================================================
# Jawaban Analisis :
# 1. Node awal yang digunakan adalah 'A'.
# 2. Edge yang dipilih pertama kali adalah ('A', 'C') dengan bobot 2.
# 3. Prim menentukan edge berikutnya dengan membandingkan semua edge yang terhubung 
# dari node-node yang sudah dikunjungi ('A' dan 'C') ke node yang belum dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6.
# 5. Perbedaannya: Kruskal memilih edge terkecil secara global (fokus pada edge), 
# sedangkan Prim menumbuhkan tree dari satu node ke tetangga terdekatnya (fokus pada node).
#===================================================================================