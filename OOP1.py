class Whale():
    species = None
    height = None
    weight = None
    habitat = None

    def __init__(self):
        print("Ini dalah Paus")

    def breath(self):
        print(f'{self.species} breaths with its lungs')
    def sleep(self):
        print(f'{self.species} sleeps with open eyes')
    def eat(self):
        print(f'{self.species} eats small planctons')

blue_whale = Whale()
blue_whale.species = 'blue_whale'
blue_whale.heiight = 546
blue_whale.weight = 329
blue_whale.habitat = 'antartica'

print(blue_whale.species)
print(f'{blue_whale.species} breaths with its lungs')
blue_whale.sleep()
blue_whale.eat()


class Bonsai():

    species = None
    color = None
    height = None

    def menyerap_air(self):
        print(f'{self.species} menyerap banyak air dalam waktu singkat')
    def berfotosintesis(self):
        print(f'{self.species} berfotosintesis banyak pada pagi hari')
    def berbunga(self):
        print(f'{self.species} berbunga pada suhu sekitar 20-30 derajat celcius')

bonsai_jepang = Bonsai()
bonsai_jepang.species = 'bonsai jepang'
bonsai_jepang.color = 'pink'
bonsai_jepang.height = 125
bonsai_jepang.menyerap_air()
bonsai_jepang.berfotosintesis()
bonsai_jepang.berbunga()


# Chianing
class Warteg():

    def __init__(self) -> None:
        self.total = 0
        self.item = []

    def nasi(self):
        self.item.append('Nasi 1 porsi')
        self.total = self.total+3000
        return self

    def bakwan(self):
        self.item.append('Bakwan 1 biji')
        self.total = self.total+1000
        return self

    def kangkung(self):
        self.item.append('Sayur kangkung')
        self.total = self.total+2500
        return self

    def ayam_krispi(self):
        self.item.append('Ayam krispi')
        self.total = self.total+8500
        return self

    def kerupuk_udang(self):
        self.item.append('Kerupuk udang')
        self.total = self.total+2500
        return self

    def bayar(self):
        print(f'Item :{self.item}')
        print(f'Total :{self.total}')



mas_mas1 = Warteg().nasi().bakwan().ayam_krispi().kangkung().bayar()
