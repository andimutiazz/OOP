class Whale():
    species = None
    height = None
    weight = None
    habitat = None

    def breath(self):
        print(f'{self.species} breaths with its lungs')
    def sleep(self):
        print(f'{self.species} sleeps with open eyes')
    def eat(self):
        print(f'{self.species} eats small planctons')

    def __init__(self, s, hg, wg, hb): # method yang pertama kali akan di baca sama class
        self.species = s
        self.height = hg
        self.weight = wg
        self.habitat = hb

w = Whale("Orcha", 50,200, "antartika")
w.sleep()
w.eat()
w.sleep()
w.eat()

class Bonsai():
    species = None
    height = None
    color = None

    def __init__(self, species, height, color):
        self.species = species
        self.height = height
        self.color = color

    def absorb_water(self):
        print(f'{self.species} absorb water slowly')

    def bloom(self):
        print(f'{self.species} blooms monthly')
        
    def produce_o2(self):
        print(f'{self.species} produce o2 quickly at night')


b = Bonsai('Jepang', 112, 'pink')
b.absorb_water()
b.bloom()
b.produce_o2()



