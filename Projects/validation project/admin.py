from database import Database


class Admin:
    
    def _init_(self):
        self.db = Database()
        
    def login(self):
        username = input("Enter Admin Username : ")
        password = input("Enter Admin Password : ")
        
        query = "SELECT * FROM admin WHERE username=%s AND password=%s"
        
        self.db.execute(query, (username, password))
        
        admin = self.db.fetchone()
        
        if admin:
            print("Admin Login Successful")
            self.dashboard()
        else:
            print("Invalid Admin Credentials")
    def view_all_users(self):
        query = """
        SELECT id,name,email,mobile,username,created_at
        FROM users
        """
        
        self.db.execute(query)
        
        users = self.db.fetchall()
        
        if not users:
            print("No Users Found")
            return
            
        print("\n==================== USERS ====================")
        
        for user in users:
            
            print(f"""
            ID       : {user[0]}
            Name     : {user[1]}
            Email       : {user[2]}
            Mobile      : {user[3]}
            Username    : {user[4]}
            Created At  : {user[5]}
            ==============================
            """)
    
    
    def search_user(self):
        username = input("Enter Username : ")
        
        query = """
        SELECT id,name,email,mobile,username,created_at
        FROM users
        WHERE username=%s
        """
        
        self.db.execute(query, (username,))
        
        user = self.db.fetchone()
        
        if user:
            print(f"""
            ID         : {user[0]}
            Name       : {user[1]}
            Email      : {user[2]}
            Mobile     : {user[3]}
            Username   : {user[4]}
            Created At : {user[5]}
            """)
        else:
            print("User not found")  
          
    def delete_user(self):
        # 1. Get input safely
        username = input("Enter Username: ")
        
        # 2. Use a safe parameterized query (Example using '?' for SQLite)
        # Note: If using MySQL/PostgreSQL, keep %s but do NOT format it manually
        query = "SELECT * FROM users WHERE username =%s"
        self.db.execute(query, (username,))
        
        user = self.db.fetchone()
        
        if not user:
            print("User Not Found")
            return
            
        choice = input("Delete User (Y/N): ")
        
        if choice.lower() == 'y':
            # 3. Parameterize the delete query as well
            delete_query = "DELETE FROM users WHERE username = ?"
            self.db.execute(delete_query, (username,))
            print("User Deleted Successfully") 
        else:
            print("Cancelled")      
    
    
    def total_user(self):
      query="SELECT COUNT(*) FROM users"
      self.db.execute(query)
      total= self.db.fetchone()
      print("Total users:", total[0])
      
      
      
      
    def dashboard(self):
        
        while True:
            
            print("\n========== ADMIN DASHBOARD ==========")
            print("1. View All Users")
            print("2. Search User")
            print("3. Delete User")
            print("4. Total Users")
            print("5. Logout")
            
            choice = input("Enter Choice : ")
            
            if choice == "1":
                self.view_all_users()
                
            elif choice == "2":
                self.search_user()
                
            elif choice == "3":
                self.delete_user()
                
            elif choice == "4": 
                 self.total_user()
            elif choice == "5":
                 print("Logout successfull")
            else:
                 print("Invalid choice")
                 