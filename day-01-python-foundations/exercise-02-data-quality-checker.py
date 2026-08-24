total_rows = 2000
missing_rows = 120
duplicate_rows = 30

total_problematic_rows = missing_rows +  duplicate_rows
percentage_of_problematic_rows = (total_problematic_rows)/total_rows * 100
print(f"Total rows : {total_rows}")
print(f"Problematic rows : {total_problematic_rows}")
print(f"Problem percentage : {percentage_of_problematic_rows}")

print("Final classification of Datasets: ")
if percentage_of_problematic_rows <= 2 :
    print("Excellent")
elif   2 < percentage_of_problematic_rows <= 5:
    print("Acceptable")
else:
    print("Needs Cleaning")