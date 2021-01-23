mahasiswa = [
    ["Amira Jauharah Diffa","Perempuan","Pamulang"],
    ["Ariq Ikbar Darwansyah","Laki-laki","Batam"],
    ["Bagas Wahyu Putra","Laki-laki","Nganjuk"],
    ["Bryan Ronald Talisman","Laki-laki","Papua"],
    ["Dea Gina Dewi Sihotang","Perempuan","Medan"],
    ["Dana Noviandi","Laki-laki","Jakarta"],
    ["Danar Prayoga","Laki-laki","Banten"],
    ["Geldisen Afrananta","Laki-laki","Bandung"],
    ["Gildas Agathon Cato","Laki-laki","Bandung"],
    ["Hamim Nugraha","Laki-laki","Klaten"],
    ["Hasan Abdullah Muhammad","Laki-laki","Mojokerto"],
    ["Luthfi Fitra Musyaffa","Laki-laki","Bandung"],
    ["Made Gangga Wiwardhana","Laki-laki","Bogor"],
    ["Michael Christensen Kasparov Bonar","Laki-laki","Bandung"],
    ["Muhammad Daffi Daulay","Laki-laki","Medan"],
    ["Muhammad Faris Nurliyan","Laki-laki","Bandung"],
    ["Muhammad Lukman Bahrul Hikam","Laki-laki","Klaten"],
    ["Muhammad Naufal Wirawan","Laki-laki","Bandung"],
    ["Muhammad Rizqan Aditama","Laki-laki","Bogor"],
    ["Muhammad Sipa Fauzi","Laki-laki","Cianjur"],
    ["Neta Aulya Kurnia Ningrum","Perempuan","Bekasi"],
    ["Nicolaus Advendea Indrayono Putra","Laki-laki","Klaten"],
    ["Raihan Daffa Advokatya Putra","Laki-laki","Semarang"],
    ["Ramiz Qudamah","Laki-laki","Depok"],
    ["Revyolla Ananta Dila","Perempuan","Padang"],
    ["Rymarshanda Syifa Wardhana","Perempuan","Bandung"],
    ["Salsabilla Zahrani Amril","Perempuan","Padang"],
    ["Sekar Tamara Indhira","Perempuan","Cirebon"],
    ["Shazkia Septiaweni","Perempuan","Padang"],
    ["Silmy Sephia Nurashila","Perempuan","Purwakarta"],
    ["Siti Munawarrah Sapna","Perempuan","Makassar"],
    ["Tiara Aurellia Putri Insyira","Perempuan","Malang"],
    ["Tiara Hati Giwangkara","Perempuan","Jambi"],
    ["Tiara Rahmania Hadiningrum","Perempuan","Surabaya"],
    ["Wawan Wanda Adi Jatmiko","Laki-laki","Kalimantan"],
    ["Yadi Nugraha","Laki-laki","Bandung"],
    ["Yumna Zahran Ramadhan","Laki-laki","Kepulauan Riau"],
    ["Yunus Ardiansyah","Laki-laki","Karawang"]
]
def search_nested(mahasiswa, val):
    for i in range(len(mahasiswa)):
        for j in range(len(mahasiswa[i])):
            #print i,j
            if mahasiswa[i][j] == val:
                return mahasiswa[i]
    return str(val) + ' not found'

print("-----SELAMAT DATANG DI APLIKASI ABSEN SI-43-04-----")
print("1. Lihat Nama Mahasiswa")
print("2. Lihat Jenis Kelamin Mahasiswa Berdasarkan Nama")
print("3. Lihat Asal Mahasiswa Berdasarkan Nama")
print("4. Lihat Data Lengkap")
pilih=input("Silahkan masukkan no pilihan:")
if pilih =="1":
    for i in mahasiswa:
        print(i[0])
elif pilih == "2":
    nama = input("Masukkan nama untuk melihat jenis kelamin:")
    hasil = search_nested(mahasiswa, nama)
    print(hasil[1])
elif pilih == "3":
    asal = input("Masukkan nama untuk melihat asal :")
    hasilasal = search_nested(mahasiswa, asal)
    print(hasilasal[2])
elif pilih == "4":
    print(mahasiswa)
else:
    print("Pilihan anda tidak ada")     