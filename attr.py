class Whale():
    def __init__(self):
        self.species = None #public
        self.weight = None
        self.__respiratory_organ = "Lung" #private attr

    def getRespiratory_organ(self): #get private attr
        return self.__respiratory_organ
    def setRespiratory_organ(self, value):
        self.__respiratory_organ = value

    def breath(self):
        print(f'{self.species} breath with {self.getRespiratory_organ()}')

    



w = Whale()
print(w.species)
w.species = "Orcha"
print(w.species)
print(w.getRespiratory_organ())
w.setRespiratory_organ("Gill")
print(w.getRespiratory_organ())
w.breath()


class Superhero():

    def __init__(self):
        self.name = None
        self.gender = None
        self.__marital_status = 'Married'
    
    def get_marital_status(self):
        return self.__marital_status

    def attack(self):
        print(f'{self.name} attacts moderately')
    
    


S = Superhero()
S.name = 'Thor'
print(S.name)
print(S.get_marital_status())
S.attack()



class Wizard():
    def __init__(self):
        self.name = None
        self.group = None
        self.__heritage = 'Muggle'
    
    def get_heritage(self):
        return self.__heritage
    
    def set_heritage(self, value):
        self.__heritage = value
    
    def spell(self):
        print(f'{self.name} spells with a wand')

W = Wizard()
W.name = 'Luna'
W.group = 'Griffindor'
print(W.name)
print(W.get_heritage())
W.set_heritage('Rudolph')
print(W.set_heritage('Rudolph'))
W.spell()

    
  



