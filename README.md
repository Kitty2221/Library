# Library

With all information about books,authors and orders stored in one place, you no longer have to sift through hoards of spreadsheets to manually search and enter data. Just enter data once, and use it across all web platform.

#### Librarian can :

- Create,update,delete book and its author. 
- See all users.
- See all orders.

#### Registered users can:

- See all available books and authors.
- Search book.
- Order books.
- See their orders. 

![photo_2023-02-26_11-16-41](https://user-images.githubusercontent.com/78548921/221402087-45a5c97d-359a-4455-8412-4263aa950856.jpg)

![photo_2023-02-26_11-14-21](https://user-images.githubusercontent.com/78548921/221401995-5542b153-7ac8-4b7f-b78b-b453f30c47f6.jpg)

![photo_2023-02-26_11-17-39](https://user-images.githubusercontent.com/78548921/221402131-4509841f-8911-4d56-9f91-c118636c965c.jpg)

# Setup

#### Create local env file

Just run `make test_env`


#### Build containers

`docker-compose -f docker-compose-dev.yml build`

#### Before running project

- Create env file with settings
- Build containers
- Run project

#### Run project

`docker-compose -f docker-compose-dev.yml up`


#### When project is running

- Apply db migrations `make migrations`
- Create superuser `make test_user`. After that you will be able to log in into app or admin
- Be happy!

#### Create new app

`make app name=<app_name>`


#### All commands you can find in `Makefile`

