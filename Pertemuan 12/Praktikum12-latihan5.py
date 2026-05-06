#===================================================================================
# Nama    : Selena Rohmani Putri
# NIM     : J0403251131
# Kelas   : B
# Praktikum 12 Graph II: Shortest Path
#===================================================================================

#===================================================================================
# Latihan 5 : Studi Kasus Jalur Terpendek Lokasi Kampus 
#===================================================================================

import heapq

def dijkstra(graph, start):
    # 1. Inisialisasi jarak: set semua ke tak hingga (inf), kecuali start = 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # 2. Priority queue untuk menyimpan (jarak_terpendek, node)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Jika jarak di queue lebih besar dari yang tercatat, abaikan
        if current_distance > distances[current_node]:
            continue
            
        # 3. Proses relaksasi: periksa tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih murah ke tetangga tersebut
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Representasi Weighted Graph menggunakan Dictionary
# Sesuai data: Bogor-Jakarta(5), Bogor-Depok(2), Depok-Jakarta(2), Jakarta-Bandung(7), Depok-Bandung(6)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

# Menentukan node awal
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# Output hasil jarak terpendek
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

#===================================================================================
# Jawaban Analisis :
# 1. Jawaban: Node awal yang digunakan adalah 'Bogor'.
# 2. Jawaban: Node 'Bogor' itu sendiri (jarak 0), atau 'Depok' (jarak 2) jika mencari node tujuan terdekat.
# 3. Jawaban: Node 'Bandung' dengan total bobot 8 (melalui Bogor -> Depok -> Bandung).
# 4. Jawaban: Algoritma ini bekerja secara greedy. Dimulai dari Bogor, ia melihat tetangga terdekatnya (Depok).
# Meskipun ada jalur langsung Bogor -> Jakarta (5), Dijkstra menemukan bahwa melalui Depok (2) kemudian ke Jakarta (+2) totalnya lebih kecil (4).
# Proses ini terus dilakukan hingga semua jarak minimum ke setiap kota ditemukan.
#===================================================================================