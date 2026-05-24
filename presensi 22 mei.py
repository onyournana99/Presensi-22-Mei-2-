data_mahasiswa = [
    ["Andi",  "Tinggi",  "Lengkap"],
    ["Budi",  "Rendah",  "Tidak Lengkap"],
    ["Citra", "Tinggi",  "Tidak Lengkap"],
    ["Deni",  "Rendah",  "Lengkap"],
    ["Eka",   "Tinggi",  "Lengkap"],
    ["Fatur", "Rendah",  "Lengkap"],
]

LEBAR = 50

WARNA = {
    "reset"  : "\033[0m",
    "bold"   : "\033[1m",
    "hijau"  : "\033[92m",
    "merah"  : "\033[91m",
    "kuning" : "\033[93m",
    "cyan"   : "\033[96m",
    "putih"  : "\033[97m",
    "abu"    : "\033[90m",
}

def warna(teks, *kode):
    prefix = "".join(WARNA.get(k, "") for k in kode)
    return f"{prefix}{teks}{WARNA['reset']}"

def garis(karakter="─", lebar=LEBAR, warna_kode="abu"):
    print(warna(karakter * lebar, warna_kode))

def cetak_judul(teks, karakter="═", warna_kode="cyan"):
    print(warna(karakter * LEBAR, warna_kode))
    print(warna(teks.center(LEBAR), warna_kode, "bold"))
    print(warna(karakter * LEBAR, warna_kode))

def klasifikasi(kehadiran, tugas):
    if kehadiran == "Tinggi":
        status = "Aktif"
        keterangan = "Mahasiswa Disiplin" if tugas == "Lengkap" else "-"
    else:
        status = "Tidak Aktif"
        keterangan = "-"
    return status, keterangan

def rekomendasi(kehadiran, tugas):
    if kehadiran == "Tinggi" and tugas == "Lengkap":
        return "Pertahankan prestasi!", "hijau"
    elif kehadiran == "Tinggi" and tugas == "Tidak Lengkap":
        return "Segera lengkapi tugas.", "kuning"
    elif kehadiran == "Rendah" and tugas == "Lengkap":
        return "Tingkatkan kehadiran!", "kuning"
    else:
        return "Konsultasi ke dosen.", "merah"

# ─────────────────────────────────────────
def cetak_menu():
    print()
    menu = [
        ("1", "Tampilkan Semua Data Mahasiswa (Kartu)", "hijau"),
        ("2", "Tampilkan Tabel Ringkasan",              "hijau"),
        ("3", "Tampilkan Statistik Kelas",              "hijau"),
        ("4", "Cek Status Mahasiswa Tertentu",          "hijau"),
        ("0", "Keluar",                                 "merah"),
    ]
    for nomor, label, warna_nomor in menu:
        print(f"  {warna(f'[{nomor}]', warna_nomor)} {warna(label, 'putih')}")
    print()
    print(warna("  Pilih menu: ", "putih"), end="")

# ─────────────────────────────────────────
def tampilkan_kartu():
    print()
    cetak_judul("  SISTEM PRESENSI MAHASISWA  ")
    print(warna("  Mata Kuliah : Kecerdasan Komputasional".ljust(LEBAR), "abu"))
    garis("═", warna_kode="cyan")
    print()
    for i, mhs in enumerate(data_mahasiswa, 1):
        nama, kehadiran, tugas = mhs
        status, keterangan = klasifikasi(kehadiran, tugas)
        saran, warna_saran = rekomendasi(kehadiran, tugas)
        warna_status = "hijau" if status == "Aktif" else "merah"
        print(warna(f"  [{i}] {nama}", "putih", "bold"))
        garis("─")
        print(f"  {'Kehadiran':<14}: {warna(kehadiran, 'cyan')}")
        print(f"  {'Tugas':<14}: {warna(tugas, 'cyan')}")
        print(f"  {'Status':<14}: {warna(status, warna_status, 'bold')}")
        print(f"  {'Keterangan':<14}: {warna(keterangan, 'kuning')}")
        print(f"  {'Rekomendasi':<14}: {warna(saran, warna_saran)}")
        garis("─")
        print()

# ─────────────────────────────────────────
def tampilkan_tabel():
    print()
    cetak_judul("  TABEL RINGKASAN MAHASISWA  ")
    header = f"  {'No':<4} {'Nama':<10} {'Kehadiran':<12} {'Tugas':<16} {'Status':<12} {'Keterangan'}"
    print(warna(header, "cyan", "bold"))
    garis("─")
    for i, mhs in enumerate(data_mahasiswa, 1):
        nama, kehadiran, tugas = mhs
        status, keterangan = klasifikasi(kehadiran, tugas)
        warna_status = "hijau" if status == "Aktif" else "merah"
        print(f"  {warna(str(i), 'abu'):<4} {nama:<10} {kehadiran:<12} {tugas:<16} "
              f"{warna(status, warna_status):<20} {keterangan}")
    garis("─")

# ─────────────────────────────────────────
def tampilkan_statistik():
    total    = len(data_mahasiswa)
    aktif    = sum(1 for m in data_mahasiswa if klasifikasi(m[1], m[2])[0] == "Aktif")
    tidak    = total - aktif
    disiplin = sum(1 for m in data_mahasiswa if m[1] == "Tinggi" and m[2] == "Lengkap")
    persen   = round((aktif / total) * 100) if total else 0

    print()
    cetak_judul("  STATISTIK KELAS  ")
    print(f"  {'Total Mahasiswa':<30}: {warna(str(total), 'putih', 'bold')}")
    print(f"  {'Jumlah Aktif':<30}: {warna(str(aktif), 'hijau', 'bold')}")
    print(f"  {'Jumlah Tidak Aktif':<30}: {warna(str(tidak), 'merah', 'bold')}")
    print(f"  {'Mahasiswa Disiplin':<30}: {warna(str(disiplin), 'cyan', 'bold')}")
    print(f"  {'Tingkat Keaktifan':<30}: {warna(str(persen) + '%', 'kuning', 'bold')}")
    garis("═", warna_kode="cyan")

# ─────────────────────────────────────────
def cek_status_tertentu():
    print()
    cetak_judul("  CEK STATUS MAHASISWA  ")
    print(warna("  Nama mahasiswa: ", "putih"), end="")
    cari = input().strip().title()
    ditemukan = False
    for mhs in data_mahasiswa:
        if mhs[0].lower() == cari.lower():
            nama, kehadiran, tugas = mhs
            status, keterangan = klasifikasi(kehadiran, tugas)
            saran, warna_saran = rekomendasi(kehadiran, tugas)
            warna_status = "hijau" if status == "Aktif" else "merah"
            garis("─")
            print(f"  {'Nama':<14}: {warna(nama, 'putih', 'bold')}")
            print(f"  {'Kehadiran':<14}: {warna(kehadiran, 'cyan')}")
            print(f"  {'Tugas':<14}: {warna(tugas, 'cyan')}")
            print(f"  {'Status':<14}: {warna(status, warna_status, 'bold')}")
            print(f"  {'Keterangan':<14}: {warna(keterangan, 'kuning')}")
            print(f"  {'Rekomendasi':<14}: {warna(saran, warna_saran)}")
            garis("─")
            ditemukan = True
            break
    if not ditemukan:
        print(warna(f"  ✗ Mahasiswa '{cari}' tidak ditemukan.", "merah"))

cetak_judul("  SISTEM PRESENSI MAHASISWA  ")

while True:
    cetak_menu()
    pilihan = input().strip()

    if   pilihan == "1": tampilkan_kartu()
    elif pilihan == "2": tampilkan_tabel()
    elif pilihan == "3": tampilkan_statistik()
    elif pilihan == "4": cek_status_tertentu()
    elif pilihan == "0":
        print(warna("\n  Sampai jumpa!\n", "cyan", "bold"))
        break
    else:
        print(warna("  ✗ Pilihan tidak valid!", "merah"))