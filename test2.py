import random
from re import S


# data = {
#     "23527472":{
#         "name":"Chidu",
#         "dob":"97-10-06",
#         "bvn":"123456789",
#         "pin":"1234",
#         "bal": 5000
#     }
# }

data = {
    "account":"23527472",
    "name":"Chidu",
    "dob":"97-10-06",
    "bvn":"123456789",
    "pin":"1234",
    "bal": 5000
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
        print(f"Welcome {user['name']}. \nYour account balance is ${user['bal']}")
    else:
        print('Invalid Login')

elif choice == 's':
    name_input = input("Enter your name: \n>")
    dob_input = input("Enter dob in this format DD-MM-YY: \n>")

    acctNums = random.sample(range(1, 10), 8)
    
    print(f"Welcome you are signed up here is your account number: {acctNums}")

# withdrawal function

# data = {
#     "account":"23527472",
#     "name":"Chidu",
#     "dob":"97-10-06",
#     "bvn":"123456789",
#     "pin":"1234",
#     "bal": 5000
#     }


user_bal = data.get("bal")
wit_amount = int(input("Enter the amount you wish to withdraw: \n>"))

if wit_amount == "":
    print("No entry")

else:
    if user_bal >= wit_amount:
        user_bal -= wit_amount
        print(f"You withdrew: ${wit_amount}")
        print(f"Your main balance is: ${user_bal}")
    else:
        print("Insufficient Balance")


dep_amount = int(input("Enter the amount you wish to deposit: \n>"))
user_bal += dep_amount
print(f"Amount deposited: ${dep_amount}")
print(f"Your main balance is: ${user_bal}")




   








