import random

# =========================
# CHARACTER CREATION
# =========================

print("================================")
print(" MMORPG CHARACTER SIMULATOR ")
print("================================")

name = input("Enter Character Name: ")

print("\nChoose Your Job")
print("1. Warrior")
print("2. Mage")
print("3. Archer")

choice = input("Choice: ")

if choice == "1":
    job = "Warrior"
    max_hp = 150
    attack = 20

elif choice == "2":
    job = "Mage"
    max_hp = 80
    attack = 30

elif choice == "3":
    job = "Archer"
    max_hp = 100
    attack = 25

else:
    job = "Novice"
    max_hp = 100
    attack = 10

hp = max_hp
level = 1
exp = 0
gold = 0

inventory = {
    "Health Potion": 3
}

# =========================
# MONSTERS
# =========================

monsters = [
    {"name":"Goblin","hp":50,"attack":10,"exp":50,"gold":20},
    {"name":"Wolf","hp":70,"attack":12,"exp":75,"gold":30},
    {"name":"Skeleton","hp":100,"attack":15,"exp":100,"gold":50},
    {"name":"Orc","hp":150,"attack":20,"exp":150,"gold":80},
    {"name":"Dragon","hp":300,"attack":35,"exp":300,"gold":200}
]

# =========================
# GAME LOOP
# =========================

while True:

    print("\n================================")
    print("Name :", name)
    print("Job  :", job)
    print("Level:", level)
    print("HP   :", hp, "/", max_hp)
    print("EXP  :", exp)
    print("Gold :", gold)
    print("================================")

    print("\n1. Hunt Monster")
    print("2. Inventory")
    print("3. Rest")
    print("4. Exit")

    menu = input("\nChoose: ")

    # =====================
    # HUNT
    # =====================

    if menu == "1":

        monster = random.choice(monsters)

        monster_name = monster["name"]
        monster_hp = monster["hp"]

        print("\nA Wild", monster_name, "Appeared!")

        while monster_hp > 0 and hp > 0:

            print("\n--------------------")
            print(monster_name, "HP:", monster_hp)
            print("Your HP:", hp)
            print("--------------------")

            print("1. Attack")
            print("2. Use Potion")
            print("3. Run")

            action = input("Choose: ")

            if action == "1":

                damage = random.randint(
                    attack-5,
                    attack+5
                )

                monster_hp -= damage

                print(
                    "You dealt",
                    damage,
                    "damage!"
                )

                if monster_hp <= 0:

                    print(
                        "\nYou defeated",
                        monster_name
                    )

                    exp += monster["exp"]
                    gold += monster["gold"]

                    print(
                        "+",
                        monster["exp"],
                        "EXP"
                    )

                    print(
                        "+",
                        monster["gold"],
                        "Gold"
                    )

                    if random.randint(1,100) <= 30:

                        inventory[
                            "Health Potion"
                        ] = inventory.get(
                            "Health Potion",
                            0
                        ) + 1

                        print(
                            "Monster dropped a Health Potion!"
                        )

                    while exp >= 100:

                        exp -= 100

                        level += 1

                        max_hp += 20

                        attack += 5

                        hp = max_hp

                        print(
                            "\n***** LEVEL UP *****"
                        )

                        print(
                            "Level:",
                            level
                        )

                    break

                monster_damage = random.randint(
                    monster["attack"]-3,
                    monster["attack"]+3
                )

                hp -= monster_damage

                print(
                    monster_name,
                    "dealt",
                    monster_damage,
                    "damage!"
                )

            elif action == "2":

                if inventory.get(
                    "Health Potion",
                    0
                ) > 0:

                    inventory[
                        "Health Potion"
                    ] -= 1

                    heal = 50

                    hp += heal

                    if hp > max_hp:
                        hp = max_hp

                    print(
                        "Recovered",
                        heal,
                        "HP!"
                    )

                else:
                    print(
                        "No Potions!"
                    )

            elif action == "3":

                print(
                    "You escaped!"
                )

                break

        if hp <= 0:

            print("\nYOU DIED!")

            hp = max_hp

            print(
                "Respawned in town!"
            )

    # =====================
    # INVENTORY
    # =====================

    elif menu == "2":

        print("\n===== INVENTORY =====")

        for item, qty in inventory.items():

            print(
                item,
                "x",
                qty
            )

    # =====================
    # REST
    # =====================

    elif menu == "3":

        hp = max_hp

        print(
            "\nFully Healed!"
        )

    # =====================
    # EXIT
    # =====================

    elif menu == "4":

        print(
            "\nThanks For Playing!"
        )

        break