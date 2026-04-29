#===================================================================================
# Nama : Selena Rohmani Putri
# NIM : J0403251131
# Kelas : B2
#===================================================================================

#===================================================================================
# Implementasi DFS
#===================================================================================

# Struktur data untuk membuat antrian, menggunakan library collections bawaan python yaitu deque (double ended queue)

from collections import deque  # Mengimpor deque (meskipun di DFS ini tidak digunakan)
from platform import node  # Mengimpor fungsi node dari platform (tidak digunakan dalam kode)


#representasi graph
graph ={  # Membuat dictionary sebagai representasi graph
    'A': ['B', 'C'],  # Node A memiliki anak B dan C
    'B': ['D', 'E',],  # Node B memiliki anak D dan E
    'C': ['F', 'G'],  # Node C memiliki anak F dan G
    'D': [],  # Node D tidak memiliki tetangga (leaf)
    'E': [],  # Node E tidak memiliki tetangga
    'F': [],  # Node F tidak memiliki tetangga
    'G': []  # Node G tidak memiliki tetangga

}

def dfs(graph, node, visited=None):  # Fungsi DFS (Depth-First Search)
#fungsi untuk melakukan penelusuran graph menggunakan DFS 
#graph : dictionary yang menyimpan graph
#node : menyimpan node yang sedang dikunjungi
#visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai sudah dikunjungi
    visited.add(node)  # Menambahkan node ke dalam set visited

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")  # Menampilkan node tanpa pindah baris

        #periksa semua tetangga dari node saat ini 
    for neighbor in graph [node]:  # Iterasi semua tetangga dari node saat ini
        #jika tetangga belum dikunjungi
        if neighbor not in visited:  # Cek apakah tetangga belum dikunjungi
            #panggil fungsi DFS secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)  # Rekursi ke node berikutnya
            #tandai sebagai sudah dikunjungi
            #visited.add(neighbor)  # Tidak diperlukan karena sudah dilakukan di awal fungsi

#menjalankan DFS dari graph A
#set untuk menyimpan node yang sudah dikunjungi
visited = set()  # Membuat set kosong untuk menyimpan node yang dikunjungi
dfs(graph, 'A', visited)  # Memulai DFS dari node A

#===================================================================================
# DFS adalah metode penelusuran graph yang berjalan sedalam mungkin terlebih dahulu menggunakan rekursi.
# Setiap node dikunjungi, lalu fungsi memanggil dirinya sendiri ke tetangga yang belum dikunjungi hingga mencapai ujung,
# kemudian kembali (backtracking).
#===================================================================================