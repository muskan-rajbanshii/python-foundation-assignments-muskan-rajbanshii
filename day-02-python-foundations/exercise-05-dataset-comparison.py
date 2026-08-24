dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

#All unique dataset names
unique_datasets = dataset_a . union(dataset_b)
print(f" All Unique dataset names: {unique_datasets}")

#Datasets found in both groups

common_datasets = dataset_a.intersection(dataset_b)
print(f"Dataset found in both groups : {common_datasets}")

#Datasets only in dataset_a

dataonly_in_dataset_a = dataset_a.difference(dataset_b)
print(f"Datasets only in dataset_a : {dataonly_in_dataset_a}")

#Datasets only in dataset_b

dataonly_in_dataset_b = dataset_b.difference(dataset_a)
print(f"Datasets only in dataset_b : {dataonly_in_dataset_b}")