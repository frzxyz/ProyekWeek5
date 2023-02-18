import os
# inisialisasi
file = "phone_book.txt"

# Membaca data phonebook.txt
phone_book = {}
with open(file, "r") as f:
    for line in f:
        nama, nomor = line.strip().split(":")
        phone_book[nama] = nomor

while True:
    print("Phone Book\n")

    # Menu
    print("Pilih menu")
    print("1. Tambah kontak")
    print("2. Update kontak yang sudah ada")
    print("3. Hapus kontak")
    print("4. Cari kontak")
    print("5. List kontak")
    print("6. Keluar")

    Pilihan = input("Input angka (1-5): ")
    match Pilihan:
        case "1":
            # Tambah kontak
            nama = input("Masukkan nama kontak: ")
            nomor = input("Masukkan nomor telepon: ")
            phone_book[nama] = nomor
            os.system('cls')
            print(f"{nama} sudah ditambahkan dalam kontak.\n")
        case "2":
             # update kontak
            nama = input("Masukkan nama kontak: ")
            if nama in phone_book:
                nomor = input("Masukkan nomor telepon: ")
                phone_book[nama] = nomor
                os.system('cls')
                print(f"{nama} Nomor telepon sudah diupdate.\n")
            else:
                os.system('cls')
                print(f"{nama} Tidak ada dalam kontak.\n")
        case "3":
            # hapus kontak
            nama = input("Masukkan nama kontak: ")
            if nama in phone_book:
                del phone_book[nama]
                os.system('cls')
                print(f"{nama} Sudah dihapus dari kontak.\n")
            else:
                os.system('cls')
                print(f"{nama} Tidak ada dalam kontak.\n")
        case "4":
            # Cari kontak
            nama = input("Masukkan nama kontak: ")
            if nama in phone_book:
                os.system('cls')
                print(f"{nama}: {phone_book[nama]}\n")
            else:
                os.system('cls')
                print(f"{nama} D.\n")
        case "5":
            #List kontak
            if phone_book:
                os.system('cls')
                print("Kontak:")
            for nama, nomor in phone_book.items():
                print(f"{nama}: {nomor}")
            print()
        case "6":
        # Keluar program dan menulis data kontak
        #Menulis data kontak ke phonebook.txt
            with open(file, "w") as f:
                for nama, nomor in phone_book.items():
                    f.write(f"{nama}:{nomor}\n")
            os.system('cls')
            print("Sayonara!")
            break
        case _:
            print("Input tidak valid,coba lagi")


