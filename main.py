class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main():
    try:
        # Meminta input dari pengguna
        panjang = float(input("Masukkan panjang (cm): "))
        lebar = float(input("Masukkan lebar (cm): "))

        # Validasi input
        if panjang <= 0 or lebar <= 0:
            print("Panjang dan lebar harus lebih besar dari 0.")
            return

        # Membuat objek PersegiPanjang
        persegi_panjang = PersegiPanjang(panjang, lebar)

        # Menampilkan hasil
        print(persegi_panjang)
        print(f"Keliling: {persegi_panjang.keliling()} cm")
        print(f"Luas: {persegi_panjang.luas()} cm²")

    except ValueError:
        print("Input tidak valid. Masukkan angka untuk panjang dan lebar.")

# Memanggil fungsi main
if __name__ == "__main__":
    main()
