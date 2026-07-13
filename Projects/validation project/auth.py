from database import Database
from validation import Validation


class Auth:

    def __init__(self):
        self.db = Database()
        self.validation = Validation()

    def register(self):

        name = input("Enter Name : ")
        email = input("Enter Email : ")
        mobile = input("Enter Mobile : ")
        username = input("Enter Username : ")
        password = input("Enter Password : ")
        confirm = input("Confirm Password : ")
        question = input("Enter Security Question : ")
        answer = input("Enter Security Answer : ")

        if not self.validation.is_empty(name):
            print("Name cannot be empty")
            return

        if not self.validation.validate_name(name):
            print("Invalid Name")
            return

        if not self.validation.validate_email(email):
            print("Invalid Email")
            return

        if not self.validation.validate_mobile(mobile):
            print("Invalid Mobile Number")
            return

        if not self.validation.validate_username(username):
            print("Invalid Username")
            return

        if not self.validation.validate_password(password):
            print("Weak Password")
            return

        if not self.validation.confirm_password(password, confirm):
            print("Password does not match")
            return

        query = "SELECT * FROM users WHERE username=%s"
        self.db.execute(query, (username,))
        if self.db.fetchone():
            print("Username already exists")
            return

        query = "SELECT * FROM users WHERE email=%s"
        self.db.execute(query, (email,))
        if self.db.fetchone():
            print("Email already exists")
            return

        query = "SELECT * FROM users WHERE mobile=%s"
        self.db.execute(query, (mobile,))
        if self.db.fetchone():
            print("Mobile already exists")
            return

        query = """
        INSERT INTO users
        (name,email,mobile,username,password,security_question,security_answer)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            name,
            email,
            mobile,
            username,
            password,
            question,
            answer
        )

        self.db.execute(query, values)

        print("Registration Successful")

    def login(self):

        username = input("Enter Username : ")
        password = input("Enter Password : ")

        query = "SELECT * FROM users WHERE username=%s AND password=%s"

        self.db.execute(query, (username, password))

        user = self.db.fetchone()

        if user:
            print("Login Successful")
            return username

        print("Invalid Username or Password")
        return None

    def forgot_password(self):

        username = input("Enter Username : ")

        query = """
        SELECT security_question, security_answer
        FROM users
        WHERE username=%s
        """

        self.db.execute(query, (username,))

        user = self.db.fetchone()

        if not user:
            print("Username Not Found")
            return

        print("Security Question :", user[0])

        answer = input("Enter Security Answer : ")

        if answer != user[1]:
            print("Wrong Security Answer")
            return

        new_password = input("Enter New Password : ")
        confirm = input("Confirm New Password : ")

        if not self.validation.validate_password(new_password):
            print("Weak Password")
            return

        if not self.validation.confirm_password(new_password, confirm):
            print("Password Does Not Match")
            return

        query = "UPDATE users SET password=%s WHERE username=%s"

        self.db.execute(query, (new_password, username))

        print("Password Reset Successfully")

    def change_password(self, username):

        old_password = input("Enter Old Password : ")

        query = "SELECT password FROM users WHERE username=%s"

        self.db.execute(query, (username,))

        user = self.db.fetchone()

        if not user:
            print("User Not Found")
            return

        if old_password != user[0]:
            print("Old Password Incorrect")
            return

        new_password = input("Enter New Password : ")
        confirm = input("Confirm New Password : ")

        if not self.validation.validate_password(new_password):
            print("Weak Password")
            return

        if not self.validation.confirm_password(new_password, confirm):
            print("Password Does Not Match")
            return

        query = "UPDATE users SET password=%s WHERE username=%s"

        self.db.execute(query, (new_password, username))

        print("Password Changed Successfully")

    def logout(self):
        print("Logout Successful")