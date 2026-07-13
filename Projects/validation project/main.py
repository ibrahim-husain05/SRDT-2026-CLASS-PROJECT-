from auth import Auth
from user import User
from admin import Admin

auth = Auth()
user = User()
admin = Admin()

while True:

    print("\n" + "=" * 50)
    print("        LOGIN & REGISTRATION SYSTEM")
    print("=" * 50)
    print("1. Register")
    print("2. User Login")
    print("3. Forgot Password")
    print("4. Admin Login")
    print("5. Exit")
    print("=" * 50)

    choice = input("Enter Your Choice : ")

    if choice == "1":
        auth.register()

    elif choice == "2":

        username = auth.login()

        if username:

            while True:

                print("\n" + "=" * 50)
                print("            USER DASHBOARD")
                print("=" * 50)
                print("1. View Profile")
                print("2. Update Profile")
                print("3. Change Password")
                print("4. Delete Account")
                print("5. Logout")
                print("=" * 50)

                option = input("Enter Your Choice : ")

                if option == "1":
                    user.view_profile(username)

                elif option == "2":
                    user.update_profile(username)

                elif option == "3":
                    auth.change_password(username)

                elif option == "4":

                    result = user.delete_account(username)

                    if result:
                        break

                elif option == "5":
                    print("Logout Successfully")
                    break

                else:
                    print("Invalid Choice")

    elif choice == "3":
        auth.forgot_password()

    elif choice == "4":
        admin.login()

    elif choice == "5":
        print("\nThank You For Using Login System")
        break

    else:
        print("Invalid Choice")