from src.accounts import Account, StandardAccount, PremiumAccount
import os
import csv

class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        self.store_inventory = self.inventory()
        self.accounts = Account.accounts()

    def inventory(self):
        inventory = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                inventory.append((dict(row)))

        return inventory

    def list_inventory(self):
        for video in self.store_inventory:
            print("\n", video)

    def list_customers(self):
        for account in self.accounts:
            print("\n", account)
    
    def add_account(self, account_data):
        account_data["id"] = str((int(self.accounts[-1].customer_id) + 1))
        if account_data["account_type"] == "sx":
            self.accounts.append(StandardAccount(**account_data))
            print("Account successfully created!")
        else:
            self.accounts.append(PremiumAccount(**account_data))
            print("Account sucecssfully created!")
        self.save_customers()

    def save_customers(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(['id','account_type','first_name','last_name','current_video_rentals'])
            for customer in self.accounts:
                customer_csv.writerow([customer.customer_id, customer.account_type, customer.first_name, customer.last_name, "/".join(customer.current_video_rentals)])

    def save_inventory(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")

        with open(path, 'w') as csvfile:
            inventory_csv = csv.writer(csvfile, delimiter=',')
            inventory_csv.writerow(['id','title', 'copies_available'])
            for movie in self.store_inventory:
                inventory_csv.writerow([movie['id'], movie['title'], movie['copies_available']])