#1  LISTY
test_accounts = ["admin", "user", "guest", "blocked_user"] #stworzenie listy

qty_accounts = len(test_accounts) #len liczy elemnty listy
print("Quantity of accounts is:", qty_accounts )
print("-"*30)

#2 PETLA FOR
for account in test_accounts:
    print("I tested log-in for:", account)

    if account == "blocked_user":
        print("USER IS BLOCKED")
    else:
        print("LOGIN STATUS: OK")
print("-"*30)

#PETLA WHILE

seconds = 0
limit_time = 3

print("Waitting for loading page...")

while seconds < limit_time:
    print("Wait for...", seconds, "s")
    seconds += 1 #inaczej seconds + 1

print("Page is loaded")

