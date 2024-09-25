# ulang = 10
# for i in range (ulang):
#     print ("Halo")

# simpan = [12, "Udin petot", 14.5, True, "A", "102"]
# for i in simpan[2:5]:
#     print(i)
    # print(simpan)
    # print(simpan[4])

# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{i} x {j} = {i * j}")

# makanan = ["mie", "sop", "bakso"]
# minuman = ["es teh", "air putih", "es jeruk"]

# for i in makanan:
#     for j in minuman:
#         print(f"{i} & {j}")

# print("menu rumah makan informatika 24:")
# print("--------------------------------")
# simpan = ["nasi goreng", "mie goreng", "mie ayam", "bakso", "soto"]
# for i, menu in enumerate (simpan,start=1):
#     print(f"{i}.{menu}")

# print("menu rumah makan informatika 24:")
# print("--------------------------------")
# simpan = ["nasi goreng", "mie goreng", "mie ayam", "bakso", "soto"]
# for i in range(len(simpan)):
#     print(f"{i+1}. {simpan[i]}")

# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("ulang lagi tidak? ")
# print(f"Total perulangan; {hitung}")

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih ingin lanjut? ")
#     if ulang == "y" or ulang == "Y":
#         print("oke kita lanjut")
#         continue


# jawab = "ya"
# hitung = 0
# while(True):
#     hitung +=1
#     jawab = input("balikkan lagi gak? ")
#     if jawab == "ga" or jawab == "gak": 
#         break

# print("Daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print (i)

hitung = 0
while (True):
    angka = input("masukkan angka positif " or "angka negatif untuk berhenti")
    if angka < 0:
        break
    hitung += angka
    print(hitung)
