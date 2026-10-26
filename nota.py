from kalkulasi import format_rupiah

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
