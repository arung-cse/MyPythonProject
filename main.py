print("=== MMORPG Character Simulator ===")

name = input("Enter Character Name: ")

level = 1
hp = 100

print("\nChoose Your Job")
print("1. Warrior")
print("2. Mage")
print("3. Archer")

choice = input("Enter Choice: ")

if choice == "1":
    job = "Warrior"
    hp = 150

elif choice == "2":
    job = "Mage"
    hp = 80

elif choice == "3":
    job = "Archer"
    hp = 100

else:
    job = "Novice"

print("\n=== Character Created ===")
print("Name :", name)
print("Job  :", job)
print("Level:", level)
print("HP   :", hp)