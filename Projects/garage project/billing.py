from database import Database
from datetime import date
class billing:
    def __init__(self):
        self.db = Database()
        self.con = self.db.connect()
        self.cursor = self.con.cursor()

    def generate_bill(self):

        vehicle_id = int(input("Enter Vehicle ID : "))

        print("\n------ Services ------")
        print("1. Car Wash        ₹500")
        print("2. Oil Change      ₹1000")
        print("3. Brake Service   ₹1500")
        print("4. Wheel Alignment ₹800")
        print("5. Full Service    ₹5000")

        choice = int(input("\nSelect Service : "))

        if choice == 1:
            service = "Car Wash"
            amount = 500
        elif choice==2:
            service = "oil change"
            amount= 1000
        elif choice == 3:
            service = "brake service"
            amount = 1500
        elif choice == 4:
            service = "wheel alignment"
            amount = 800
        elif choice == 5:
            service = "full service"
            amount = 5000
        else:
            print("invalid choice")
            return
        sql = """
        INSERT INTO bills(vehicle_id, service, amount, bill_date)
        VALUES(%s, %s, %s, %s)
        """

        value = (vehicle_id, service, amount, date.today())

        self.cursor.execute(sql, value)
        self.con.commit()

        print("\n========== BILL ==========")
        print("Service :", service)
        print("Amount  : ₹", amount)
        print("Date    :", date.today())
        print("==========================")
        print("Bill Generated Successfully.")

    def view_bills(self):

        sql = """
        SELECT
            bills.bill_id,
            customers.customer_name,
            vehicles.vehicle_no,
            bills.service,
            bills.amount,
            bills.bill_date
        FROM bills
        INNER JOIN vehicles
        ON bills.vehicle_id = vehicles.vehicle_id
        INNER JOIN customers
        ON vehicles.customer_id = customers.customer_id
        """

        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print("\n------vehicle list-------")

        for row in data:
            print(row)

        
