from datetime import datetime

# === MENU LENGKAP ===
menu_makanan = {
    1: ("Nasi Goreng Spesial", 20000),
    2: ("Nasi Goreng Seafood", 23000),
    3: ("Ayam Geprek Sambal Ijo", 18000),
    4: ("Ayam Bakar Madu", 21000),
    5: ("Mie Ayam Bakso", 15000),
    6: ("Soto Ayam Lamongan", 17000),
    7: ("Bakso Mercon Pedas", 18000),
    8: ("Kwetiau Goreng", 19000),
    9: ("Nasi Uduk Ayam Goreng", 16000),
    10: ("Nasi Liwet Spesial", 22000),
    11: ("Ikan Bakar Rica-Rica", 23000),
    12: ("Cumi Saus Tiram", 25000),
    13: ("Udang Tepung Krispi", 24000),
    14: ("Sapi Lada Hitam", 27000)
}

menu_snack = {
    1: ("Tempe Mendoan", 7000),
    2: ("Tahu Crispy", 8000),
    3: ("Kentang Goreng", 10000),
    4: ("Sosis Bakar", 9000),
    5: ("Pisang Goreng Coklat", 9000),
    6: ("Roti Bakar Keju", 11000),
    7: ("Cireng Isi Pedas", 8000),
    8: ("Donat Mini", 9000)
}

menu_minuman = {
    1: ("Es Teh Manis", 5000),
    2: ("Es Jeruk Segar", 6000),
    3: ("Jus Alpukat", 10000),
    4: ("Kopi Susu Gula Aren", 12000),
    5: ("Lemon Tea Dingin", 8000),
    6: ("Es Campur", 13000),
    7: ("Milkshake Coklat", 12000),
    8: ("Teh Hangat", 5000),
    9: ("Cappuccino Panas", 10000)
}

# helper: format rupiah
def rp(x):
    return f"Rp{int(x):,}"

def pilih_menu_kategori(kategori):
    if kategori == 1:
        collection = menu_makanan
        heading = "🍛 Makanan Utama"
    elif kategori == 2:
        collection = menu_snack
        heading = "🍟 Snack"
    else:
        collection = menu_minuman
        heading = "🍹 Minuman"

    print(f"\n--- {heading} ---")
    for k, (nama, harga) in collection.items():
        print(f"{k}. {nama:<25} {rp(harga)}")
    pilih = int(input("Pilih nomor menu: "))
    jumlah = int(input("Jumlah: "))
    nama, harga = collection[pilih]
    return nama, harga, jumlah

# MAIN LOOP
while True:
    total = 0
    pesanan = []

    while True:
        print("\n=== PILIH KATEGORI ===")
        print("1. Makanan Utama 🍛")
        print("2. Snack 🍟")
        print("3. Minuman 🍹")
        kategori = int(input("Masukkan nomor kategori (1-3): "))
        try:
            nama, harga, jumlah = pilih_menu_kategori(kategori)
        except Exception as e:
            print("Pilihan tidak valid, coba lagi.")
            continue

        subtotal = harga * jumlah
        pesanan.append((nama, jumlah, subtotal))
        total += subtotal
        if input("Tambah pesanan lagi? (y/n): ").lower() != 'y':
            break

    diskon = int(round(0.10 * total)) if total > 100000 else 0
    ppn = int(round(0.11 * (total - diskon)))
    total_akhir = (total - diskon) + ppn

    print("\n=== METODE PEMBAYARAN ===")
    print("1. Tunai")
    print("2. Transfer (BRI, BNI, Mandiri, BCA)")
    print("3. QRIS")
    metode = int(input("Pilih metode (1-3): "))

    if metode == 1:
        metode_bayar = "Tunai"
        while True:
            bayar = int(input(f"Masukkan uang tunai (minimal {rp(total_akhir)}): "))
            if bayar < total_akhir:
                print("Uang tidak cukup. Masukkan jumlah yang sesuai.")
            else:
                break
        kembalian = int(bayar - total_akhir)
    elif metode == 2:
        print("Pilih Bank: 1.BRI 2.BNI 3.Mandiri 4.BCA")
        bank = int(input("Bank (1-4): "))
        bank_nama = {1: "BRI", 2: "BNI", 3: "Mandiri", 4: "BCA"}[bank]
        metode_bayar = f"Transfer via {bank_nama}"
        bayar = int(total_akhir)
        kembalian = 0
        print(f"Silakan transfer ke rekening {bank_nama}: 1234567890 a.n WARUNG SINDI & RESTI")
    elif metode == 3:
        metode_bayar = "QRIS"
        bayar = int(total_akhir)
        kembalian = 0
        print("Silakan scan QRIS untuk pembayaran...")
    else:
        metode_bayar = "Lainnya"
        bayar = int(total_akhir)
        kembalian = 0

    waktu = datetime.now()
    tanggal_str = waktu.strftime("%d/%m/%Y %H:%M:%S")
    nomor_transaksi = waktu.strftime("#TRX-%Y%m%d-%H%M%S")

    garis = "=" * 44
    lines = []
    lines.append(garis)
    lines.append("         🧾 WARUNG KEL 5 🧾")
    lines.append(f"   Nomor Transaksi : {nomor_transaksi}")
    lines.append(f"   Waktu           : {tanggal_str}")
    lines.append(f"   Metode Pembayaran: {metode_bayar}")
    lines.append(garis)
    for i, (nama, jumlah, subtotal) in enumerate(pesanan, start=1):
        lines.append(f"{i}. {nama:<25} x{jumlah:<2} {rp(subtotal)}")
    lines.append("-" * 44)
    lines.append(f"{'Subtotal':<30} {rp(total):>10}")
    lines.append(f"{'Diskon (10%)':<30} {rp(diskon):>10}")
    lines.append(f"{'PPN (11%)':<30} {rp(ppn):>10}")
    lines.append(f"{'Total Akhir':<30} {rp(total_akhir):>10}")
    if metode == 1:
        lines.append(f"{'Tunai':<30} {rp(bayar):>10}")
        lines.append(f"{'Kembalian':<30} {rp(kembalian):>10}")
    lines.append(garis)
    lines.append("🙏 Terima kasih, silahkan tunggu pesanan anda 🙏")
    lines.append(garis)

    print("\n".join(lines))

    filename = f"struk_{nomor_transaksi}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n✅ Struk berhasil disimpan ke file '{filename}'")

    if input("\nPesan lagi? (y/n): ").lower() != 'y':
        print("\n🍽️ Terima kasih, silahkan tunggu pesanan anda 🙏")
        break
