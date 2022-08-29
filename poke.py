# create a Pokemon
class Pokemon:
    def __init__(self, name, primary_type,max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self) -> str:
        return f"{self.name} ({self.primary_type})"


    # take a look at it
    # feed them to increase health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp +=1
            print(f"{self.name} has now {self.hp} HP.")
        else:
            print(f"{self.name} is full.")

    # make them battle & decide a winner
    def battle(self, other):
        print("Battle:"self.name, other.name)
        # calling typewheel
        result = self.typewheel(self.primary_type, other.primary_type)
        if result == 'lose':
            self.hp = 0
            print(f"{self.name} fainted!")
        elif result == 'tie':
            self.hp -= 10
            other.hp -= 10
            print(f"{self.name} and {other.name} battled hard. It's a tie.")
        elif result == 'win':
            other.hp = 0
            print(f"{self.name} won. Congratulations!")

    @staticmethod
    def typewheel(type1,type2):
        result_map = {0:'lose',1:"win",-1:'tie'}
        #mapping bw types & result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # Win-lose matrix
        rps_table = [
            [-1, 1, 0],  # water
            [0, -1, 1],  # fire
            [1, 0, -1]   # grass
        ]
        result = rps_table[game_map[type1]][game_map[type2]]
        return result_map[result]

if __name__ == '__main__':
    bulbasaur = Pokemon("Bullbi", "Grass")
    charmander = Pokemon("charmander", "fire")
    print(bulbasaur)
    print(charmander)