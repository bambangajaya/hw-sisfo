class Registration:
    def register_krs(self, jenis_krs):
        if jenis_krs == "paket":
            print("Anda sedang mendaftar KRS paket.")
        elif jenis_krs == "non paket":
            print("Anda sedang mendaftar KRS non-paket.")
        else:
            print("Jenis KRS yang dimasukkan tidak valid.")
