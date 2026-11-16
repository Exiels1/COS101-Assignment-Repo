
# Force which is Mass * Acceleration
def calculate_force(mass, acceleration):
    return mass * acceleration

# Weight which is Mass * Gravity
def calculate_weight(mass, gravity):
    return mass * gravity

# Velocity is Distance / Time
def calculate_velocity(distance, time):
    return distance / time

# Kinetic Energy
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

# Ohms Law Current * Resistance
def calculate_ohms_law(current, resistance):
    return current * resistance


def main():
    while True:
        print("\nPick the Formula to use")
        print("1. Force")
        print("2. Weight")
        print("3. Velocity")
        print("4. Kinetic Energy")
        print("5. Ohm Law")

        choice = input("Which Formula do you want to use: ")

        if choice == "1":
            mass = float(input("Enter the mass: "))
            acceleration = float(input("Enter the acceleration: "))
            force = calculate_force(mass, acceleration)
            print("The Force is: " + str(force))

        elif choice == "2":
            mass = float(input("Enter the mass: "))
            gravity = float(input("Enter the gravity: "))
            weight = calculate_weight(mass, gravity)
            print("The Weight is: " + str(weight))

        elif choice == "3":
            distance = float(input("Enter the distance: "))
            time = float(input("Enter the time: "))
            velocity = calculate_velocity(distance, time)
            print("The Velocity is: " + str(velocity))

        elif choice == "4":
            mass = float(input("Enter the mass: "))
            velocity = float(input("Enter the velocity: "))
            kinetic_energy = calculate_kinetic_energy(mass, velocity)
            print("The Kinetic Energy is: " + str(kinetic_energy))

        elif choice == "5":
            current = float(input("Enter the current: "))
            resistance = float(input("Enter the resistance: "))
            ohms_law = calculate_ohms_law(current, resistance)
            print("The Ohm's Law is: " + str(ohms_law))

        else:
            print("No Option was selected")

        again = input("\nDo you want to use the calculator again? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using the Physics Calculator!")
            break


main()
