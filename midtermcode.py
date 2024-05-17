## STORES GAME ##
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
}

## STORE USER ACC ##
user_accounts = {}

## ADMIN ##
admin_username = "admin"
admin_password = "adminpass"

## DISPALY GAME ##
def display_available_games():
    print("Available Games:")
    for game, details in game_library.items():
        print(f"{game}: Quantity - {details['quantity']}, Rental Cost - ${details['cost']}")

# REGISTER USER ##
def register_user():
    username = input("Input username: ")
    if username in user_accounts:
        print("Username already exists! Enter another username.")
        return
    password = input("Input password: ")
    balance = float(input("Top up your account with an initial balance: "))
    user_accounts[username] = {"password": password, "balance": balance, "points": 0, "inventory": []}
    print("Welcome to Nicole's Game Rental!")

## RENT GAME ##
def rent_game(username):
    game = input("Enter the name of the game you want to rent: ")
    if game not in game_library:
        print("Game not available.")
        return
    if game_library[game]["quantity"] <= 0:
        print("Game is out of stock.")
        return
    if user_accounts[username]["balance"] < game_library[game]["cost"]:
        print("Insufficient balance!")
        return

    user_accounts[username]["balance"] -= game_library[game]["cost"]
    user_accounts[username]["points"] += int(game_library[game]["cost"] / 2)
    game_library[game]["quantity"] -= 1
    user_accounts[username]["inventory"].append(game)
    print(f"Game '{game}' rented successfully!")

## RETURN GAME ##
def return_game(username):
    game = input("Enter the name of the game you want to return: ")
    if game not in game_library:
        print("Game not found!")
        return
    if game not in user_accounts[username]["inventory"]:
        print("You don't have this game in your inventory!")
        return

    user_accounts[username]["points"] += 1
    game_library[game]["quantity"] += 1
    user_accounts[username]["inventory"].remove(game)
    print(f"Game '{game}' returned successfully!")

## TOP-UP ##
def top_up_account(username, amount):
    user_accounts[username]["balance"] += amount
    print(f"Account topped up successfully! New balance: ${user_accounts[username]['balance']}")

## USER INVENTORY ##
def display_inventory(username):
    print(f"Inventory for user '{username}':")
    for game in user_accounts[username]["inventory"]:
        print(game)

# ADMIN UPDATE GAME DETAILS ##
def admin_update_game():
    game = input("Enter game name: ")
    if game not in game_library:
        print("Game not found!")
        return
    quantity = int(input("Enter new quantity: "))
    cost = float(input("Enter new rental cost: "))
    game_library[game]["quantity"] = quantity
    game_library[game]["cost"] = cost
    print(f"Game '{game}' details updated successfully!")

# Function for admin login
def admin_login(username, password):
    if username == admin_username and password == admin_password:
        return True
    else:
        return False

## ADMIN MENU ##
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Update Game Details")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if admin_login():
                admin_update_game()
        elif choice == "2":
            break
        else:
            print("Invalid choice!")

## REDEEM POINTS ##
def redeem_free_rental(username):
    if user_accounts[username]["points"] < 3:
        print("Not enough points to redeem a free rental.")
        return
    game = input("Enter the name of the game you want to redeem: ")
    if game not in game_library or game_library[game]["quantity"] <= 0:
        print("Game not available or out of stock.")
        return

    user_accounts[username]["points"] -= 3
    game_library[game]["quantity"] -= 1
    user_accounts[username]["inventory"].append(game)
    print(f"Game '{game}' redeemed successfully!")

## GAME INVENTORY ##
def display_game_inventory():
    print("Game Inventory:")
    for game, details in game_library.items():
        print(f"{game}: Quantity - {details['quantity']}")

## USER LOG-IN ##
def logged_in_menu(username):
    while True:
        print("\nRENTAL GAME MENU:")
        print("1. Display Available Games")
        print("2. Rent a Game")
        print("3. Return a Game")
        print("4. Top-Up Account")
        print("5. Display Inventory")
        print("6. Redeem Points for Free Rental")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_available_games()
        elif choice == "2":
            rent_game(username)
        elif choice == "3":
            return_game(username)
        elif choice == "4":
            amount = float(input("Enter the amount to top-up: "))
            top_up_account(username, amount)
        elif choice == "5":
            display_inventory(username)
        elif choice == "6":
            redeem_free_rental(username)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

## CREDENTIALS ##
def check_credentials(username, password):
    if username in user_accounts and user_accounts[username]["password"] == password:
        return True
    else:
        return False

## MAIN FUNCTION ##
def main():
    while True:
        print("\nWelcome to Nicole's Game Rental:")
        print("1. Login")
        print("2. Register")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if check_credentials(username, password):
                print("Login successful!")
                logged_in_menu(username)
            else:
                print("Invalid username or password!")
        elif choice == "2":
            register_user()
        elif choice == "3":
            if admin_login():
                admin_menu()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
