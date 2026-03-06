# NAMA  : Innosencius Roumer Ranjaan
# KELAS : 9A
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
nilai_ujian = [75, 55, 90, 85, 45, 95, 80]
print("Data Nilai Asli: ", nilai_ujian)

for i in range(len(nilai_ujian)):
  for j in range(i + 1, len(nilai_ujian)):
    if nilai_ujian[i] < nilai_ujian[j]:
      nilai_ujian[i], nilai_ujian[j] = nilai_ujian[j], nilai_ujian[i]

print("Data Setelah Diurutkan:", nilai_ujian)

beasiswa = []
for i in range(3):
  beasiswa.append(nilai_ujian[i])

print("Tiga Nilai Tertinggi (Penerima Beasiswa):", beasiswa)

nilai_lulus = []
for i in range(len(nilai_ujian)):
  if nilai_ujian[i] >= 60:
    nilai_lulus.append(nilai_ujian[i])

print("Daftar Nilai Yang Lulus:", nilai_lulus)
