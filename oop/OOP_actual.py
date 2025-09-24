import random, time

class Player:
#Defining some basic attributes that the Player has
    def __init__(self, type, intro="", priv_enemy1="", priv_enemy2="", starting_health=100, shield=3, skill=1):
        self.__health = starting_health
        self.shield = shield
        self.skill = skill
        self.type = type
#For each unique player type there are specific characters to add to the lore of the game.
        if self.type == "1":
            self.intro = "You work at a gas station. \nYour night shifts are too long. \nYour law diploma is useless in this world. \nNo jobs, no money. \nYou see the emotions of the people around you, but feel like a blank slate yourself. \nYou feel nothing. \nThe only thing that dilates your pupils is the sharp waft of gasoline each evening. \nHopelessness reigns supreme."
            self.priv_enemy1 = Enemy("Apparition", 1.5, 10, "'You forgot to clock out yesterday. I'll have to let you go if you keep being a nuisance. I pay you too much anyway'", "Your manager")
            self.priv_enemy2 = Enemy("Apparition", 1.5, 10, "'You'll make a truly gifted lawyer one day. There's plenty of potential…'", "Your professor")
        elif self.type == "2":
            self.intro = "You lost all of your money in a rigged business deal only a week ago, and your entrepreneurial empire has fallen to dust. \nYour fresh set of veneers will only last 20 years. \nBut honestly, would you even be able to survive until then? \nThe bright shade of white is too overbearing. "
            self.priv_enemy1 = Enemy("Apparition", 1.5, 10, "'What are you talking about? What assets? I didn't steal anything. You're gaslighting me.'", "Your childhood friend")
            self.priv_enemy2 = Enemy("Apparition", 1.5, 10, "'You need to become self-sufficient; I can't buy and cook you food for your entire life'", "Your late mother")
        elif self.type == "3":
            self.intro = "You've returned from the war. \nA machete has left its mark across your face, and whilst it's mostly healed now, the trail of discoloration reminds you of the pain. \nThere's no one to return to. \nYou feel more lost in your home city than in the unfamiliar plains of Europe."
            self.priv_enemy1 = Enemy("Apparition", 1.5, 10, "'That scar looks like it hurt a lot once. One of my friends lost an arm when he served a few decades ago. It's a miracle he made it out alive.'", "The homeless man")
            self.priv_enemy2 = Enemy("Apparition", 1.5, 10, "'Please give this pocket watch to my son. They'll give you my address. You know what to tell them.'", "Your friend in combat")
        elif self.type == "4":
            self.intro = "A packed suitcase sits in the corner of the hotel. \nYou've cut all ties. \nMissing in action. \nBut, you're freshly legal, so nobody can find you. \nYou are now completely alone, in the middle of nowhere. \nYou're starting again. \nBut you don't know how, or why you've decided to leave."
            self.priv_enemy1 = Enemy("Apparition", 1.5, 10, "'Off to see a family member for Christmas? I wish I could see my family more.'", "The bus driver")
            self.priv_enemy2 = Enemy("Apparition", 1.5, 10, "'When I grow up I'm gonna be a cool adult just like you and hang out with all my friends and ask you to take me to McDonald's every day!'", "Your sister")

    def load_stats(self):
#Taken from the original code, this component displays the status of the attributes
        print("\nYour Stats:\n" + "Health: " + str(self.__health) + "\n" +"Skill: " + str(self.skill) + "\n"+ "Shield: " + str(self.shield))

#Also taken from the original code, this checks the status of the health and returns a value of true or false to signify whether the player is out of health or not 
    def is_dead(self):
        if self.__health <=0:
            return True
        else:
            return False
    
#More complex, ambitious attack that requires effort
    def launch_attack(self):
        attack_power = 10 * self.skill
        target = random.randint(1,5)
        print("\nDistance: " + str(target) + " metres.")
        time.sleep(2)
        print("...")
        initial = time.time()
        input()
        final = time.time()
        distance_accuracy = final - initial
#This if-elif component checks how close the player was to the target and decides on a multiplier. 
        if distance_accuracy > target+1 or distance_accuracy < target-1:
            multiplier = 2
        elif distance_accuracy > target+0.5 or distance_accuracy <target-0.5:
            multiplier = 3
        elif distance_accuracy > target+0.2 or distance_accuracy <target-0.2:
            multiplier = 5
        else:
            multiplier = 1
        ultimate_attack = attack_power*multiplier*self.skill
#The program prints how much you ended up depleting. 
        print("You attack with " + str(ultimate_attack) + " power.")
        return ultimate_attack
    
    def boss_attack(self):
        attack_power = 10 * self.skill
        target = 10
        print("\nDistance: " + str(target) + " metres.")
        time.sleep(2)
        print("...")
        initial = time.time()
        input()
        final = time.time()
        distance_accuracy = final - initial
        if distance_accuracy > target+1 or distance_accuracy < target-1:
            multiplier = 2
        elif distance_accuracy > target+0.5 or distance_accuracy <target-0.5:
            multiplier = 3
        elif distance_accuracy > target+0.2 or distance_accuracy <target-0.2:
            multiplier = 5
        else:
            multiplier = 1
        ultimate_attack = attack_power*multiplier*self.skill
        return ultimate_attack

#Basic, low-effort attack type if the player doesn't want to put in any effort. 
    def swipe_attack(self):
        ultimate_attack = 3*self.skill
        return ultimate_attack
    
#Defense method, prints how much damage you're hit with.
    def defend(self, ultimate_attack):
        damage = ultimate_attack - self.shield
        if damage >  0:
            self.__health -= damage
            print("\nYou're hit with " + str(damage) + " damage")
        else:
            print('No damage dealt to you.')

#Coffee function has the chance to completely heal the user before the next round starts. Probability low though.
    def coffee(self):
        x = random.randint(1,17)
        y = random.randint(1,17)
#Essentially two random numbers are selected and if they match then the user gets the boost. 
        if x == y:
            print("\nA crinkle emits from under your foot. You jolt up in fear, only to realise you've been blessed with a packet of instant coffee. Your health is fully restored.")
            self.__health = 100

    def restore_health(self):
        self.__health = 100
        
    
class Enemy():
#Defining the attributes for the enemy which are similar to the Player attributes
    def __init__(self, type, skill=2, shield=10, voice="", name="", starting_health=100):
        self.type = type
        self.skill = skill
        self.shield = shield
        self.__health = starting_health
        self.name = name
#Separate kinds of enemies have their own unique names and voicelines which are assigned as following:
        if type == "Poltergeist":
            self.name = "Poltergeist"
            self.voice = "You don't see it. Rather, you hear a low frequency, outlining a thin presence."
        elif type == "Silhouette":
            self.name = "Silhouette"
            self.voice = "A dark patch inches closer, barely discernable from the dim surroundings."
        elif type == "Boss":
            self.name = "... wait...that looks like....you?"
            self.voice = "A spitting image. \nBut it feels...idle...unreal... \nThreatening energy emits from it."
        else: self.voice = voice

#The enemy class also has a method to load the status of their attributes.
    def load_stats(self):
        print("\nEnemy status:\n" + "Health: " + str(round(self.__health, 2)) + "\n" + "Skill: " + str(self.skill) + "\n" + "Shield: " + str(self.shield))

#The enemy has only one basic attack mechanism where the skill is multiplied by a random integer.
    def attack(self):
        attack_power = self.skill*random.randint(3,6)
        return attack_power
    
#Once again a method to check the health status of the enemy.
    def is_dead(self):
        if self.__health <=0:
            return True
        else:
            return False
        
    def revive(self):
        self.__health = 100
    
#Antoher defence method for the enemy.
    def defend(self, ultimate_attack):
        damage = ultimate_attack - self.shield
        if damage >  0:
            self.__health -= damage
#The printed damage to the user is rounded because otherwise it's too distracting
            print("The enemy takes " + str(damage) + " damage.")
        else:
            print("The enemy takes " + str(damage) + " damage.")
    
    def announce(self):
        print(self.voice)

#Bank of enemies that can be selected from.
enemies = ["Poltergeist", "Silhouette", "Apparition"]

#Main game function where the user first has a chance to revive all their health, then the user faces an enemy, chooses what skill type to use for the battle and fights the enemy. This happens 5 times and is randomly selected.
def game_loop():
    counter = 0
    while counter != 5:
        progress = input("Enter 'e' to continue.\n")
        if progress:
            #Before any battles occur the coffee method is called and the enemy is randomly selected.
            user.coffee()
            print("\nSomething approaches you...")
            roulette = random.choice(enemies)
            if roulette == "Apparition":
                decider = random.randint(1,2)
                if decider == 1:
                    enemy = user.priv_enemy1
                elif decider == 2:
                    enemy = user.priv_enemy2
            else:
                enemy = Enemy(roulette)
            #The selected enemy is conveniently announced.
            enemy.announce()
            if enemy.type == "Apparition":
                print("An apparition of " + enemy.name.lower() +"...\n")
            else:
                print("A " + enemy.name.lower() + "...\n")
            decision = input("What skill would you like to use this round? (launch or swipe) ")
            #Sequence of events for the launch attack
            if decision == "launch":
                while enemy:
                    enemy.defend(user.launch_attack())
                    enemy.load_stats()
                    time.sleep(2)
                    if enemy.is_dead():
                        print("\nYou successfully make it past the enemy...")
                        enemy.revive()
                        break
                    user.defend(enemy.attack())
                    user.load_stats()
                    time.sleep(2)
                    if user.is_dead():
                        print('\nThe enemy wins.\nYou lose 0.15 skill.')
                        user.skill = user.skill-0.15
                        user.restore_health()
#We need the enemy to reset at the end because otherwise if it re-appears it'll still have its depleted health.
                        enemy.revive
                        break
                print('')
            #Sequence of events upon selecting the swipe attack.
            elif decision == "swipe":
                while enemy:
                    enemy.defend(user.swipe_attack())
                    enemy.load_stats()
                    time.sleep(2)
                    print('')
                    if enemy.is_dead():
                        print('\nYou succesfully make it past the enemy')
                        enemy.revive()
                        break
                    user.defend(enemy.attack())
                    user.load_stats()
                    time.sleep(2)
                    if user.is_dead():
                        print('\nThe enemy wins.\nYou lose 0.15 skill.')
                    #Depletion of user skill if loss occurs rather than triggering permadeath.
                        user.skill = user.skill-0.15
                        user.restore_health()
                        enemy.revive()
                        break
                    print('')
            else: 
                print("Not a skill. Try again.\n")
                counter = counter - 1
        counter = counter + 1

#The completion of a round adds to the user's skill whereas a failure depletes the user's skill. This ultimately determines their strength when it comes to the boss fight.
        user.skill = user.skill + 0.2

#This is the final boss battle component whereby the boss is announced, and then the user battles it. The core idea is that the boss is essentially a reflection of the player themselves. The player has to face themselves to win the game.
    boss = Enemy("Boss", user.skill, user.shield)
    boss.announce()
    print("Are you ready for the final test?\n")
    progress = input("Enter 'e' to continue: ")
    while boss.is_dead() == False:
        enemy.defend(user.boss_attack())
        enemy.load_stats()
        time.sleep(2)
        print('')
        if enemy.is_dead():
            print('\nYou successfully make it past the reflection...\n')
            winner = "user"
            break
        user.defend(enemy.attack())
        user.load_stats()
        time.sleep(2)
        if user.is_dead():
            print(enemy.name,'wins\n')
            winner = "boss"
            break
        print('')

#Final conclusion to the game, reflecting on self development, depends on whethet you win or not.
    if winner == "boss":
        print("You are rapidly consumed by your own sharp thoughts and regrets, arm outstretched in front of you, a last attempt to help yourself.\n")
        time.sleep(1)
        print("Why didn't you try help yourself before?\n")
        time.sleep(1)
        print("Why does the light of day have to dim in your eyes to make you realise?\n")
        time.sleep(1)
        print("The light fades... \n")
        time.sleep(1)
        print()
        print("---")
    elif winner == "user":
        print("The figure crumbles to the ground, its menacing light sorrowfully dimming.\n")
        time.sleep(2)
        print("You stand victorious.\n")
        time.sleep(2)
        print("In the corner of your eye, you see a door lightly cracked open, a light eminating from it.\n")
        time.sleep(2)
        print("An escape. An exit. \n")
        time.sleep(2) 
        print("You feel at peace. A wash of hope embraces you, as you cautiously proceed, leaving the house and thus leaving your worries.\n")
        print("---")
     

#This block is essentially most of the story and sets the scene whilst initiating the core components as necessary.

print("\nThere's something about this house… it appears the same as the rest of the neighbourhood, but it feels… strange.")
time.sleep(4)
print("A soup of fear and curiosity leads you nearer.")
time.sleep(3)
print("Overgrown grass.")
time.sleep(2)
print("Worn paint.")
time.sleep(2)
print("This place is… completely abandoned.")
time.sleep(3)
print("Right before you reach the doorstep, you notice your reflection in the only unboarded window. You see…")
time.sleep(4)
print("")
print("1. Your tired, sullen eyes.")
time.sleep(3)
print("2. The fresh set of veneers peeking out from your half-agape mouth.")
time.sleep(4)
print("3. The almost-healed scar stretching across your face.")
time.sleep(3)
print("4. A glimmer from your silver-frame aviator glasses.")
time.sleep(2)

#This component of the block is where the user selects the character. The characters vary by their story.

choice = input("\nWhich one? (Enter the number)\n")
user = Player(choice)
print(user.intro)
time.sleep(7)
print("You hastily look away.")
time.sleep(2)
print("Pushing the clunky door open makes it weep as it swings out.")
time.sleep(2)
print("Your nostrils are hit with a sorrowful waft of dampness, and age.")
time.sleep(3)
print("The world is… silent.")
time.sleep(4)
print("Maybe if you make it through this house… you'll truly find peace.")
time.sleep(3)
print("They… await you")
time.sleep(2)
print("They await your instinct")
time.sleep(2)
print("Do you still have your dignity?")
time.sleep(2)
print("Enough dignity to make it through?")
time.sleep(2)
print("\nTraverse through this place. \nThe enemy travels a metre each second after the ellipses appear. \nWhen you feel the enemy is close enough, hit enter to attack. \nYour intuition is your best friend.")
time.sleep(4)
game_loop()
