import mysql.connector
class BankAccount:
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor()

    def create_account(self, name, balance):
        query = "INSERT INTO accounts (name, balance) VALUES (%s, %s)"
        values = (name, balance)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Account created successfully!")

    def deposit(self, account_id, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        query = "UPDATE accounts SET balance = balance + %s WHERE id = %s"
        values = (amount, account_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"{amount} deposited successfully.")

    def withdraw(self, account_id, amount):
        query = "SELECT balance FROM accounts WHERE id = %s"
        self.cursor.execute(query, (account_id,))
        result = self.cursor.fetchone()
        
        if result is None:
            print("Account not found.")
            return
        
        balance = result[0]
        
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            query = "UPDATE accounts SET balance = balance - %s WHERE id = %s"
            values = (amount, account_id)
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"{amount} withdrawn successfully.")

    def check_balance(self, account_id):
        query = "SELECT name, balance FROM accounts WHERE id = %s"
        self.cursor.execute(query, (account_id,))
        result = self.cursor.fetchone()
        
        if result:
            name, balance = result
            print(f"Account: {name}, Balance: {balance}")
        else:
            print("Account not found.")

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '123456',   
        'database': 'bank_account'
    }

    bank = BankAccount(db_config)
    while True:
        print("\nBank Account Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial deposit: "))
            bank.create_account(name, balance)

        elif choice == "2":
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_id, amount)

        elif choice == "3":
            account_id = int(input("Enter account ID: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_id, amount)

        elif choice == "4":
            account_id = int(input("Enter account ID: "))
            bank.check_balance(account_id)

        elif choice == "5":
            print("Exiting program.")
            bank.close()
            break
        else:
            print("Invalid choice! Please try again.")
