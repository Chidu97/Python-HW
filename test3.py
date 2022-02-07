import random

data = {
    "2352747202":{
        "name":"Chidu",
        "dob":"97-10-06",
        "bvn":"123456789",
        "pin":"1234",
        "bal": 0
    },
    "2352747203":{
        "name":"Ife",
        "dob":"87-11-06",
        "bvn":"123456789",
        "pin":"1234",
        "bal": 5000
    }
}

print("Welcome to the Astrobank App")
print("Enter s to signup or l to login")
choice = input(">").lower()

if choice == 'l':
    acc_num = input("Enter your account num: \n>")
    pin = input('Enter your pin: \n>')
 
    user = data.get(acc_num)

    if user is not None and user['pin'] == pin:
        print("Success")
    else:
        print('Invalid Login') 

    if user and user['pin'] == pin:
        print(f"Welcome {user['name']}. \n Your account balance is ${user['bal']}")

        print("""What would you like to do?
        Press 1 to withdraw
        Press 2 to deposit
        Press 3 to transfer
        Press any other key to quit.""")

        user_input = input(">")

        if user_input == "1":
                amount = int(input("How much?\n>"))
                if amount >= user["bal"]:
                        print("Insufficient Funds")
                else:
                        user["bal"] -= amount
                        print(f"Please take your cash")
                        print(f"Balance is {user['bal']}")

        elif user_input == "2":
                amount = int(input("How much?\n>"))
                user["bal"] += amount
                print(f"You have added: ${amount}")
                print(f"Your balance is ${user['bal']}")
        
        elif user_input == "3":
            account_input = int(input("Enter the account number you want to send to:\n>"))
            amount = int(input("How much?\n>"))

            if amount >= user["bal"]:
                print("Insufficient funds")
            else:
                user["bal"] -= amount
                print(f"You have sent ${amount} to {account_input}")
                print(f"Your balance is ${user['bal']}")
        else:
                print("Goodbye")
    else:
        print('Invalid Login') 

elif choice == 's':
        name = input("Enter your name: \n>")
        dob = input("Enter your date of birth: \n>")
        bvn = input("Enter your BVN: \n>")
        pin = input("Enter your PIN: \n>")
        details = [('name', name), 
                   ('dob', dob),
                   ('bvn', bvn),
                   ('pin', pin),
                   ('bal',0) 
                   ]
        num = [1,2,3,4,5,6,7,8,9,0]
        acc_num1_list = [str(random.choice(num)) for _ in num]

        acc_num1 = "".join(acc_num1_list)
        data[acc_num1] = dict(details)
else:
        print("Invalid input")

# print(data)