import sys
# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

def transfer(from_acc, to_acc, amount):
    change_balance(from_acc, -amount)
    change_balance(to_acc, amount)


def change_balance(account_number, amount):
    temp_index = get_index_by_id(account_number)
    if accounts[temp_index]['balance'] + amount > 0:
        accounts[temp_index]['balance'] += amount
    else:
        print("403 - forbidden")
        sys.exit()

def get_index_by_id(account_number_id):
    for account in accounts:
        if account['account_number'] == account_number_id:
            return accounts.index(account)
    print("404")

print(transfer(11234543, None, None))