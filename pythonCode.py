hello = "Hello"

text = input("Type some code: ")
print(text)

age = 41

money = 10.10

isGameOver = True

name = "Raul"
game = 'Survivng Mars'

inventory = ["Axe", "Food", "Sword", "Helmet"]

food = inventory[1]
inventory[1] = "Fruit"

print(inventory[0:2])
inventory.append("Dagger")
inventory.remove("Sword")
inventory.insert(1,"Boots")
print(inventory)

# Tupals
profile = ("Raul", 41)
# profile[0] = "Sam" is not allowed
name = profile[0]

#Ranges
my_range = range(5)
print(my_range)

#Dictionaries
#List is ordered, dictionary is just there
inventory = {"Axe":1, "Fruit":3, "Helmet":1, "Dagger":2}

num_axes = inventory["Axe"]
print(num_axes)
inventory["Axe"] = 2
print(inventory)
inventory["Boots"] = 2 #Adds a new item to the dictionary
print(inventory)
print(inventory.items())

pos = 5
key = "r"

if key == "r":
    pos += 1
    print("Player moved right")
elif key == "l":
    pos -= 1
    print("Player moved left")
else:
    print("Unknown command")

posi = 0
end_posi = 5

while posi < end_posi:
    posi += 1
    print(posi)

inventory = ["Axe", "Food", "Sword", "Helmet"]

for item in inventory:
    print(item)

for i in range(5):
    print(i)

def move(posit, by_amount):
    new_pos = posit + by_amount
    return new_pos

final_pos = move(0, 5)
print(final_pos)

class GameCharacter:

    def __init__(self, name, pos, health):
        self.name = name
        self.pos = pos
        self.health = health

    def move(self, by_amount):
        self.pos += by_amount

character = GameCharacter("Owl", 5, 100)
print(character.name)
character.health = 120
print(character.health)

character.move(10)
print(character.pos)