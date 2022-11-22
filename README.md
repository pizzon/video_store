# Assessment 2: Video Inventory Manager.  <br>Object Oriented Programming + CSV Reading


## Requirements
- This assessment should be completed using Python.

## Challenge
*Back in the day*, humans would actually leave their homes to go rent a physical video copy of movies (what a strange concept, right?). Blockbuster was the leading video rental company in this era. Today, there is only one Blockbuster location left which is located in Bend, Oregon. We are going to ask you to build a video inventory application for this Blockbuster!

### Data Files Provided
 We have provided you with two data csv files. customers.csv and inventory.csv.

#### customer.csv
- id
- account_type 
- first_name 
- last_name 
- current_video_rentals (list of titles separated by '/')

#### inventory.csv
- id 
- title 
- copies_available 

### Data Management
Your Video Inventory Management application should manage the following data:

- Manage customer information:
  - customer id
  - customer account type (sx/px/sf/pf)
    - "sx" = standard account: max 1 rental out at a time
    - "px" = premium account: max 3 rentals out at a time 
  - customer first name
  - customer last name 
  - current list of video rentals (*by title*)
- Manage the store's video inventory:
  - video id
  - video title
  - number of copies currently available in-store
  
### Application Features
Your application should allow:
1. Viewing the current video inventory for the store
    - show `title` and `copies_available` for each video in the inventory
2. Viewing all customers
    - show `customer_id` and `name` for each customer in the store
3. Viewing a customer's current rented videos
    - take in a `customer_id` from the user and show current rented videos for that customer
    - each title should be listed separately (i.e. not displayed as one string with slashes straight from the CSV file)
4. Adding a new customer
    - a newly created customer should not have any rentals 
    - can you prevent duplicate ids from existing?
5. Renting a video out to a customer
    - video *by `title`*
    - customer *by `id`*
    - **IMPORTANT:** Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video!
6. Returning a video from a customer
    - video *by `title`*
    - customer *by `id`*
7. Exiting the application

Be sure to give careful consideration into what data structures & data types (including classes) you might need to use in your application logic. 

Your menu should look something like this: 
```
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View store customers
3. View customer rented videos
4. Add new customer
5. Rent video
6. Return video
7. Exit
```

## Important Grading Information
- If you're into rubrics, please enjoy [Assessment-2 Grading Rubric](https://docs.google.com/spreadsheets/d/1AlAQukmB3SS7IyW2hu0zY-9RaQnHY3lLeTi2O1fUb30/edit?usp=sharing).  Otherwise, just make sure that your code meets the basic requirements and works.  Bonus points for tests!
- You need to get a 75% or better to pass. You will pass if your code meets the basic requirements and works.
- If you fail the assessment, you have can retake it once to improve your score. You will have two weeks do do so.  You will also need to include a written explanation of how your code works.

## Rules / Process
- This test is fully open notes and open internet, but is not to be completed with the help of other students/individuals.
- Push your solution up to a private repo in your personal Github account.
- At the beginning of class on Wednesday, we will all make PRs at the same time.
