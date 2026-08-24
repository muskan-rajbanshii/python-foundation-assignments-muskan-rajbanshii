orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}


#Print every order ID and customer.
for key,value in orders.items():
    print(f"Order_ID : {key},Customer : {value['customer']}" )

# Print only completed orders.

for key,value in orders.items():
    if value["status"] == "Completed":
        print(f"completed orders : {key}")

#Calculate the total amount of completed orders.

total_amount = 0
for key,value in orders.items():
    if value["status"] == "Completed":
        total_amount += value["amount"]

print(f"Total amount of completed orders : {total_amount}")

#Count pending orders.

count = 0

for key,value in orders.items():
   if value["status"] == "Pending":
       count += 1

print(f"Count of pending orders : {count}")

# Add a new order to the dictionary.

orders["ORD-004"] = {
    "customer" : "Muskan",
    "amount" : 4500,
    "status" : "Completed"
}

print(orders)

