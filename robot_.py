class Robot:
    def __init__(self):
        self.name = ''
        self.health = '100'
        self.power_level = '35'
        self.weapon_type = ''
        self.attack_power = '14'
#setting robot name to prompt user:

    def set_robot_name(self):
        response = input()
        self.name = response
        print(f'Robot Name is Now {self.weapon_type}')

#setting weapon to user prompt:

    def set_weapon_type(self):
        response = input('what type of Weapon would you like?')
        self.weapon_type = response
        print(f'Weapon type is now {self.weapon_type}')
