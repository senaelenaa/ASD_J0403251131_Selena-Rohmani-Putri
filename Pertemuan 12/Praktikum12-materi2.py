#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
# Praktikum 12 - Graph II: Shortest Path 
#===================================================================================

#===================================================================================
# Materi 2
#===================================================================================

def bellman_ford(graph, start): 
 
    # Inisialisasi jarak semua node ke tak hingga (infinity)
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0 
 
    # Relaksasi berulang sebanyak (jumlah node - 1)
    # Tujuannya untuk memastikan semua jalur terpendek ditemukan
    for _ in range(len(graph) - 1): 
 
        # Iterasi setiap node dalam graph
        for node in graph: 
 
            # Iterasi setiap tetangga dari node tersebut
            for neighbor, weight in graph[node].items(): 
 
                # Jika ditemukan jarak yang lebih kecil,
                # maka update jarak ke neighbor
                if distances[node] + weight < distances[neighbor]: 
 
                    distances[neighbor] = distances[node] + weight 
 
    # Mengembalikan hasil jarak terpendek
    return distances