import random

class Fighter:

    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self._health = starting_health
        self.weapon = weapon
        self.shield = shield
    
    def report(self):
        print(self.name+" |"+" Health: "+str(self._health))

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        return attack_power
    
    def get_health(self):
        return self._health
    
    #This function allows the health to be updated as health is a private attribute that should be modified within the class
    def set_health(self, hp_loss):
    #Takes parameters of the hp_loss variables and subtracts it from the health attribute
        self._health = self._health - hp_loss
        return self._health


you = Fighter("You", 100, 60, 20)
troll = Fighter("Troll", 200, 30, 10)

def play_game(player, enemy):
#Define null values for hp_loss and winner
    hp_loss = 0
    winner = ""
#Loop continues until either the player or enemy's health is 0 or less
    while player._health > 0 or enemy._health > 0:
#The program prints out the status of the enemy and player
        player.report()
        enemy.report()
        print("- You attack the enemy -")
#The variable of hp_loss is randomly defined
        hp_loss = player.random_attack()
#Then using the new variable the health is updated
        enemy.set_health(hp_loss)
#The program then checks whether the enemy has lost all hp and if it has, the player won, and so winner gains the value of the player's name
        if enemy._health < 0:
            winner = player.name
#First print the final result of the game
            player.report()
            enemy.report()
            print("\n...Enemy defeated...")
#Function ultimately returns the name of the victor
            return winner

#The program prints out the status of the enemy and player
        player.report()
        enemy.report()
        print("- The enemy attacks you -")
#The variable of hp_loss is randomly defined
        hp_loss = enemy.random_attack()
#Then using the new variable the health is updated
        player.set_health(hp_loss)
#The program then checks whether the player has lost all hp and if they have, the enemy wins, and so the winner variable gains the value of the enemy's name
        if player._health < 0:
            winner = enemy.name
#First print the final result of the game
            player.report()
            enemy.report()
            print("\n...You lost...")
#Function ultimately returns the name of the victor
            return winner

#To test, the game function is run and the winner returned is printed as the victor.
print(play_game(you, troll) + " won the game!\n")


