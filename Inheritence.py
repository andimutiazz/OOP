class Tumbuhan():
    def __init__(self):
        self.kelas = 'tanaman hias'
        self.habitat = 'daerah_lembab'
        self.__berbunga = False

    def get_berbunga(self):
        return self.__berbunga

    def menyerap_air(self):
        print(f'tumbuhan {self.kelas} menyerap air denga cepat')


t = Tumbuhan()
t.menyerap_air()

class Anggrek(Tumbuhan):
    def __init__(self):
        self.jenis = 'anggrek bulan'
        self.warna = 'ungu'
        self.maximum_tinggi = 145
        Tumbuhan.__init__(self)

    def megusir_nyamuk (self):
        print(f'tumbuhan {self.jenis} megusir mebgusir nyamuk denga cepat')
        

A = Anggrek()
print(A.habitat)


        

    