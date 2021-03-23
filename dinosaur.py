class Dinosaur:
    def __init__(self):
        self.type = ''
        self.health = '100'
        self.energy = ''
        self.attack_power = '27'
        self.power_level = '84'

    def set_dino_type(self):
        response = input('what type of dinosaur would you like?')
        self.type = response
        print(f'Dino type is now {self.type}')



