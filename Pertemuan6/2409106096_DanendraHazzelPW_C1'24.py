# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])


# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku1" : "Twillight"
# }
# print(daftar_buku["Buku1"]) # bakal print yang paling bawah karena dianggap memperbarui


# Biodata = {
#     "Nama" : "Danendra Hazzel Putra Wahana",
#     "NIM" : "2409106096",
#     "KRS" : ["PROGRAM WEB", "STRUKTUR DATA", "BASIS DATA"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {
#         "Instagram" : "@_DHZPW",
#         "Discord" :  "Az1945",
#         "Email" : "email123@gmail.com"
#     }
# }

# print(Biodata["Social Media"]["Email"])
# print(Biodata["KRS"][0])
# print(Biodata["Nama"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = "FPS")
# print(games["Pokemon"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = {"nama" : "Hazzel"})
# print(games["Pokemon"])
# print(games ["Valorant"]["nama"]) # key bisa gunakan pake tanda petik 1 saja karena terkadang error

# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = {"nama" : {123 : "Informatika"}})
# print(games["Sekiro"])
# print(games ["Valorant"]["nama"][123])

# Games = {
#     "Games1" : "PUBG Mobile",
#     "Games2" : "Mobie Legends",
#     "Games3" : "Clash Royale"
# }

# print(Games.get('Games3'))

# Games = {
#     "Games1" : "PUBG Mobile",
#     "Games2" : "Mobie Legends",
#     "Games3" : {
#         "nama" : "clash royale",
#         "genre" : "strategi"
#     }
# }
# print((Games.get("Games3")).get('genre'))
# print(Games.get('Games3')["genre"]) # keduanya benar tergantung efisiensi

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# # tanpa gunakan item
# for i in Nilai:
#     print(i)
# print(" ")

# # gunakan item
# for i, j in Nilai.items():
#     print(f"Nilai {i} Anda adalah {j}")

# Film = {
#     "Avengers Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# # Sebelum update
# # print(Film)

# # Sesudah Update
# Film["Zombieland"] = "comedy"
# Film.update({"Hours" : "Thrillers", "Elemental" : " Drama", "Moana" : "Musical"}) # Bisa menambahkan banyak tinggal pake koma
# print(Film)

# # del Film['Avengers Endgame'] # Menghapus permanen film
# # # print(Film)

# # # simpan = Film.pop('Hours')  # Menyimpan variabel akan hilang dan bisa di print lagi tapi yang muncul value/isinya
# # # # Film.clear() # Menghapus semua
# # # print(Film)
# # # Film["Hours"] = simpan # Menambahkan variabel dan value ke paling akhir/ disimpan sementara dan dimunculkan lagi
# # # print(Film)
# # # # print(simpan) # Hanya memunculkan valuenya saja tanpa variabel
# # print("Jumlah Film = ", len(Film)) # Mengetahui berapa data yang kita buat

# movies = Film.copy()
# print(movies)
# print("Jumlah Film = ", len(movies))

# Key = "Apel", "Mangga", "Jeruk"
# Value = 2
# buah = dict.fromkeys(Key, Value)
# print(buah) # cocok untuk yang valuenya hanya satu/tunggal

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# print(Nilai)
# print(" ")
# print(Nilai["Kimia"])
# print("Nilai : ", Nilai.setdefault("Kimia", 78))
# print(" ")

# Musik = {
#     "The Chainsmoker" : ["All We Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of me", "Memories"]
# }

# for i,j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j :
#         print(song)
# print(" ")

# mahasiswa = {
# 96 : {"Nama" : " Hazzel", "Umur" : 19},
# 91 : {"Nama" : "Wawan", "Umur" : 18}
# }
# for key,value in mahasiswa.items():
#     print("ID mahaiswa:", key)
#     for key_a, value_a in value.items():
#         print(key_a, " : ", value_a)
# print(" ")

# mahasiswa = {
# 24 : {"Nama" : "Hazzel", "Umur" : 19, "Jurusan" : "Informatika"}
# }
# for key,value in mahasiswa.items():
#     print("Mahasiswa Angkatan : ", key)
#     for key_a, value_a in value.items():
#         print(key_a, " : ", value_a)
# print(" ")

# Nilai = {
#     "Matematika" : 90,
#     "Fisika" : 80,
#     "Biologi" : 80,
#     "Kimia" : 70
# }
# total = 0
# for i in Nilai.values():
#     total += i
# print(f"total nilai adalah {total}")
# print(f"rata-rata nilai adalah {total/4}")