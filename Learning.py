
class Learning:
    def __init__(self):
        self.jadwal_pelajaran = {
            "Senin": {"matakuliah": "ANALISA & PERANCANGAN SI", "nilai": 80, "ruang": "A101"},
            "Selasa": {"matakuliah": "ANALISA & PERANCANGAN PROSES BISNIS", "nilai": 75, "ruang": "B203"},
            "Rabu": {"matakuliah": "MANAJEMEN SISTEM INFORMASI", "nilai": 85, "ruang": "C305"},
            "Kamis": {"matakuliah": "PEMROGRAMAN BERORIENTASI OBJEK", "nilai": 70, "ruang": "D407"},
            "Jumat": {"matakuliah": "pemrograman website lanjutan", "nilai": 90, "ruang": "E509"}
        }
        self.mahasiswa = None

    def check_schedule(self):
        print("Jadwal Pelajaran:")
        for hari, detail in self.jadwal_pelajaran.items():
            print(f"{hari}: {detail['matakuliah']} - Ruang {detail['ruang']}")

    def check_grades(self):
        print("Nilai Pelajaran:")
        for hari, detail in self.jadwal_pelajaran.items():
            print(f"{hari}: {detail['matakuliah']} - Nilai: {detail['nilai']}")

    def check_classroom(self):
        print("Ruang Kelas:")
        for hari, detail in self.jadwal_pelajaran.items():
            print(f"{hari}: {detail['matakuliah']} - Ruang {detail['ruang']}")

    def isi_nilai(self, mahasiswa, nilai):
        if self.mahasiswa is not None and mahasiswa.username == self.mahasiswa.username:
             for hari, detail in self.jadwal_pelajaran.items():
                if detail["matakuliah"] == mahasiswa.learning_instance.jadwal_pelajaran[hari]["matakuliah"]:
                    detail["nilai"] = nilai
                    print(f"Nilai untuk {mahasiswa.username} pada hari {hari} telah diisi.")
                    break
        else:
            print("Mahasiswa atau matakuliah tidak ditemukan.")
        
    