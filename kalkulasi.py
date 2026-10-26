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
