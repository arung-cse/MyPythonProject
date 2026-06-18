import random

print("=== MMORPG Character Simulator ===")

name = input("Enter Character Name: ")

level = 1

print("\nChoose Your Job")
print("1. Warrior")
print("2. Mage")
print("3. Archer")

choice = input("Enter Choice: ")

if choice == "1":
    job = "Warrior"
    hp = 150
    attack = 20

elif choice == "2":
    job = "Mage"
    hp = 80
    attack = 30

elif choice == "3":
    job = "Archer"
    hp = 100
    attack = 25

else:
    job = "Novice"
    hp = 100
    attack = 10

monster_name = "Goblin"
monster_hp = 50

print("\nA Wild", monster_name, "Appeared!")

while hp > 0 and monster_hp > 0:

    print("\nYour HP:", hp)
    print(monster_name, "HP:", monster_hp)

    print("\n1. Attack")
    print("2. Run")

    action = input("Choose: ")

    if action == "1":

        damage = random.randint(attack - 5, attack + 5)

        monster_hp -= damage

        print("You dealt", damage, "damage!")

        if monster_hp <= 0:
            print("\nYou defeated the", monster_name)
            break

        monster_damage = random.randint(5, 15)

        hp -= monster_damage

        print(monster_name, "dealt", monster_damage, "damage!")

    elif action == "2":
        print("You escaped!")
        break

if hp <= 0:
    print("\nYou were defeated...")