#nama: irvan syah putra purba(2409010107)

#List Nama Sayuran Berwarna Hijau
list_sayuran_berwarna_hijau = ['bayam', 'sawi', 'brokoli', 'selada', 'kangkung', 'kubis', 'buncis']
print(list_sayuran_berwarna_hijau)

#Menambah 5 Nama Sayuran Ke List
list_sayuran_berwarna_hijau.extend(['seledri', 'asparagus', 'timun', 'pakchoy', 'kemangi'])
print(list_sayuran_berwarna_hijau)

#Hapus 2 Sayur Posisi Depan
list_hasil = list_sayuran_berwarna_hijau[2:]
print(list_hasil)

#Menambah N Item Sayuran (Dimana N Merupakan Angka NPM Terakhir)
npm = 2409010107
npm_terakhir = 7
sayur_baru = ['kenikir', 'kale', 'pare']
list_hasil.extend(sayur_baru[:npm_terakhir])

#Output Hasil Akhir
print(list_hasil)