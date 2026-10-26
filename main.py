from data import katalog_makanan
from menu import tambah_menu, transaksi

def main():
    print("=" * 40)
    print("   SELAMAT DATANG DI RESTORAN   ".center(40))
    print("=" * 40)

    while True:
        print("\n=== SISTEM KASIR RESTORAN ===")
        print("1. Transaksi Kasir (Input Nama Pembeli & Cetak Nota)")
        print("2. Tambah Menu Makanan (Input Nama Makanan & Harga)")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            transaksi(katalog_makanan)
        elif pilihan == "2":
            tambah_menu(katalog_makanan)
        elif pilihan == "3":
            print("Terima kasih! Sampai jumpa. 👋")
            break
        else:
            print("❌ Pilihan tidak valid. Masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    main()