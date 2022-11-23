import os
import csv

class Account:

    def __init__(self, id, account_type, first_name, last_name, current_video_rentals):
        self.customer_id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals.split("/")
        if "" in self.current_video_rentals:
            self.current_video_rentals.remove("")

    def __repr__(self):
        return f"{self.customer_id}: {self.last_name}, {self.first_name}"
    
    def list_rented_movies(self):
        return self.current_video_rentals
    
    def rent_movie(self, movie_title):
        self.current_video_rentals.append(movie_title)
        return True

    def return_movie(self, movie_title):
        if movie_title in self.current_video_rentals:
            self.current_video_rentals.remove(movie_title)
            return True
        else:
            return False
    @classmethod
    def accounts(cls):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/customers.csv")
        
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["account_type"] == "sx":
                    accounts.append(StandardAccount(**dict(row)))
                else:
                    accounts.append(PremiumAccount(**dict(row)))

        return accounts


class StandardAccount(Account):
    def rent_movie(self, movie_title):
        if len(self.current_video_rentals) == 1:
            print("You cannot rent more than 1 movie as a standard user.")
            return False
        return super().rent_movie(movie_title)


class PremiumAccount(Account):
    def rent_movie(self, movie_title):
        if len(self.current_video_rentals) == 3:
            print("You cannot rent more than 3 movies at once.")
            return False
        return super().rent_movie(movie_title)