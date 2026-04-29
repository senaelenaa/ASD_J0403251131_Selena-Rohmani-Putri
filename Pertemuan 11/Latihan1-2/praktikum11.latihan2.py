#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

# Representasi graph
graph = {
    'A': ['B', 'C'], # A ke B dan C
    'B': ['D', 'E'], # B ke D dan E
    'C': ['F'], # C ke F
    'D': [], # Tidak ada cabang
    'E': [],
    'F': []
}

# Fungsi DFS (rekursif)
def dfs(graph, node, visited):
    visited.add(node) # Tandai node sudah dikunjungi
    print(node, end=" ") # Tampilkan node

    # Telusuri semua tetangga
    for neighbor in graph[node]:
        if neighbor not in visited: # Jika belum dikunjungi
            dfs(graph, neighbor, visited) # Rekursi ke node tersebut

visited = set() # Set kosong untuk tracking

print("DFS dari A:")
dfs(graph, 'A', visited)


#===================================================================================
# Jawaban Analisis
#===================================================================================

# 1. DFS masuk ke node terdalam terlebih dahulu karena menggunakan pendekatan rekursif (atau stack),
# jadi dia terus "menyelam" sebelum kembali.

# 2. Jika urutan neighbor diubah, maka urutan hasil DFS juga berubah.
# karena DFS mengikuti urutan traversal dari list.

# 3. Perbandingan BFS vs DFS:
# BFS: menyebar per level (lebih cocok cari jarak terdekat)
# DFS: menyelam ke dalam dulu (lebih cocok eksplorasi jalur)