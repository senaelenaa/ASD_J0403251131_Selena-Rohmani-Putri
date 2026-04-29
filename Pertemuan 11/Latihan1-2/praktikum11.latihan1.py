#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

# Import deque untuk queue (antrian)
from collections import deque  

# Representasi graph dalam bentuk dictionary (adjacency list)
graph = {
    'Rumah': ['Sekolah', 'Toko'], # Rumah terhubung ke Sekolah dan Toko
    'Sekolah': ['Perpustakaan'], # Sekolah ke Perpustakaan
    'Toko': ['Pasar'], # Toko ke Pasar
    'Perpustakaan': [], # Tidak ada cabang lagi
    'Pasar': [] # Tidak ada cabang lagi
}

# Fungsi BFS
def bfs(graph, start):
    visited = set() # Menyimpan node yang sudah dikunjungi
    queue = deque([start]) # Queue dimulai dari node awal

    visited.add(start) # Tandai node awal sudah dikunjungi

    while queue: # Selama masih ada antrian
        node = queue.popleft() # Ambil node paling depan
        print(node, end=" ") # Tampilkan node

        # Cek semua tetangga dari node
        for neighbor in graph[node]:
            if neighbor not in visited: # Jika belum dikunjungi
                visited.add(neighbor) # Tandai sudah dikunjungi
                queue.append(neighbor) # Masukkan ke antrian

print("BFS dari Rumah:")
bfs(graph, 'Rumah')



#===================================================================================
# Jawaban Analisis
#===================================================================================
# 1. Node pertama yang dikunjungi adalah "Rumah"
# karena BFS selalu mulai dari node awal yang diberikan.

# 2. BFS cocok untuk mencari jalur terdekat karena BFS mengeksplorasi node per level (lapisan).
# Jadi node yang paling dekat akan ditemukan lebih dulu.

# 3. Jika struktur graph diubah (misalnya urutan tetangga),
# maka urutan hasil BFS juga bisa berubah,
# karena BFS mengikuti urutan neighbor dalam list.