from database import Database
from validation import Validation


class User:

    def __init__(self):
        self.db = Database()
        self.validation = Validation()

    def view_profile(self, username):

        query = "SELECT id,name,email,mobile,username,created_at FROM users WHERE username=%s"

        self.db.execute(query, (username,))

        user = self.db.fetchone()

        if user:

            print("\n========== PROFILE ==========")
            print("ID :", user[0])
            print("Name :", user[1])
            print("Email :", user[2])
            print("Mobile :", user[3])
            print("Username :", user[4])
            print("Created At :", user[5])
            print("=============================\n")

        else:
            print("User Not Found")

    def update_profile(self, username):

        name = input("Enter New Name : ")
        email = input("Enter New Email : ")
        mobile = input("Enter New Mobile : ")

        if not self.validation.validate_name(name):
            print("Invalid Name")
            return

        if not self.validation.validate_email(email):
            print("Invalid Email")
            return

        if not self.validation.validate_mobile(mobile):
            print("Invalid Mobile")
            return

        query = """
        UPDATE users
        SET name=%s,email=%s,mobile=%s
        WHERE username=%s
        """

        self.db.execute(query, (name, email, mobile, username))

        print("Profile Updated Successfully")

    def delete_account(self, username):

        password = input("Enter Password : ")

        query = "SELECT password FROM users WHERE username=%s"

        self.db.execute(query, (username,))

        user = self.db.fetchone()

        if not user:
            print("User Not Found")
            return

        if password != user[0]:
            print("Incorrect Password")
            return

        choice = input("Are you sure (Y/N) : ")

        if choice.lower() == "y":

            query = "DELETE FROM users WHERE username=%s"

            self.db.execute(query, (username,))

            print("Account Deleted Successfully")

            return True

        print("Account Deletion Cancelled")

        return False

    def dashboard(self, username):

        while True:

            print("\n========== USER DASHBOARD ==========")
            print("1. View Profile")
            print("2. Update Profile")
            print("3. Delete Account")
            print("4. Logout")

            choice = input("Enter Choice : ")

            if choice == "1":
                self.view_profile(username)

            elif choice == "2":
                self.update_profile(username)

            elif choice == "3":

                deleted = self.delete_account(username)

                if deleted:
                    break

            elif choice == "4":
                print("Logout Successfully")
                break

            else:
                print("Invalid Choice")