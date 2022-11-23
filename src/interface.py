from src.store import Store

class Interface:

    def __init__(self, store_name):
        self.store = Store(store_name)
        print(f"== Welcome to {self.store.store_name} Video! ==")

    def menu(self):
        return "---------\n1. View store video inventry\n2. View store customers\n3. View customer rented videos\n4. Add new customer\n5. Rent video\n6. Return video\n7. Exit\n---------\n"

    def view_store_video_inventory(self):
        return self.store.list_inventory()

    def view_store_customers(self):
        return self.store.list_customers()

    def view_customer_rented_videos(self):
        customer_id = input("\nEnter customer ID: ")
        for account in self.store.accounts:
            if customer_id == account.customer_id:
                return account.current_video_rentals
        return f"\nUnable to find an account with ID {customer_id}"

    def add_new_customer(self):
        while True:
            account = {}
            account["account_type"] = input("Enter account type: ")
            if account["account_type"] not in ["sx", "px"]:
                print("Not a valid account type, please enter either sx or px")
                continue
            account["first_name"] = input("Enter first name: ")
            account["last_name"] = input("Enter last name: ")
            account["current_video_rentals"] = ""
            break
        self.store.add_account(account)

    def rent_video(self):
        rental_account = input("Enter the account ID to rent from: ")
        movie_to_rent = input("Enter the title of the movie you would like to rent: ")
        movie_exists_and_in_stock = False
        account_exists = False
        for movie_index, movie in enumerate(self.store.store_inventory):
            if movie['title'] == movie_to_rent:
                if int(movie['copies_available']) > 0:
                    movie_exists_and_in_stock = True
                    rental_movie_index = movie_index
        if not movie_exists_and_in_stock:
            return f'{movie_to_rent} could not be found or is currently out of stock.'
        for account in self.store.accounts:
            if rental_account == account.customer_id:
                account_exists = True
                if account.rent_movie(movie_to_rent):
                    self.store.store_inventory[rental_movie_index]['copies_available'] = str(int(self.store.store_inventory[rental_movie_index]['copies_available']) - 1)
                    self.store.save_customers()
                    self.store.save_inventory()
                    return f'{movie_to_rent} successfully rented'
                return "Please return a movie or upgrade your account to premium if you have not to rent another movie"
        if not account_exists:
            return f'Unable to find account ID {rental_account}'
        
    def return_video(self):
        return_account =  input("Enter the account ID to return movie: ")
        movie_to_return = input("Enter the title of the movie you would like to return: ")
        for account in self.store.accounts:
            if return_account == account.customer_id:
                if account.return_movie(movie_to_return):
                    for movie in self.store.store_inventory:
                        if movie['title'] ==  movie_to_return:
                            movie['copies_available'] = str(int(movie['copies_available']) + 1)
                    self.store.save_customers()
                    self.store.save_inventory()
                    return f'{movie_to_return} successfully returned.'
                else:
                    return f'{movie_to_return} not in account {return_account}.'
        return f'Unable to find account ID {return_account}.'


    def run(self):
        while True:
            option = input(self.menu())
            if option == "1":
                self.view_store_video_inventory()
            elif option == "2":
                self.view_store_customers()
            elif option == "3":
                print(self.view_customer_rented_videos())
            elif option == "4":
                self.add_new_customer()
            elif option == "5":
                print(self.rent_video())
            elif option == "6":
                print(self.return_video())
            elif option == "7":
                print("\nExitting the program, goodbye!")
                exit()
            else:
                print("\nPlease enter a valid option")