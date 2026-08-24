user_role = "data"
is_active  = False
requested_dataset = "salary_data"

allowed_roles = ["analyst","scientist","engineer"]
restricted_datasets = ["salary_data","personal_data"]



if user_role in allowed_roles and  is_active  and  requested_dataset not  in restricted_datasets:
    print("Grant access")
else:
    if user_role not in allowed_roles:
        print("Access denied because the user is not allowed.")
        
    if is_active == False:
        print("Access denied because the user is inactive.")
        

    if requested_dataset in restricted_datasets:
        print("Access denied because the dataset is restricted.")
        
    