#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path
#===================================================================================

#===================================================================================
# Latihan 4 : Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma : Dijkstra 
#===================================================================================

import heapq  # Digunakan untuk membuat priority queue (antrian prioritas)

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
# Setiap node merepresentasikan lokasi, dan nilainya adalah jarak ke lokasi lain
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, # Dari Gerbang ke Perpustakaan (6 menit), ke Kantin (2 menit)
    'Perpustakaan': {'Lab': 3}, # Dari Perpustakaan ke Lab (3 menit)
    'Kantin': {'Lab': 4, 'Aula': 7}, # Dari Kantin ke Lab (4 menit), ke Aula (7 menit)
    'Lab': {'Aula': 1}, # Dari Lab ke Aula (1 menit)
    'Aula': {} # Aula tidak punya tujuan lain
} 

def dijkstra(graph, start): 
    # Inisialisasi semua jarak ke tak hingga
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari titik awal ke dirinya sendiri adalah 0
    distances[start] = 0 
    
    # Priority queue untuk menyimpan (jarak, node)
    priority_queue = [(0, start)] 

    # Selama masih ada node dalam antrian
    while priority_queue: 
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue) 

        # Jika jarak saat ini lebih besar dari yang sudah tercatat, lewati
        if current_distance > distances[current_node]: 
            continue 

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru ke neighbor
            distance = current_distance + weight 

            # Jika jarak baru lebih kecil, update
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor)) 

    # Mengembalikan semua jarak terpendek
    return distances 

# Menjalankan algoritma dari node 'Gerbang'
hasil = dijkstra(graph, 'Gerbang') 

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit")


#===================================================================================
# Jawaban Analisis : 
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin (2 menit).
# 2. Waktu tercepat dari Gerbang ke Aula adalah 7 menit (Gerbang → Kantin → Lab → Aula).
# 3. Tidak, jalur langsung tidak selalu paling kecil karena bisa saja jalur tidak langsung memiliki total waktu lebih cepat.
# 4. Dijkstra cocok karena semua bobot waktu bernilai positif dan ingin mencari jalur tercepat.
#===================================================================================