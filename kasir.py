# Ini adalah "gudang" untuk menyimpan daftar menu.
# Awalnya kosong, nanti diisi lewat fitur Tambah Menu.
katalog_makanan = {}


def format_rupiah(nilai):
    """Format angka ke 'Rp 20,000'"""
    return f"Rp {int(nilai):,}"


def hitung_diskon(subtotal):
    """
    Diskon bertingkat.
    PENTING: urutan dari ambang terbesar ke terkecil.
    """
    if subtotal >= 150000:
        return 0.30
    elif subtotal >= 100000:
        return 0.20
    elif subtotal >= 50000:
        return 0.10
    else:
        return 0.0


def tampilkan_katalog(katalog):
    """Menampilkan daftar menu."""
    print("\n--- KATALOG MENU ---")
    for i, (nama, harga) in enumerate(katalog.items(), 1):
        print(f"{i}. {nama:<20} {format_rupiah(harga)}")
    print("0. Batal")
    print("-" * 30)


def cetak_nota(nama_pembeli, nama_makanan, harga, qty,
               subtotal, diskon_persen, diskon_nilai, total, uang, kembalian):
    """Mencetak nota sesuai format soal."""
    print("=" * 40)
    print(" " * 13 + "NOTA PEMBAYARAN" + " " * 12)
    print("=" * 40)
    print(f"{'Nama Pembeli':<14}: {nama_pembeli}")
    print(f"{'Makanan':<14}: {nama_makanan}")
    print(f"{'Harga Satuan':<14}: {format_rupiah(harga)}")
    print(f"{'Jumlah Porsi':<14}: {qty}")
    print("-" * 40)
    print(f"{'Subtotal':<14}: {format_rupiah(subtotal)}")
    print(f"{'Diskon (' + str(int(diskon_persen * 100)) + '%)':<14}: {format_rupiah(diskon_nilai)}")
    print(f"{'Total Bayar':<14}: {format_rupiah(total)}")
    print("-" * 40)
    print(f"{'Uang Tunai':<14}: {format_rupiah(uang)}")
    print(f"{'Kembalian':<14}: {format_rupiah(kembalian)}")
    print("=" * 40)
    print(" " * 4 + "Terima Kasih Atas Kunjungan Anda!" + " " * 3)
    print("=" * 40)


def tambah_menu(katalog):
    """Menu 2: Tambah menu makanan."""
    nama = input("Nama makanan: ").strip()
    if not nama:
        print("❌ Nama tidak boleh kosong.")
        return
    try:
        harga = int(input("Harga satuan (Rp): ").strip())
        if harga <= 0:
            print("❌ Harga harus lebih dari 0.")
            return
    except ValueError:
        print("❌ Harga harus berupa angka.")
        return

    katalog[nama] = harga
    print(f"✅ Menu '{nama}' ({format_rupiah(harga)}) berhasil ditambahkan.")


def transaksi(katalog):
    """Menu 1: Transaksi kasir."""
    if not katalog:
        print("Katalog makanan kosong. Silakan tambah menu di Menu 2 terlebih dahulu!")
        return

    nama_pembeli = input("Nama pembeli: ").strip()
    if not nama_pembeli:
        print("❌ Nama pembeli tidak boleh kosong.")
        return

    while True:
        tampilkan_katalog(katalog)
        pilihan = input("Pilih makanan (nomor/nama, atau '0' untuk batal): ").strip()

        if pilihan.lower() in ["0", "batal", "cancel"]:
            print("❌ Transaksi dibatalkan.")
            return

        nama_makanan = None
        if pilihan.isdigit():
            idx = int(pilihan) - 1
            daftar = list(katalog.items())
            if 0 <= idx < len(daftar):
                nama_makanan = daftar[idx][0]
        else:
            for nama in katalog:
                if nama.lower() == pilihan.lower():
                    nama_makanan = nama
                    break

        if nama_makanan:
            break

        print("❌ Makanan tidak ditemukan. Silakan pilih kembali.")

    harga = katalog[nama_makanan]

    try:
        qty = int(input("Jumlah porsi: ").strip())
        if qty <= 0:
            print("❌ Jumlah porsi harus lebih dari 0.")
            return
    except ValueError:
        print("❌ Jumlah porsi harus angka.")
        return

    subtotal = harga * qty
    diskon_persen = hitung_diskon(subtotal)
    diskon_nilai = subtotal * diskon_persen
    total = subtotal - diskon_nilai

    print(f"\nTotal yang harus dibayar: {format_rupiah(total)}")
    while True:
        try:
            uang = int(input("Uang tunai: ").strip())
        except ValueError:
            print("❌ Uang harus angka.")
            continue
        if uang < total:
            print(f"❌ Uang kurang {format_rupiah(total - uang)}. Silakan coba lagi.")
            continue
        break

    kembalian = uang - total
    cetak_nota(nama_pembeli, nama_makanan, harga, qty,
               subtotal, diskon_persen, diskon_nilai, total, uang, kembalian)


def main():
    print("=" * 40)
    print("   SELAMAT DATANG DI PEMPEK PALEMBANG   ".center(40))
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
