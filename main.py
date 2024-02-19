print('Welcome to Online Shopping Mart!!')

# for reading the information saved in a file for verification
f = open('Account info.txt', 'a+')
f.seek(0)
check = f.read()
f.close()
if check == '':
    info = []  # this variable will be executed to prevent the 1st iteration and check the info in the file
else:
    info = check.split()
while True:
    for i in info:
        if i == 'Username:' or i == ',Password:':
            info.remove(i)
    print()
    # user input to create an account or log in
    acc_info = input('Select the choice 1. Create an account, 2.Log into account: ')
    print()

    # creating an account
    if acc_info == '1':
        print('For creating an account, you have to fulfill the requirements.')
        print()

        # Taking information from user for making an account
        while True:
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            address = input('Enter your residential address: ')
            username1 = input('Enter the username: ')
            password1 = input('Enter the password for your account: ')
            print()
            if username1.isdigit():
                print('You should write an alphabet too in your username!')
                break
            if len(password1) == 0 or len(first_name) == 0 or len(last_name )== 0 or len(username1) == 0 or len(address) == 0:
                print('You should give all info!')
                break
            if ' ' in username1:
                print('There should be no space in username')
                break
            if ' ' in password1:
                print('There should be no space in password')
                break
            # checking info in file
            if info:
                if username1 in info:
                    print('You should enter a unique username! ')
                    print()
                if password1 in info:
                    print('You should enter a unique password! ')
                    print()

            # entering the info in the file
                if username1 not in info and password1 not in info:
                    f = open('Account info.txt', 'a+')
                    f.write(f'Username: {username1:20},Password: {password1:20}\n')
                    f.seek(0)
                    info = f.read()
                    info = info.split()
                    f.close()

                    # saving the information of user in User_info.txt file
                    f = open('User_info.txt', 'a+')
                    f.write(f'First Name: {first_name:20},Last Name: {last_name:20},Address: {address:30},Username: {username1:20},Password: {password1:20} \n')
                    f.close()
                    print('You have successfully created your account!')
                    break

            if not info:
                f = open('Account info.txt', 'a+')
                f.write(f'Username: {username1:20},Password: {password1:20}\n')
                f.seek(0)
                info = f.read()
                info = info.split()
                f.close()

                # saving the information of user in User_info.txt file
                f = open('User_info.txt', 'a+')
                f.write(f'First Name: {first_name:20},Last Name: {last_name:20},Address: {address:30},Username: {username1:20},Password: {password1:20} \n')
                f.close()
                print('You have successfully created your account!')
                break

    # once account is created, then logging into account
    if acc_info == '2':
        print('For logging into account, you have to verify your account')
        print()

        # verifying information for log in
        username2 = input('Enter your username: ')
        password2 = input('Enter your password: ')
        print()
        if username2 in info:
            ind = info.index(username2)
            if password2 == info[ind+1]:
                print('You have been successfully logged into Online Shopping Mart!', username2.capitalize())
                print()
                break
            else:
                print('You have entered wrong info, please correct info for log in!')
                print()
        else:
            print("You have entered the wrong username")

# item list
items = {'COOKIEBOX': 100, 'FACEWASH': 150, 'SHOES': 1000, 'WASHINGPOWDER': 350, 'COOKINGOIL': 400, 'SOFTDRINK': 80, 'SHAMPOO': 200, 'MEDICINE': 120, 'CHICKEN': 250, 'BEEF': 300}
items_names = items.keys()


# defining function for whole shopping

def view_list():
    print()
    for item,price in items.items():
        print(f'{item:15}Rs.{price}')


def add_products():
    print()
    print(items_names)
    f = open('products.txt', 'a+')
    if count1 == 1:  # not to write name and products again and again
        f.write(f'\nTime:{time.ctime()}  ,Name: {username2.capitalize()} ,Product: ')
    while True:
        products = input("Type the products you want to select, if you want to cancel,press 'E': ")
        products = products.upper()
        # checking the products
        if products in items_names:
            f.write(f' {products} ')
        if products not in items_names and products != 'E':
            print('You should select the appropriate items')
        if products == 'E':
            f.close()
            break


def remove_products():
    if count1 >= 1:
        f = open('products.txt')
        read = f.read()
        f.close()
        view = read.split()
        see = []  # this will use in making a separate list of products
        for i in range(len(view) - 1, -1, -1):
            if view[i] != ',Product:':
                see += [view[i]]
            if view[i] == ',Product:':
                break

        while True:
            remove = input("Type the products from the list you want to remove, if you want to cancel, press 'E': ")
            remove = remove.upper()
            if see:
                if remove in items_names:
                    see.remove(remove)
                if remove not in items_names and remove != 'E':
                    print('You should select the appropriate items')
                if remove == 'E':
                    print(see)
                    break
            if not see:
                if remove == 'E':
                    print(see)
                    break
                print('The cart is empty, you should pick some things!')

        if see or not see:
            # updating the file after removing some items
            string = ''
            for i in range(len(read) - 1, -1, -1):
                if read[i] != ':':
                    string += read[i]
                if read[i] == ':':
                    break
            new_str = ''
            for i in range(len(string) - 1, -1, -1):
                new_str += string[i]

            # replacing the material in the file with the new one
            f = open('products.txt', 'w')
            read = read.replace(new_str, '')
            f.write(read)
            for i in see:
                f.write(f' {i}')
            f.close()

    else:
        print('The cart is empty, you should pick some things!')
        print()


def view_cart():
    if count1 >= 1:
        f = open('products.txt')
        view = f.read()
        f.close()
        view = view.split()
        see = []  # this will use in making a separate list of products
        for i in range(len(view) - 1, -1, -1):
            if view[i] != ',Product:':
                see += [view[i]]
            if view[i] == ',Product:':
                print('Your products in your cart,', see)
                break
    else:
        print('The cart is empty, you should pick some things!')
        print()
        

def checkout(bill):
    if count1 >= 1:
        f = open('products.txt')
        view = f.read()
        f.close()
        view = view.split()
        see = []  # this will use in making a separate list of products
        for i in range(len(view) - 1, -1, -1):
            if view[i] != ',Product:':
                see += [view[i]]
            if view[i] == ',Product:':
                break
        if see:
            for i in see:  # calculating the bill
                bill += items[i]
        if not see:
            bill == 0

        print('Your bill for your product is Rs.', bill)
        if bill != 0:
            print('Your products will be delivered in 6 hours!')
            print()
        return bill
    else:
        print('The cart is empty, you should pick some things!')
        print()


def view_history():
    f = open('products.txt')
    history = f.readlines()
    f.close()
    for i in history:
        if username2.capitalize() in i:
            print(i)


count1 = 0
count2 = 0

print('What are you gonna do?', username2.capitalize())
# user input for shopping
while True:
    print()
    choice = input('Select the given options: \n1. View product list \n2. Add products to cart \n3. Remove products from cart \n4. View cart \n5. Checkout \n6. View shopping history \n7. Exit the application  ')

    # The point where the shopping starts
    if choice == '1':
        view_list()
    if choice == '2':
        import time
        count1 += 1
        add_products()
    if choice == '3':
        remove_products()
    if choice == '4':
        view_cart()
    if choice == '5':
        count2 += 1
        bill = 0
        bill = checkout(bill)
    if choice == '6':
        view_history()
    if choice == '7':
        # after paying the bill, bill info is written in file
         if count1 >= 1 and count2 != 0:
            f = open('products.txt', 'a+')
            f.write(f' ,Bill: Rs. {bill} ')
            f.close()
            print('Thanks for visiting Online Shopping Mart!')
            exit()
        if count2 == 0:
            print('Thanks for visiting Online Shopping Mart!')
            exit()
