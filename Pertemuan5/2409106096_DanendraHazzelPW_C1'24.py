# nama = ["Hazzel", 96, True, 3.96]
# matkul = ["APD","APL","RPL","JARKOM"]
# print(nama)
# print(matkul)

# nama = ["Hazzel", 96, True, 3.96]
# matkul = ["APD","APL","RPL","JARKOM"]
# print(nama[1])

# nama = ["Hazzel", 96, True, 3.96]
# matkul = ["APD","APL","RPL","JARKOM"]
# print(matkul[-1])

# nama = ["Hazzel", 96, True, 3.96]
# matkul = ["APD",
#           "APL",
#           "RPL",
#           "JARKOM", 
#           "BASDAT", 
#           "STRUKDAT",
#           "PTI"
# ]
# print(matkul[3])

# nama = ["Hazzel", 96, True, 3.96,
#         ["Danendra", 114],3.65,
#         [123, "Putra", False, 3.66], 
#         "rehan"]
# print(nama[4][0])
# print(nama[0])

# matkul = ["APD",
#           "APL",
#           "RPL",
#           "JARKOM", 
#           "BASDAT", 
#           "STRUKDAT",
#           "PTI"
# ]
# print(matkul[2])

# makanan = ["mie ayam", "sate", "soto", "iga bakar", "ayam taliwang", "cumi goreng", "mie goreng"]
# print("sebelum : ")
# print(makanan)
# del makanan[2]
# # makanan.append("Nasi telor")
# print("Seudah : ")
# # makanan.clear()
# print(makanan)
# # data = makanan.pop(2)
# # print(makanan)
# # print(data)
# # del makanan[5]
# # print(makanan)
# # makanan.insert(2, "Nasi telor")
# # makanan[2] = "ayam joss, rendang"
# # print(makanan)

# minuman = ["es teh", "teh tarik", "jus", "air es","es buah","es kelapa"]
# print(minuman)
# del minuman [2]
# print(minuman)
# minuman[4] = "air putih"
# print(minuman)
# minuman.insert(0, "jus tomat")
# print(minuman)

# makanan = ["bakso","soto","sate","bebek"]
# # print(makanan)
# for i in makanan :
#     print(i, end=", ")

# makanan = [["balon","bakso","soto","sate","bebek"], ["teh","kopi","air"]]
# print(makanan)
# for i in makanan :
#     for j in i:
#         print(j, end= ", ")

# makanan = ["ayam","ikan",["bakso","soto","sate","ikan","bebek"], ["teh","kopi","air"]]
# for i in makanan :
#     if isinstance(i, list):
#         for j in i:
#             print(j)
#     else:
#         print(i)

# for i in makanan:
#     for j in i:
#         print(j)

# akuns = []

# while True:
#     print("Halo! selamat datang di aplikasi catatan")
#     print("Silahkan dipilih 'Daftar Akun' jika belum buat akun, dan jika sudah memiliki akun siahkan 'login'")
#     print("1. Daftar akun")
#     print("2. Login")
#     print("3. Exit")
#     print("________________________")
#     opsi = input("Oilih opsi: ")
#     print(" ")

#     if opsi == "1":
#         print("Halo pengguna baru! Ayo buat akun dulu")
#         Username = input("Username: ")
#         akuna = False
#         for akun in akuns:
#             if akun[0] == Username: 
#                 akuna = True
#                 break
#         if akuna:
#             print("Nama sudah terpakai untuk registrasi silahkan coba lagi")
#         else:
#             Password = input("Password: ")
#             akuns.append([Username, Password, []]) 
#             print(f"Akun anda berhasil teraftar dengan ID: {Username}")