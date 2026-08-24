file_name = input("Enter the file name: ").strip().lower()

if  file_name.endswith(".csv"):
    print("File accepted.")
elif file_name.endswith(".json"):
    print("File accepted.")
elif file_name.endswith(".parquet"):
    print("File accepted.")

else:
    print("File not accepted.")
