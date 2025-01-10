# Eva Deng
# 10/15/24

# init
print("Welcome to the Greek Mythology Name Generator")

def generate_name():
    # Step 1: Choose an Element (Fire or Water)
    print("Step 1: Choose an Element")
    element = input("Choose Fire or Water: ").lower()

    if element == "fire":
        # Step 2: Fire - Choose Flame or Ember
        print("\nStep 2: Since you chose Fire, choose between Flame or Ember")
        fire_choice = input("Choose Flame or Ember: ").lower()

        if fire_choice == "flame":
            # Step 3: Final choices for Flame
            print("\nStep 3: Choose one of the following:")
            print("1. God of Underworld\n2. God of Forge and Fire")
            final_choice = input("Enter the number for your choice: ")
            if final_choice == "1":
                name = "Hephaestus, God of Underworld"
            elif final_choice == "2":
                name = "Prometheus, God of Forge and Fire"

        elif fire_choice == "ember":
            # Step 3: Final choices for Ember
            print("\nStep 3: Choose one of the following:")
            print("1. Goddess of the Hearth\n2. Fiery Steed of the Sun")
            final_choice = input("Enter the number for your choice: ")
            if final_choice == "1":
                name = "Hestia, Goddess of the Hearth"
            elif final_choice == "2":
                name = "Aetna, Fiery Steed of the Sun"

    elif element == "water":
        # Step 2: Water - Choose River or Ocean
        print("\nStep 2: Since you chose Water, choose between River or Ocean")
        water_choice = input("Choose River or Ocean: ").lower()

        if water_choice == "river":
            # Step 3: Final choices for River
            print("\nStep 3: Choose one of the following:")
            print("1. River God of Arcadia\n2. God of the Sea")
            final_choice = input("Enter the number for your choice: ")
            if final_choice == "1":
                name = "Alpheus, River God of Arcadia"
            elif final_choice == "2":
                name = "Achelous, God of the Sea"

        elif water_choice == "ocean":
            # Step 3: Final choices for Ocean
            print("\nStep 3: Choose one of the following:")
            print("1. Guardian of the Ocean\n2. Wizard of Turmoil")
            final_choice = input("Enter the number for your choice: ")
            if final_choice == "1":
                name = "Oceanus, Guardian of the Ocean"
            elif final_choice == "2":
                name = "Nereus, Wizard of Turmoil"

    print("\nYour Greek Mythology-inspired name is: " + name)

# Run the name generator
generate_name()
