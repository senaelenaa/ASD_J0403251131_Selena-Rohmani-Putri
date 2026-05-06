#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path 
#===================================================================================

#===================================================================================
# Materi 1
#===================================================================================

import heapq  # Digunakan untuk membuat priority queue (antrian prioritas)

# Representasi graph berbobot (weighted graph)
# Setiap node memiliki tetangga dengan jarak tertentu
graph = {
    'A': {'B': 4, 'C': 2}, # A ke B = 4, A ke C = 2
    'B': {'D': 5}, # B ke D = 5
    'C': {'D': 1}, # C ke D = 1
}

def dijkstra(graph, start): 
    # Menyimpan jarak minimum dari start ke semua node
    # Awalnya semua di-set ke tak hingga (infinity)
    distances = {node: float('inf') for node in graph} 
 
    # Jarak node awal = 0 
    distances[start] = 0 
 
    # Priority queue untuk menyimpan (jarak, node)
    pq = [(0, start)] 
 
    # Selama masih ada node dalam antrian
    while pq: 
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items(): 
 
            # Hitung jarak baru
            distance = current_distance + weight 
 
            # Jika ditemukan jarak lebih kecil 
            if distance < distances[neighbor]: 
 
                # Update jarak
                distances[neighbor] = distance 
 
                # Masukkan ke priority queue untuk diproses
                heapq.heappush(pq, (distance, neighbor)) 
 
    # Mengembalikan hasil jarak terpendek
    return distances 
 
# Menjalankan fungsi dari node 'A'
hasil = dijkstra(graph, 'A') 

# Menampilkan hasil
print(hasil)