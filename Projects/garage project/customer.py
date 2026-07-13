from database import Database
class Customer:
    def __init__(self):
        self.db = Database()
        self.con = self.db.connect()
        self.cursor = self.con.cursor()

    def add_customer(self):
        name =input("enter customer name : ")
        mobile = input("enter customer phone : ")

        sql = "INSERT INTO customers(customer_name,mobile) VALUES(%s,%s)"
        value = (name, mobile)

        self.cursor.execute(sql,value)
        self.con.commit()
        print("customer added successfully.")

    def view_customers(self):
        sql ="SELECT * FROM customers"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print("\n------customer list-------")
        for row in data:
            print(row)

    def add_vehicle(self):
        customer_id = int(input("enter customer id : "))
        vehicle_no= input("enter vehicle number : ")
        vehicle_name = input("enter vehicle name : ")

        sql ="""
        INSERT INTO vehicles (customer_id,vehicle_no,vehicle_name)
        VALUES(%s,%s,%s)
        """
        value = (customer_id,vehicle_no,vehicle_name)

        self.cursor.execute(sql,value)
        self.con.commit()

        print("vehicle added successfully.")

    def view_vehicles(self):
        sql = """
        SELECT 
        vehicles.vehicle_id,
        customers.customer_name,
        vehicles.vehicle_no,
        vehicles.vehicle_name
        FROM vehicles
        INNER JOIN customers
        ON customers.customer_id = vehicles.customer_id
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print("\n------vehicle list-------")

        for row in data:
            print(row)

           