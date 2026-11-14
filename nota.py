from kalkulasi import format_rupiah

def cetak_nota(nama_pembeli, nama_makanan, harga, qty,
               subtotal, diskon_persen, diskon_nilai, total, uang, kembalian):
    diskon_label = f"Diskon ({int(diskon_persen * 100)}%)"

    print("\n" + "=" * 40)
    print("NOTA PEMBAYARAN".center(40))
    print("=" * 40)
    print(f"{'Nama Pembeli':<14}: {nama_pembeli}")
    print(f"{'Makanan':<14}: {nama_makanan}")
    print(f"{'Harga Satuan':<14}: {format_rupiah(harga)}")
    print(f"{'Jumlah Porsi':<14}: {qty}")
    print("-" * 40)
    print(f"{'Subtotal':<14}: {format_rupiah(subtotal)}")
    print(f"{diskon_label:<14}: {format_rupiah(diskon_nilai)}")
    print(f"{'Total Bayar':<14}: {format_rupiah(total)}")
    print("-" * 40)
    print(f"{'Uang Tunai':<14}: {format_rupiah(uang)}")
    print(f"{'Kembalian':<14}: {format_rupiah(kembalian)}")
    print("=" * 40)
    print("Terima Kasih Atas Kunjungan Anda!".center(40))
    print("=" * 40 + "\n")

