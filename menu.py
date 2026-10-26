# menu.py

from kalkulasi import format_rupiah, hitung_diskon
from nota import cetak_nota

def tampilkan_katalog(katalog):
    """Menampilkan daftar menu."""
    print("\n--- KATALOG MENU ---")
    for i, (nama, harga) in enumerate(katalog.items(), 1):
        print(f"{i}. {nama:<20} {format_rupiah(harga)}")
    print("-" * 30)


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

    tampilkan_katalog(katalog)
    pilihan = input("Pilih makanan (nomor/nama): ").strip()

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

    if not nama_makanan:
        print("❌ Makanan tidak ditemukan.")
        return

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