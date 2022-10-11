class Whale():
    def __init__(self, species, weight, length):
        self.species = species
        self.weight = weight
        self.length = length


    def breath(self):
        print(f'{self.species} breaths with its lungs')
    def sleep(self):
        print(f'{self.species} sleeps with open eyes')
    def eat(self):
        print(f'{self.species} eats small planctons')

species = 'Blue whale'

Blue_whale = Whale('Blue whale',356,8)
Blue_whale.eat()
print(Blue_whale.species)