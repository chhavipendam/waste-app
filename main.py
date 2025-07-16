
from db import init_db
from user import register, login, log_waste
from admin import view_all_users, waste_summary
from utils import get_float_input

def user_menu(user_id):
    while True:
        print("\n👤 User Menu")
        print("1. Log Waste")
        print("2. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            o = get_float_input("Organic (kg): ")
            p = get_float_input("Plastic (kg): ")
            e = get_float_input("E-waste (kg): ")
            g = get_float_input("Glass (kg): ")
            log_waste(user_id, o, p, e, g)
        elif choice == '2':
            break
        else:
            print("❌ Invalid choice.")

def admin_menu():
    while True:
        print("\n🛠️ Admin Menu")
        print("1. View All Users")
        print("2. View Waste Summary")
        print("3. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            view_all_users()
        elif choice == '2':
            waste_summary()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice.")

def main():
    init_db()
    while True:
        print("\n♻️ Waste Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            register(username, password)

        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            user = login(username, password)
            if user:
                uid, is_admin = user
                print("✅ Login successful!")
                if is_admin:
                    admin_menu()
                else:
                    user_menu(uid)
            else:
                print("❌ Incorrect username or password.")

        elif choice == '3':
            print("👋 Exiting the system.")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
