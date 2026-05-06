#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path
#===================================================================================

#===================================================================================
# Latihan 3 : Implementasi Bellman-Ford 
#===================================================================================

# Weighted graph dengan bobot negatif 
# Graph ini memperbolehkan adanya bobot negatif (berbeda dengan Dijkstra)
graph = { 
    'A': {'B': 5, 'C': 4}, # A ke B = 5, A ke C = 4
    'B': {}, # B tidak punya tetangga
    'C': {'B': -2} # C ke B = -2 (bobot negatif)
} 
 
def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga (infinity)
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    # Tujuannya untuk memastikan semua kemungkinan jalur terpendek ditemukan
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge (hubungan antar node)
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jalur yang lebih pendek ke neighbor,
                # maka perbarui jaraknya (relaksasi)
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    # Mengembalikan hasil jarak terpendek dari start
    return distances 
 
 
# Menjalankan algoritma dari node 'A'
hasil = bellman_ford(graph, 'A') 
 
# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

#===================================================================================
# Jawaban Analisis : 
# 1. Bobot langsung dari A ke B adalah 5.
# 2. Total bobot jalur A → C → B adalah 4 + (-2) = 2.
# 3. Jalur yang lebih kecil adalah A → C → B.
# 4. Bellman-Ford bisa digunakan karena mampu menangani bobot negatif melalui proses relaksasi berulang.
# 5. Relaksasi edge adalah proses memperbarui jarak jika ditemukan jalur yang lebih pendek.
# 6. Perbedaannya:
# a) Dijkstra lebih cepat tapi tidak bisa bobot negatif
# 2) Bellman-Ford lebih lambat tapi bisa bobot negatif
#===================================================================================