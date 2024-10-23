# angka = int(input("Masukkan Angka : "))
# print(angka)

# nama = ["Andi", "Budi", "Caca"]
# print(nama[1])

# try :
#     angka = int(input("Masukkan Angka: "))
#     print(angka)
# except ValueError :
#     print("Input anda salah, input yang harus dimasukkan hanya berupa angka")

# try :
#     angka = int(input("Masukkan Angka: "))
#     if angka  == 0:
#         print("Berhasil")
#     elif angka  == 1:
#         print("Berhasil")
#     else:
#         print("Pilih antara 0 dan 1")
# except ValueError:
#     print("Input tidak valid")

# try :
#     nama = input("Hai, Siapa nama anda? : ")
#     if len(nama) > 5:
#         raise ValueError("Nama tidak boleh lebih dari 5 karakter")
# except ValueError as a :
#     print(a)

# try :
#     angka = int(input("Masukkan Angka: "))
#     if angka  == 0:
#         print("Berhasil")
#     elif angka  == 1:
#         print("Berhasil")
#     else:
#         print("Pilih antara 0 dan 1")
# except ValueError:
#     print("Input tidak valid")
# finally:
#     print("Program selesai")


# def penjumlahan():
#     try:
#         angka1 = int(input("Angka pertama : "))
#         angka2 = int(input("Angka Kedua : "))
#         hasil = angka1+angka2
#         print(f"Hasil penjumlahan {angka1}+{angka2} = {hasil}")
#     except ValueError:
#         print("Input yang anda masukkan tidak valid")

# def menu():
#     while True :
#         print("Halo bos, selamat datang di aplikasi penjumlahan paling akurat")
#         print("============MENU============")
#         print("1. Penjumlahan")
#         print("2. Exit")
        
#         try:
#             pilihan = int(input("Pilih Menu : "))
#             if pilihan == 1:
#                 penjumlahan()
#             elif pilihan == 2:
#                 print("oke, BaiBai")
#                 break
#             else:
#                 print("Milih yang bener!")
#         except ValueError:
#             print("Dibilangin milih yang bener")

# menu()