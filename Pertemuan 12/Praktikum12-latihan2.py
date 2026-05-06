#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path
#===================================================================================

#===================================================================================
# Latihan 2 : Implementasi Dijkstra
#===================================================================================

import heapq  # Digunakan untuk priority queue (antrian prioritas)

# Weighted graph dengan bobot positif 
# Setiap node memiliki tetangga dengan jarak (bobot) tertentu
graph = { 
    'A': {'B': 4, 'C': 2}, # A ke B = 4, A ke C = 2
    'B': {'D': 5}, # B ke D = 5
    'C': {'D': 1}, # C ke D = 1
    'D': {} # D tidak punya tetangga
} 

def dijkstra(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    """ 

    # Semua jarak awal dibuat tak hingga (infinity)
    distances = {node: float('inf') for node in graph} 

    # Jarak dari start ke start adalah 0 
    distances[start] = 0 

    # Priority queue menyimpan pasangan (jarak, node)
    # Dimulai dari node awal
    priority_queue = [(0, start)]

    # Selama masih ada node yang perlu diproses
    while priority_queue: 
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Jika jarak saat ini lebih besar dari yang sudah tersimpan,
        # berarti data ini sudah tidak relevan (skip)
        if current_distance > distances[current_node]: 
            continue 
 
        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            # Hitung jarak baru ke neighbor
            distance = current_distance + weight 
 
            # Jika ditemukan jarak yang lebih kecil, perbarui
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                # Masukkan ke priority queue untuk diproses selanjutnya
                heapq.heappush(priority_queue, (distance, neighbor)) 
 
    # Kembalikan semua jarak terpendek dari start
    return distances 
 
 
# Menjalankan fungsi Dijkstra dari node 'A'
hasil = dijkstra(graph, 'A') 
 
# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

#===================================================================================
# Jawaban Analisis : 
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3 (melalui C).
# 4. Karena jalur A → C → D memiliki bobot 2 + 1 = 3, lebih kecil dibanding A → B → D yaitu 9.
# 5. priority_queue berfungsi untuk memilih node dengan jarak terkecil terlebih dahulu agar proses lebih efisien.
# 6. Dijkstra tidak cocok untuk bobot negatif karena bisa menghasilkan perhitungan jarak yang salah (tidak stabil).
#===================================================================================