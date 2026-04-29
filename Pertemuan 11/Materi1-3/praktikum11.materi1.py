#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Implementasi Dasar Graph
#===================================================================================

graph = {  # Membuat dictionary untuk merepresentasikan graph
    'A': ['B', 'C'],  # Node A terhubung ke B dan C
    'B': ['A', 'D'],  # Node B terhubung ke A dan D
    'C': ['A', 'D'],  # Node C terhubung ke A dan D
    'D': ['B', 'C']   # Node D terhubung ke B dan C
}

for node in graph:  # Melakukan iterasi pada setiap node dalam graph
    print(node, "->", graph[node])  # Menampilkan node beserta daftar tetangganya