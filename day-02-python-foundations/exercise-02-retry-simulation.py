attempt = 1
max_attempts = 3
operation_successful = False

while attempt <= max_attempts:
    print(f"Attempt {attempt}")
    if attempt == 2:
        operation_successful = True
        break
    else:
        attempt += 1
          
if operation_successful == True:
    print("Operation completed successfully")    
else:
    print("Operation failed after three attempts ")